import streamlit as st
from scripts.rag_pipeline import load_rag_model, generate_insights
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("app")

# Page title and description
st.set_page_config(page_title="Financial Market Analyst", page_icon="📈")
st.title("Financial Market Analyst")
st.write("""
This application aggregates real-time financial news, company reports, and SEC filings to provide actionable market insights.
Enter your query below to get started.
""")

# Load the RAG model
@st.cache_resource
def load_model():
    try:
        tokenizer, retriever, model = load_rag_model()
        logger.info("RAG model loaded successfully")
        return tokenizer, model
    except Exception as e:
        logger.error(f"Error loading RAG model: {e}")
        st.error("Failed to load the RAG model. Please check the logs.")
        return None, None

tokenizer, model = load_model()

# User input
query = st.text_input("Enter your query:", placeholder="e.g., What are the key risks for Apple in 2023?")

# Generate insights
if query:
    if tokenizer and model:
        with st.spinner("Generating insights..."):
            try:
                insights = generate_insights(query, tokenizer, model)
                st.success("Insights generated successfully!")
                st.write(insights)
            except Exception as e:
                logger.error(f"Error generating insights: {e}")
                st.error("An error occurred while generating insights. Please try again.")
    else:
        st.error("The RAG model is not loaded. Please check the logs.")