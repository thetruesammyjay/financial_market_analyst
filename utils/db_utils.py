import pinecone

def init_pinecone():
    with open("config/api_keys.yaml", "r") as f:
        config = yaml.safe_load(f)
    pinecone.init(api_key=config["pinecone"]["api_key"], environment=config["pinecone"]["environment"])

def upsert_embeddings(index_name, embeddings):
    index = pinecone.Index(index_name)
    index.upsert(embeddings)