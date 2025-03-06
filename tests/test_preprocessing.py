import unittest
from scripts.preprocess_data import clean_text, preprocess_data

class TestPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        """
        Test if the clean_text function removes HTML tags and special characters.
        """
        raw_text = "<p>This is a <strong>test</strong> string with <em>HTML</em> tags!</p>"
        cleaned_text = clean_text(raw_text)
        expected_text = "This is a test string with HTML tags"
        self.assertEqual(cleaned_text, expected_text)

    def test_preprocess_data(self):
        """
        Test if the preprocess_data function correctly processes a list of raw data.
        """
        raw_data = [
            {"id": 1, "text": "<p>Apple Inc. reported <strong>record earnings</strong> for Q4 2023.</p>"},
            {"id": 2, "text": "The Federal Reserve announced an interest rate hike."},
            {"id": 3, "text": "Tesla unveiled its new <em>electric vehicle</em> model."}
        ]
        processed_data = preprocess_data(raw_data)
        self.assertIsInstance(processed_data, list)
        self.assertEqual(len(processed_data), 3)
        self.assertEqual(processed_data[0]["text"], "Apple Inc. reported record earnings for Q4 2023.")
        self.assertEqual(processed_data[1]["text"], "The Federal Reserve announced an interest rate hike.")
        self.assertEqual(processed_data[2]["text"], "Tesla unveiled its new electric vehicle model.")

if __name__ == "__main__":
    unittest.main()