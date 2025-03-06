import yaml
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("rag_pipeline")

def load_rag_model():
    """
    Load the RAG model, tokenizer, and retriever.
    """
    try:
        tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
        retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="custom")
        model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)
        logger.info("RAG model loaded successfully")
        return tokenizer, retriever, model
    except Exception as e:
        logger.error(f"Error loading RAG model: {e}")
        raise

def generate_insights(query, tokenizer, model):
    """
    Generate insights using the RAG model.
    """
    try:
        input_ids = tokenizer(query, return_tensors="pt").input_ids
        generated = model.generate(input_ids)
        insights = tokenizer.decode(generated[0], skip_special_tokens=True)
        logger.info(f"Generated insights for query: {query}")
        return insights
    except Exception as e:
        logger.error(f"Error generating insights: {e}")
        return None

if __name__ == "__main__":
    # Load the RAG model
    tokenizer, retriever, model = load_rag_model()

    # Example query
    query = "What are the key risks for Apple in 2023?"
    insights = generate_insights(query, tokenizer, model)
    print(insights)