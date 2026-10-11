"""Prepare a lossless, non-playable question draft from the supplied CSV files."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_FILE = "2026-QUESTIONS TOUTES LES LANGUES - TAB 2 (2).csv"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"Malformed CSV row: {path.name}")
    return rows


def prepare(metadata, translations):
    by_id = {}
    for row in metadata:
        identifier = int(row["id"])
        if identifier in by_id:
            raise ValueError(f"Duplicate metadata ID: {identifier}")
        category = int(row["categoryId"])
        difficulty = int(row["difficulty"]) if row["difficulty"] else None
        region = int(row["domainId"]) if row["domainId"] else None
        if category not in range(1, 6):
            raise ValueError(f"Unknown category: {identifier}")
        if category == 5:
            if difficulty is not None or region not in range(1, 11):
                raise ValueError(f"Invalid shared Domains metadata: {identifier}")
        elif difficulty not in (1, 2, 3) or region is not None:
            raise ValueError(f"Invalid level/region: {identifier}")
        by_id[identifier] = {
            "id": identifier,
            "categoryId": category,
            "regionId": region,
            "difficulty": difficulty,
            "type": None,
            "choices": None,
            "correctChoiceIds": None,
            "imagePath": row["imageUrl"] or None,
            "translations": {},
            "sourceMetadata": dict(row),
            "reviewStatus": "pending",
        }
    for row in translations:
        identifier = int(row["questionId"])
        if identifier not in by_id:
            raise ValueError(f"Translation without metadata: {identifier}")
        language = row["language"]
        if language not in ("fr", "en"):
            raise ValueError(f"Unknown language: {identifier}/{language}")
        target = by_id[identifier]["translations"]
        if language in target:
            raise ValueError(f"Duplicate translation: {identifier}/{language}")
        if not row["question"].strip() or not row["answer"].strip():
            raise ValueError(f"Empty content: {identifier}/{language}")
        target[language] = {
            "question": row["question"],
            "answer": row["answer"],
            "sourceTranslation": dict(row),
        }
    for identifier, question in by_id.items():
        if set(question["translations"]) != {"fr", "en"}:
            raise ValueError(f"Incomplete bilingual pair: {identifier}")
    return [by_id[key] for key in sorted(by_id)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check generated draft without writing")
    args = parser.parse_args()
    sources = ROOT / "sources/questions"
    paths = [sources / "QuestionsId.csv", sources / TEXT_FILE]
    fingerprints = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    questions = prepare(read_csv(paths[0]), read_csv(paths[1]))
    draft = {
        "schemaVersion": 1,
        "status": "draft_not_playable",
        "sourceSha256": fingerprints,
        "questions": questions,
    }
    destination = ROOT / "data/preparation/questions.draft.json"
    encoded = json.dumps(draft, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if destination.read_text(encoding="utf-8") != encoded:
            raise ValueError("Draft differs from the current sources; regenerate explicitly")
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(encoded, encoding="utf-8")
    assert fingerprints == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    print(f"{len(questions)} bilingual questions; source text preserved; draft {'checked' if args.check else 'written'}")


if __name__ == "__main__":
    main()
