import unittest
from scripts.rag_pipeline import load_rag_model, generate_insights

class TestRAGPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Load the RAG model once for all tests.
        """
        cls.tokenizer, cls.retriever, cls.model = load_rag_model()

    def test_load_rag_model(self):
        """
        Test if the RAG model, tokenizer, and retriever are loaded correctly.
        """
        self.assertIsNotNone(self.tokenizer)
        self.assertIsNotNone(self.retriever)
        self.assertIsNotNone(self.model)

    def test_generate_insights(self):
        """
        Test if the RAG pipeline generates insights for a query.
        """
        query = "What are the key risks for Apple in 2023?"
        insights = generate_insights(query, self.tokenizer, self.model)
        self.assertIsNotNone(insights)
        self.assertIsInstance(insights, str)
        self.assertTrue(len(insights) > 0)

if __name__ == "__main__":
    unittest.main()