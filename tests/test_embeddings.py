from document_loader import load_pdf
from text_splitter import split_text
from embeddings import create_embeddings

text = load_pdf("uploads/An-Introduction-to-Statistical-Learning-with-Applications-in-Python.pdf")

chunks = split_text(text)

vectors = create_embeddings(chunks[:5])

print("Number of vectors :", len(vectors))

print("Dimension :", len(vectors[0]))

print("\nFirst 10 values of first vector:\n")

print(vectors[0][:10])