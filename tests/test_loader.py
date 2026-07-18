from document_loader import load_pdf

text = load_pdf("uploads/An-Introduction-to-Statistical-Learning-with-Applications-in-Python.pdf")

print(text[:3000])