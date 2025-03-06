import requests
from bs4 import BeautifulSoup
import yaml
from utils.helpers import setup_logger

# Load API keys
with open("config/api_keys.yaml", "r") as f:
    config = yaml.safe_load(f)

# Set up logger
logger = setup_logger("scrape_news")

def scrape_financial_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        news_data = []
        for article in articles:
            title = article.find("h3").text.strip()
            link = article.find("a")["href"]
            news_data.append({"title": title, "link": link})
        logger.info(f"Scraped {len(news_data)} articles from {url}")
        return news_data
    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")
        return []

if __name__ == "__main__":
    url = "https://www.reuters.com/finance"
    news_data = scrape_financial_news(url)
    print(news_data)