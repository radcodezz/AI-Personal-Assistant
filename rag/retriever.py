from rag.vector_store import load_vector_store


def retrieve_chunks(query, k=3):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search_with_score(
        query=query,
        k=k
    )

    filtered_docs = []

    for doc, score in docs:

        # smaller score = more similar

        if score < 1.2:
            filtered_docs.append(doc)

    return filtered_docs
