# 🤖 AI Personal Assistant

A **Retrieval-Augmented Generation (RAG)** powered AI Assistant built using **LangGraph**, **LangChain**, **Groq Llama 3.3**, **HuggingFace Embeddings**, **FAISS**, and **Streamlit**.

It combines a general-purpose AI chatbot with document-based question answering, allowing users to upload PDF documents and chat with their contents using semantic search.

---

## ✨ Features

- 💬 General AI Chat
- 📄 Chat with PDF Documents
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using FAISS
- 🤗 HuggingFace Embeddings
- ⚡ Groq Llama 3.3 Integration
- 🧵 Conversation Memory using LangGraph
- 🔄 Hybrid Routing
  - Uses RAG for document questions
  - Falls back to general AI chat when needed
- 📥 Download Chat History
- 🆕 New Chat & Clear Chat
- 🎨 Interactive Streamlit UI

---

## 🏗️ Project Structure

```text
AI-Personal-Assistant/
│
├── app.py
├── chatbot.py
├── config.py
├── graph.py
├── llm.py
│
├── rag/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag.py
│
├── tests/
├── assets/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| LLM | Groq Llama 3.3 |
| Framework | LangGraph |
| Framework | LangChain |
| Embeddings | HuggingFace MiniLM |
| Vector Database | FAISS |
| Language | Python |

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/radcodezz/AI-Personal-Assistant.git
```

Move into the project

```bash
cd AI-Personal-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in a FAISS vector database.
6. Retrieve relevant chunks using semantic similarity.
7. Send retrieved context to Groq Llama.
8. Generate an accurate answer.
9. Fall back to the general chatbot if no relevant context is found.

---

## 🎯 Future Improvements

- Support multiple PDFs
- Source citations
- Chat history persistence
- Image & table understanding
- Authentication
- Cloud vector databases

---

## 👨‍💻 Author

**Radhey Shyam Sharma**

M.Sc. Statistics & Computing  
Banaras Hindu University

---

## 📜 License

This project is licensed under the MIT License.