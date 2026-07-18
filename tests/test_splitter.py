from document_loader import load_pdf
from text_splitter import split_text

text = load_pdf("uploads/An-Introduction-to-Statistical-Learning-with-Applications-in-Python.pdf")

chunks = split_text(text)

print(f"Total Chunks : {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])