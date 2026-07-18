from rag.retriever import retrieve_chunks
from llm import llm


def ask_pdf(question):

    docs = retrieve_chunks(question)

    if len(docs) == 0:
        return None

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the context below.

If the context does not contain enough information,
reply ONLY with:

NOT_FOUND

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    answer = response.content.strip()

    if answer == "NOT_FOUND":
        return None

    return answer
