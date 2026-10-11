import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("prepare_questions", Path(__file__).resolve().parents[2] / "scripts/prepare_questions.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.metadata = [{"id": "1", "categoryId": "5", "difficulty": "", "domainId": "2", "translations": "1", "imageUrl": "", "createdAt": "source-date"}]
        self.translations = [{"quel ": str(index), "questionId": "1", "language": language, "question": " Texte \\nA: choix", "answer": "A et B : texte inchangé", "createdAt": "source-date"} for index, language in enumerate(("fr", "en"), 1)]

    def test_domains_stay_shared_and_text_is_lossless(self):
        question = module.prepare(self.metadata, self.translations)[0]
        self.assertIsNone(question["difficulty"])
        self.assertIsNone(question["type"])
        self.assertIsNone(question["correctChoiceIds"])
        self.assertEqual(question["regionId"], 2)
        self.assertEqual(question["sourceMetadata"], self.metadata[0])
        for source in self.translations:
            result = question["translations"][source["language"]]
            self.assertEqual(result["question"], source["question"])
            self.assertEqual(result["answer"], source["answer"])
            self.assertEqual(result["sourceTranslation"], source)

    def test_duplicate_pair_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate translation"):
            module.prepare(self.metadata, self.translations + [self.translations[0]])

    def test_missing_language_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Incomplete bilingual"):
            module.prepare(self.metadata, self.translations[:1])

    def test_orphan_translation_is_rejected(self):
        self.translations[0]["questionId"] = "99"
        with self.assertRaisesRegex(ValueError, "without metadata"):
            module.prepare(self.metadata, self.translations)

    def test_invented_domain_level_is_rejected(self):
        self.metadata[0]["difficulty"] = "1"
        with self.assertRaisesRegex(ValueError, "shared Domains"):
            module.prepare(self.metadata, self.translations)

    def test_duplicate_metadata_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate metadata"):
            module.prepare(self.metadata * 2, self.translations)


if __name__ == "__main__":
    unittest.main()
