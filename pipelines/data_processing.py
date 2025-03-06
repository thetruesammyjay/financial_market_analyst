import re
from bs4 import BeautifulSoup
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("preprocess_data")

def clean_text(text):
    """
    Clean raw text by removing HTML tags, special characters, and extra spaces.
    """
    try:
        # Remove HTML tags
        text = BeautifulSoup(text, "html.parser").get_text()
        # Remove special characters and extra spaces
        text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        logger.info("Text cleaned successfully")
        return text
    except Exception as e:
        logger.error(f"Error cleaning text: {e}")
        raise

def preprocess_data(raw_data):
    """
    Preprocess raw data (e.g., clean text, tokenize).
    """
    try:
        processed_data = []
        for item in raw_data:
            cleaned_text = clean_text(item["text"])
            processed_data.append({"id": item["id"], "text": cleaned_text})
        logger.info(f"Preprocessed {len(processed_data)} items")
        return processed_data
    except Exception as e:
        logger.error(f"Error preprocessing data: {e}")
        raise

if __name__ == "__main__":
    # Example raw data (replace with actual scraped data)
    raw_data = [
        {"id": 1, "text": "<p>Apple Inc. reported <strong>record earnings</strong> for Q4 2023.</p>"},
        {"id": 2, "text": "The Federal Reserve announced an interest rate hike."},
        {"id": 3, "text": "Tesla unveiled its new <em>electric vehicle</em> model."}
    ]

    # Preprocess the data
    processed_data = preprocess_data(raw_data)
    print(processed_data)