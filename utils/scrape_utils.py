import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("scrape_utils")

def fetch_page_content(url):
    """
    Fetch the content of a web page using requests.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info(f"Successfully fetched content from {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching content from {url}: {e}")
        return None

def parse_html(html_content):
    """
    Parse HTML content using BeautifulSoup.
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        logger.info("HTML content parsed successfully")
        return soup
    except Exception as e:
        logger.error(f"Error parsing HTML content: {e}")
        return None

def setup_selenium_driver():
    """
    Set up a Selenium WebDriver for dynamic content scraping.
    """
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set up the WebDriver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        logger.info("Selenium WebDriver setup successfully")
        return driver
    except Exception as e:
        logger.error(f"Error setting up Selenium WebDriver: {e}")
        return None

def scrape_dynamic_content(url, element_selector):
    """
    Scrape dynamic content from a web page using Selenium.
    """
    driver = None
    try:
        driver = setup_selenium_driver()
        driver.get(url)
        # Wait for the dynamic content to load (adjust timeout as needed)
        driver.implicitly_wait(10)
        # Find the target element
        element = driver.find_element(By.CSS_SELECTOR, element_selector)
        content = element.text
        logger.info(f"Successfully scraped dynamic content from {url}")
        return content
    except Exception as e:
        logger.error(f"Error scraping dynamic content from {url}: {e}")
        return None
    finally:
        if driver:
            driver.quit()

def extract_links(soup, base_url):
    """
    Extract all links from a BeautifulSoup object and resolve relative URLs.
    """
    try:
        links = []
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            # Resolve relative URLs
            if href.startswith("/"):
                href = base_url + href
            links.append(href)
        logger.info(f"Extracted {len(links)} links from the page")
        return links
    except Exception as e:
        logger.error(f"Error extracting links: {e}")
        return []

def extract_text(soup):
    """
    Extract all text from a BeautifulSoup object.
    """
    try:
        text = soup.get_text(separator=" ", strip=True)
        logger.info("Text extracted successfully")
        return text
    except Exception as e:
        logger.error(f"Error extracting text: {e}")
        return ""