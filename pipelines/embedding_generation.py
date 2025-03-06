import yaml
from sentence_transformers import SentenceTransformer
from utils.db_utils import init_pinecone, upsert_embeddings
from utils.helpers import setup_logger

# Set up logger
logger = setup_logger("generate_embeddings")

def load_embedding_model():
    """
    Load the embedding model.
    """
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        logger.info("Embedding model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Error loading embedding model: {e}")
        raise

def generate_and_store_embeddings(data, model, index_name):
    """
    Generate embeddings for the data and store them in the vector database.
    """
    try:
        # Generate embeddings
        embeddings = model.encode(data)
        # Prepare embeddings for upsert
        embeddings_list = [(f"doc_{i}", embedding) for i, embedding in enumerate(embeddings)]
        # Upsert embeddings into Pinecone
        upsert_embeddings(index_name, embeddings_list)
        logger.info(f"Generated and stored {len(embeddings_list)} embeddings in {index_name}")
    except Exception as e:
        logger.error(f"Error generating or storing embeddings: {e}")
        raise

if __name__ == "__main__":
    # Initialize Pinecone
    init_pinecone()

    # Load the embedding model
    model = load_embedding_model()

    # Example data (replace with actual processed data)
    data = [
        "Apple Inc. reported record earnings for Q4 2023.",
        "The Federal Reserve announced an interest rate hike.",
        "Tesla unveiled its new electric vehicle model."
    ]

    # Generate and store embeddings
    index_name = "financial-data"
    generate_and_store_embeddings(data, model, index_name)