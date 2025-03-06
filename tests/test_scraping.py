import unittest
from scripts.scrape_news import scrape_financial_news

class TestScraping(unittest.TestCase):
    def test_scrape_financial_news(self):
        url = "https://www.reuters.com/finance"
        news_data = scrape_financial_news(url)
        self.assertIsInstance(news_data, list)
        self.assertTrue(len(news_data) > 0)

if __name__ == "__main__":
    unittest.main()