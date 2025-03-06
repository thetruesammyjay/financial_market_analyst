import requests
import yaml
from utils.helpers import setup_logger

# Load API keys
with open("config/api_keys.yaml", "r") as f:
    config = yaml.safe_load(f)

# Set up logger
logger = setup_logger("scrape_sec_filings")

def fetch_sec_filings(company_ticker):
    try:
        url = f"https://api.sec.gov/company/{company_ticker}/filings"
        headers = {"User-Agent": "Financial Market Analyst", "Authorization": f"Bearer {config['sec_edgar']['api_key']}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        filings = response.json()
        logger.info(f"Fetched {len(filings)} filings for {company_ticker}")
        return filings
    except Exception as e:
        logger.error(f"Error fetching filings for {company_ticker}: {e}")
        return []

if __name__ == "__main__":
    company_ticker = "AAPL"
    filings = fetch_sec_filings(company_ticker)
    print(filings)