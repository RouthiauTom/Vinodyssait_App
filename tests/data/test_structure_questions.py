import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('structure_questions', ROOT / 'scripts/structure_questions.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class StructureTests(unittest.TestCase):
    def test_approved_repairs_on_real_bilingual_sources(self):
        source = json.loads((ROOT/'data/preparation/questions.draft.json').read_text())['questions']
        expected = {108: ('B',3), 166: ('D',5), 511: ('C',4), 532: ('B',3), 564: ('B',4)}
        for question in source:
            if question['id'] not in expected:
                continue
            key, count = expected[question['id']]
            for language, raw in question['translations'].items():
                with self.subTest(id=question['id'], language=language):
                    original = dict(raw)
                    text, answer, correction = module.approved_format(question['id'], language, raw['question'], raw['answer'])
                    value, error = module.parse(text, answer)
                    self.assertIsNone(error)
                    self.assertEqual(value['correctChoiceIds'], [key])
                    self.assertEqual(len(value['choices']), count)
                    self.assertEqual(raw, original)

    def test_approved_repair_rejects_changed_source(self):
        with self.assertRaisesRegex(ValueError, 'no longer matches'):
            module.approved_format(532, 'fr', 'Different source text', 'B: answer')

    def test_complete_bank_and_answer_text_preserved(self):
        sources = {q['id']: q for q in json.loads((ROOT/'data/preparation/questions.draft.json').read_text())['questions']}
        bank = json.loads((ROOT/'data/questions.json').read_text())['questions']
        self.assertEqual(len(bank), 673)
        self.assertEqual(json.loads((ROOT/'data/preparation/questions.review.json').read_text())['questions'], [])
        corrected = set()
        for question in bank:
            if question['provenance']['approvedFormatCorrections']:
                corrected.add(question['id'])
            for language, value in question['translations'].items():
                self.assertEqual(value['expectedAnswer'], module.display(sources[question['id']]['translations'][language]['answer']))
        self.assertEqual(corrected, {108,166,511,532,564})

    def test_multiple_keys_are_not_reduced_to_first_letter(self):
        for answer, expected in [('B et C : réponse', ['B', 'C']), ('A: choix.\nB: choix.\nC: choix.', ['A', 'B', 'C']), ('Réponses : A : choix., D : choix., E : choix.', ['A', 'D', 'E'])]:
            value, error = module.parse('Question?\nA: premier\nB: deuxième\nC: troisième\nD: quatrième\nE: cinquième', answer)
            self.assertIsNone(error)
            self.assertEqual(value['correctChoiceIds'], expected)

    def test_malformed_separator_requires_review(self):
        value, error = module.parse('Question?\\nA: premier\\B: deuxième\\nC: troisième', 'B: deuxième')
        self.assertIsNone(value)
        self.assertIsNotNone(error)

    def test_true_false_is_derived_from_explicit_reference(self):
        value, error = module.parse('Vrai ou Faux ? texte', 'FAUX. Explication')
        self.assertIsNone(error)
        self.assertEqual(value['correctChoiceIds'], ['false'])

    def test_open_answer_is_not_evaluated_as_text(self):
        value, error = module.parse('Question orale ?', 'Réponse attendue')
        self.assertIsNone(error)
        self.assertEqual(value['type'], 'open')
        self.assertEqual(value['correctChoiceIds'], [])

    def test_all_source_ids_accounted_for_once(self):
        source = json.loads((ROOT/'data/preparation/questions.draft.json').read_text())['questions']
        bank = json.loads((ROOT/'data/questions.json').read_text())['questions']
        review = json.loads((ROOT/'data/preparation/questions.review.json').read_text())['questions']
        ids = [q['id'] for q in bank+review]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {q['id'] for q in source})
        for q in bank:
            self.assertEqual(set(q['translations']), {'fr','en'})
            if q['categoryId'] == 5:
                self.assertIsNone(q['difficulty'])


if __name__ == '__main__':
    unittest.main()
