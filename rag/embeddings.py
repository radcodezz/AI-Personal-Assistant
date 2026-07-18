from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


class LocalEmbeddings:
    """
    Wrapper class so FAISS/LangChain can use SentenceTransformer.
    """

    def embed_documents(self, texts):

        return model.encode(
            texts,
            convert_to_numpy=False
        ).tolist()

    def embed_query(self, query):

        return model.encode(
            query,
            convert_to_numpy=False
        ).tolist()


embedding_model = LocalEmbeddings()


def create_embeddings(texts):

    return embedding_model.embed_documents(texts)


def embed_query(query):

    return embedding_model.embed_query(query)