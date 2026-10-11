"""Extract explicit choices and keys; keep ambiguous records out of the usable bank."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def display(text):
    return re.sub(r"\\+n", "\n", text)


def approved_format(question_id, language, text, answer):
    """Apply only the five owner-approved format repairs, without touching sources."""
    text = display(text)
    correction = None
    pattern, replacement = None, None
    if question_id == 108:
        # Only the parsing input gets punctuation; expectedAnswer retains the source.
        pattern, replacement = r"^B\s+", "B : "
        answer, count = re.subn(pattern, replacement, answer, count=1)
        if count != 1:
            raise ValueError(f"Approved correction no longer matches: {question_id}/{language}")
        correction = "108_explicit_answer_B"
    elif question_id == 166 and language == "en":
        pattern, replacement = r"(?<!\n) E:\s*", "\nE: "
        correction = "166_separate_choice_E_en"
    elif question_id == 511 and language == "en":
        pattern, replacement = r"(?<!\n) D:\s*", "\nD: "
        correction = "511_separate_choice_D_en"
    elif question_id == 532 and language == "fr":
        pattern, replacement = r"\\+B\s*:\s*", "\nB: "
        correction = "532_restore_separator_B_fr"
    elif question_id == 564 and language == "fr":
        pattern, replacement = r"(?<=\n)b\s*:\s*", "B: "
        correction = "564_uppercase_choice_B_fr"
    if correction and question_id != 108:
        text, count = re.subn(pattern, replacement, text)
        if count != 1:
            raise ValueError(f"Approved correction no longer matches: {question_id}/{language}")
    return text, answer, correction


def parse(text, answer):
    text, answer = display(text), display(answer)
    markers = list(re.finditer(r"(?:^|\n)\s*([A-F])\s*[:.)]\s*", text))
    if markers:
        choices = [{"id": m[1], "text": text[m.end():markers[i+1].start() if i+1 < len(markers) else len(text)].strip()} for i, m in enumerate(markers)]
        ids = [c["id"] for c in choices]
        if len(ids) < 2 or len(set(ids)) != len(ids) or ids != [chr(65+i) for i in range(len(ids))]:
            return None, "non-consecutive or incomplete choices"
        if re.search(r"\\+(?!n)[A-F]\s*:", text):
            return None, "malformed choice separator"
        lead = answer.strip()
        lead = re.sub(r"^(?:réponses?|answers?)\s*:?\s*", "", lead, flags=re.I)
        match = re.match(r"^([A-F](?:\s*(?:et|and|,|&)\s*[A-F])*)\s*[:.]", lead)
        correct = re.findall(r"[A-F]", match[1]) if match else []
        if not correct:
            listed = re.findall(r"(?:^|\n)\s*([A-F])\s*:", lead)
            if listed:
                correct = listed
        if not correct:
            matched = [c["id"] for c in choices if lead.casefold().startswith(c["text"].rstrip(". ").casefold()+".")]
            if len(matched) == 1:
                correct = matched
        # Answers such as A:..., D:..., E:... explicitly list multiple keys.
        if re.match(r"^[A-F]\s*:", lead):
            listed = re.findall(r"(?:^|\n|\.\s*,?\s*)\s*([A-F])\s*:", lead)
            if len(listed) > 1:
                correct = listed
        if not correct or not set(correct) <= set(ids):
            return None, "answer key not explicit enough"
        return {"type": "qcm", "question": text[:markers[0].start()].strip(), "choices": choices, "correctChoiceIds": sorted(set(correct))}, None
    if re.search(r"vrai\s*ou\s*faux|true\s*or\s*false", text, re.I):
        match = re.match(r"\s*(vrai|faux|true|false)\b", answer, re.I)
        if not match:
            return None, "true/false key missing"
        return {"type": "true_false", "question": text, "choices": [], "correctChoiceIds": ["true" if match[1].lower() in ("vrai", "true") else "false"]}, None
    if re.search(r"(?:^|\n|\\)\s*[A-F]\s*[:.)]", text):
        return None, "possible unparsed choices"
    return {"type": "open", "question": text, "choices": [], "correctChoiceIds": []}, None


def main():
    draft = json.loads((ROOT / "data/preparation/questions.draft.json").read_text())
    usable, review = [], []
    for source in draft["questions"]:
        parsed, errors, corrections = {}, [], {}
        for lang in ("fr", "en"):
            raw = source["translations"][lang]
            text, answer, correction = approved_format(source["id"], lang, raw["question"], raw["answer"])
            if correction:
                corrections[lang] = correction
            value, error = parse(text, answer)
            if error:
                errors.append(f"{lang}: {error}")
            else:
                parsed[lang] = {**value, "expectedAnswer": display(raw["answer"])}
        if not errors and (parsed["fr"]["type"] != parsed["en"]["type"] or parsed["fr"]["correctChoiceIds"] != parsed["en"]["correctChoiceIds"] or [c["id"] for c in parsed["fr"]["choices"]] != [c["id"] for c in parsed["en"]["choices"]]):
            errors.append("FR/EN structure or answer keys disagree")
        if errors:
            review.append({"id": source["id"], "reasons": errors, "source": source})
        else:
            usable.append({"id": source["id"], "categoryId": source["categoryId"], "regionId": source["regionId"], "difficulty": source["difficulty"], "type": parsed["fr"]["type"], "correctChoiceIds": parsed["fr"]["correctChoiceIds"], "translations": {lang: {"question": v["question"], "expectedAnswer": v["expectedAnswer"], "choices": v["choices"]} for lang,v in parsed.items()}, "provenance": {"sourceQuestionId": source["id"], "status": "source_extracted_not_editorially_verified", "approvedFormatCorrections": corrections}})
    for filename, payload in [("questions.json", {"schemaVersion": 1, "questions": usable, "sourceSha256": draft["sourceSha256"]}), ("preparation/questions.review.json", {"schemaVersion": 1, "questions": review})]:
        (ROOT / "data" / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
    report = "# Structuration des questions\n\nExtraction des marqueurs explicites uniquement ; pas de correction scientifique ou traduction inventée. Les textes sources complets restent dans questions.draft.json. Les réponses et explications sont conservées ensemble dans expectedAnswer. Les séquences de saut de ligne sont normalisées dans les seuls fichiers dérivés.\n\n"
    report += f"{len(usable)} questions structurées ; {len(review)} questions isolées pour revue, jamais reclassées en ouvertes par défaut. Types : {dict(Counter(q['type'] for q in usable))}.\n\n"
    report += "## Corrections de format validées et appliquées\n\nIDs 108, 166, 511, 532 et 564 : corrections limitées aux données dérivées, approuvées par le porteur. Leur trace par langue est conservée dans provenance.approvedFormatCorrections. Les réponses affichées restent celles de la source (avec sauts de ligne normalisés).\n\n"
    report += "## Cas de format à revoir\n\n" + ("\n".join(f"- ID {q['id']} : {'; '.join(q['reasons'])}" for q in review) or "Aucun cas restant dans la file de revue de formats.")
    report += "\n\nCette extraction garantit une structure compatible FR/EN, pas la justesse éditoriale. Les signalements de contenu de l’audit (notamment ID 2) restent ouverts. Aucun type de choix vrai/faux traduit nouveau n’est ajouté ici : les boutons devront utiliser des libellés d’interface validés.\n"
    (ROOT / "docs/STRUCTURATION_QUESTIONS.md").write_text(report)
    print(f"{len(usable)} structured; {len(review)} pending review")


if __name__ == "__main__":
    main()
