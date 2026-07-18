from langchain_huggingface import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_embeddings(texts):
    """
    Convert list of text chunks into embeddings.
    """

    embeddings = embedding_model.embed_documents(texts)

    return embeddings


def embed_query(query):
    """
    Convert user query into embedding.
    """

    return embedding_model.embed_query(query)