from document_loader import load_pdf
from text_splitter import split_text
from vector_store import create_vector_store, save_vector_store

text = load_pdf("uploads/An-Introduction-to-Statistical-Learning-with-Applications-in-Python.pdf")

chunks = split_text(text)

db = create_vector_store(chunks)

save_vector_store(db)

print("✅ Vector Database Created Successfully")