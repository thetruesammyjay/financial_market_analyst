# Financial Market Analyst

---

## Overview
The Financial Market Analyst is a tool that aggregates real-time financial news, company reports, and SEC filings to provide actionable market insights. It uses web scraping, vector databases, Retrieval-Augmented Generation (RAG), and task automation to deliver context-aware insights.

---

## Features
- **Real-Time Data Aggregation**: Scrapes financial news, company reports, and SEC filings.
- **Context-Aware Insights**: Uses RAG to generate insights based on retrieved documents.
- **Task Automation**: Automates repetitive tasks like data collection and report generation using CREWAI.
- **User-Friendly Interface**: Provides a simple web interface for querying and insights generation.

---

## Tech Stack
- **Web Scraping**: BeautifulSoup, Selenium
- **Vector Database**: Pinecone/FAISS
- **RAG**: Hugging Face Transformers
- **Task Automation**: CREWAI
- **Frontend**: Streamlit
- **Backend**: Python (Flask/FastAPI optional)

---

## Setup

### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Configuration
1. Add API keys to **config/api_keys.yaml**.
2. Configure CREWAI tasks in **config/crewai_tasks.yaml**.

### Running the Application
1. Start the Streamlit app:
    ```bash
    streamlit run app/app.py
    ```
2. Open the app in your browser at http://localhost:8501.

### Running Tests
- Run unit and integration tests:
    ```bash
    python -m unittest tests/test_rag.py
    python -m unittest tests/test_preprocessing.py
    ```

---

## File Structure
```markdown
financial_market_analyst/
├── data/
├── scripts/
├── models/
├── config/
├── pipelines/
├── utils/
├── app/
├── logs/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```
