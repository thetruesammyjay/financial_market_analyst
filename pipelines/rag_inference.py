from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("rag_inference")

def generate_insights(query):
    try:
        tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
        retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="custom")
        model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)
        input_ids = tokenizer(query, return_tensors="pt").input_ids
        generated = model.generate(input_ids)
        insights = tokenizer.decode(generated[0], skip_special_tokens=True)
        logger.info(f"Generated insights for query: {query}")
        return insights
    except Exception as e:
        logger.error(f"Error generating insights: {e}")
        return None