from scripts.scrape_news import scrape_financial_news
from scripts.scrape_sec_filings import fetch_sec_filings
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("data_ingestion")

def run_data_ingestion():
    try:
        # Scrape financial news
        news_data = scrape_financial_news("https://www.reuters.com/finance")
        # Fetch SEC filings
        filings_data = fetch_sec_filings("AAPL")
        logger.info("Data ingestion completed successfully")
        return {"news": news_data, "filings": filings_data}
    except Exception as e:
        logger.error(f"Error during data ingestion: {e}")
        return None