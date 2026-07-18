import os
import shutil

from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model


def create_vector_store(chunks):
    """
    Create FAISS vector database.
    """

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store):
    """
    Save FAISS vector database.
    """

    if os.path.exists("vector_db"):
        shutil.rmtree("vector_db")

    vector_store.save_local("vector_db")


def load_vector_store():
    """
    Load saved FAISS vector database.
    """

    return FAISS.load_local(
        "vector_db",
        embedding_model,
        allow_dangerous_deserialization=True
    )
