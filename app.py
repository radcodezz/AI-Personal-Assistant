import os
import shutil

import streamlit as st
from langchain_core.messages import HumanMessage
from graph import app_graph

from rag.document_loader import load_pdf
from rag.text_splitter import split_text
from rag.vector_store import create_vector_store, save_vector_store

from rag import ask_pdf

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🤖 AI Assistant")
st.sidebar.caption("Powered by LangGraph + Groq")

st.sidebar.markdown("## 📄 Document")

# ---------------- PDF Upload ---------------- #

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"],
    help="Upload a PDF to chat with its contents."
)

if uploaded_file is not None:

    # Only process if a different file is selected
    if (
        st.session_state.pdf_path is None
        or os.path.basename(st.session_state.pdf_path) != uploaded_file.name
    ):

        os.makedirs("uploads", exist_ok=True)

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)

        st.session_state.pdf_uploaded = True
        st.session_state.pdf_processed = False
        st.session_state.pdf_path = save_path

if st.session_state.pdf_uploaded:

    st.sidebar.markdown("---")

    st.sidebar.markdown("### 📄 Current Document")

    st.sidebar.info(
        os.path.basename(st.session_state.pdf_path)
    )

    if st.session_state.pdf_processed:

        st.sidebar.success("🟢 Ready for Questions")

    else:

        st.sidebar.warning("🟡 Not Processed")

        if st.sidebar.button(
            "⚙️ Process PDF",
            use_container_width=True
        ):

            with st.spinner("📄 Processing PDF..."):

                text = load_pdf(
                    st.session_state.pdf_path
                )

                chunks = split_text(text)

                vector_db = create_vector_store(chunks)

                save_vector_store(vector_db)

            st.session_state.pdf_processed = True

            st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("## 💬 Chat")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "1"

if "messages" not in st.session_state:
    st.session_state.messages = []

# New Chat
if st.sidebar.button("🆕 New Chat", use_container_width=True):
    st.session_state.messages = []
    st.session_state.thread_id = str(int(st.session_state.thread_id) + 1)
    st.rerun()

# Clear Chat
if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

# Download Chat
chat_text = ""

for msg in st.session_state.messages:
    role = "You" if msg["role"] == "user" else "Assistant"
    chat_text += f"{role}: {msg['content']}\n\n"

st.sidebar.download_button(
    label="📥 Download Chat",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain",
    use_container_width=True,
)

st.sidebar.markdown("---")
st.sidebar.markdown("## ℹ️ About")






st.sidebar.info(
"""
### AI Personal Assistant

**Tech Stack**

- 🧠 LangGraph
- 🔗 LangChain
- ⚡ Groq Llama 3.3
- 📚 FAISS
- 🤗 HuggingFace Embeddings
- 🎨 Streamlit

Made with ❤️ by **Radhey**

Version 1.0
"""
)

# ---------------- Main ---------------- #

st.title("🤖 AI Personal Assistant")
st.caption("General AI Chat + Retrieval-Augmented Generation (RAG)")


# ---------------- Active Document ---------------- #

if st.session_state.pdf_uploaded:

    if st.session_state.pdf_processed:

        st.success(
            f"📄 Active Document: **{os.path.basename(st.session_state.pdf_path)}**"
        )

    else:

        st.warning(
            f"📄 **{os.path.basename(st.session_state.pdf_path)}** uploaded. Click **Process PDF** to start asking questions."
        )

st.markdown("---")

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

# Show Previous Messages
for msg in st.session_state.messages:

    avatar = "👨" if msg["role"] == "user" else "🤖"

    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Chat Input
if st.session_state.pdf_processed:

    prompt = st.chat_input(
        "Ask about your PDF or anything else..."
    )

else:

    prompt = st.chat_input(
        "Ask me anything..."
    )

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user", avatar="👨"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("🤖 Thinking..."):

            try:

                answer = None

                if st.session_state.pdf_processed:

                    answer = ask_pdf(prompt)

                if answer is None:

                    result = app_graph.invoke(
                        {
                            "messages": [
                                HumanMessage(content=prompt)
                            ]
                        },
                        config=config
                    )

                    answer = result["messages"][-1].content

            except Exception as e:

                answer = str(e)

            st.markdown(answer)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

st.markdown("---")

st.caption(
    "🚀 Built with LangGraph • LangChain • Groq • Streamlit"
)