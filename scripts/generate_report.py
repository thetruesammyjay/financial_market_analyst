from pipelines.rag_inference import generate_insights
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("generate_report")

def generate_market_report(query):
    try:
        insights = generate_insights(query)
        logger.info(f"Generated insights for query: {query}")
        return insights
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        return None

if __name__ == "__main__":
    query = "What are the key risks for Apple in 2023?"
    report = generate_market_report(query)
    print(report)