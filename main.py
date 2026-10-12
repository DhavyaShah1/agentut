from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
import json
import chromadb
from pypdf import PdfReader
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Smart Study Assistant", page_icon="📚")
st.title("📚 Smart Study Assistant")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

def chunk_text(text, chunk_size=1000, overlap=200):
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks

def extract_text(uploaded_file):
    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    else:
        return uploaded_file.read().decode("utf-8")

def calculate(expression: str) -> str:
    """Evaluates a basic math expression and returns the result."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def search_documents(query: str) -> str:
    """Searches the uploaded document for relevant information."""
    collection = st.session_state.collection
    q_embedding = st.session_state.client.models.embed_content(
        model="gemini-embedding-001", contents=query
    ).embeddings[0].values
    results = collection.query(query_embeddings=[q_embedding], n_results=3)
    return "\n\n".join(results["documents"][0])

st.session_state.setdefault("messages", [])

uploaded_file = st.file_uploader("Upload a document", type=["txt", "md", "pdf"])

if uploaded_file is not None:
    if st.session_state.get("loaded_file") != uploaded_file.name:
        with st.spinner("Reading and embedding your document..."):
            try:
                text = extract_text(uploaded_file)
                chunks = chunk_text(text)

                chroma_client = chromadb.Client()
                try:
                    chroma_client.delete_collection(name="user_doc")
                except Exception:
                    pass
                collection = chroma_client.create_collection(name="user_doc")

                for i, chunk in enumerate(chunks):
                    result = st.session_state.client.models.embed_content(
                        model="gemini-embedding-001", contents=chunk
                    )
                    collection.add(ids=[str(i)], embeddings=[result.embeddings[0].values], documents=[chunk])

                chat = st.session_state.client.chats.create(
                    model="gemini-3.6-flash",
                    config=types.GenerateContentConfig(tools=[calculate, search_documents])
                )

                st.session_state.collection = collection
                st.session_state.loaded_file = uploaded_file.name
                st.session_state.chat = chat
                st.session_state.messages = []

            except Exception as e:
                st.error(f"Setup failed: {e}")
                st.stop()

if "collection" not in st.session_state:
    st.info("👆 Upload a document to get started.")
    st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("tool_used"):
            st.caption(f"Tool used: {msg['tool_used']}")

user_input = st.chat_input("Ask about your document...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = st.session_state.chat.send_message(user_input)

    tool_used = None
    for item in (response.automatic_function_calling_history or []):
        for part in item.parts:
            if part.function_call:
                tool_used = part.function_call.name

    with st.chat_message("assistant"):
        st.markdown(response.text)
        if tool_used:
            st.caption(f"🔧 Tool used: {tool_used}")

    st.session_state.messages.append({
        "role": "assistant", "content": response.text, "tool_used": tool_used
    })