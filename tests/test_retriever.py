from retriever import retrieve_chunks

query = input("Ask a question: ")

results = retrieve_chunks(query)

print("\nTop Retrieved Chunks\n")

for i, doc in enumerate(results):

    print("=" * 70)
    print(f"Chunk {i+1}\n")

    print(doc.page_content)
    print()