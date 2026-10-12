# 📚 Smart Study Assistant

An **agentic RAG application** — upload any document (PDF / TXT / MD) and ask questions about it in natural language. Unlike a plain chatbot, this assistant can *decide on its own* when to search your document versus when to just do math, and it shows you exactly which tool it used for every answer.

**🔗 Live demo:** [agentut-dhavyaproject.streamlit.app](https://agentut-dhavyaproject.streamlit.app/)

---

## Why this project

Most "chat with your PDF" tutorials stop at basic RAG (retrieve chunks → stuff into a prompt → generate). This project goes one step further into **agentic AI**: the LLM is given tools and *decides for itself* which one to call, instead of a human hardcoding "always retrieve, then answer." That tool-use/function-calling pattern is the part of the 2025–26 AI engineering stack that separates a tutorial project from a portfolio project.

Built end-to-end from scratch while learning — no boilerplate templates — to understand the *mechanics* of RAG and agents, not just the library syntax.

## Features

- 📄 **Document upload** — accepts `.txt`, `.md`, and `.pdf` files
- 🔍 **Retrieval-Augmented Generation** — documents are chunked, embedded, and stored in a vector database; answers are grounded in the retrieved content to reduce hallucination
- 🤖 **Agentic tool use** — the model has two tools (`search_documents` and `calculate`) and decides on its own, per question, which (if either) to call
- 🪪 **Tool-use transparency** — every assistant reply shows a caption naming which tool fired, so you can see the agent's reasoning instead of a black box
- 💬 **Conversational interface** — built with Streamlit's chat UI, with session-aware state so switching documents resets the conversation cleanly

## How it works

```
Upload document
      │
      ▼
Split into overlapping chunks → embed each chunk (Gemini embeddings) → store in ChromaDB
      │
      ▼
User asks a question
      │
      ▼
Gemini model receives the question + 2 available tools
      │
      ├── decides to call search_documents() ──▶ embeds query → retrieves top-matching
      │                                           chunks from ChromaDB → returns as context
      │
      └── decides to call calculate() ──▶ evaluates a math expression
      │
      ▼
Model generates a grounded, final answer using whatever the tool(s) returned
```

## Tech stack

| Layer | Choice |
|---|---|
| LLM | Google Gemini (`gemini-3.6-flash`) via the `google-genai` SDK |
| Embeddings | `gemini-embedding-001` |
| Vector store | ChromaDB (in-memory, local) |
| PDF parsing | `pypdf` |
| UI | Streamlit |
| Secrets | `.env` + `python-dotenv` |

## Running it locally

```bash
# 1. Clone the repo
git clone https://github.com/DhavyaShah1/agentut.git
cd agentut

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Run the app
streamlit run main.py
```

Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com/) — no credit card required.

## Project structure

```
agentut/
├── main.py              # Streamlit app: UI, RAG pipeline, agent loop
├── requirements.txt      # Python dependencies
├── Roadmap.md            # Learning roadmap this project was built from
└── .devcontainer/        # Dev container config
```

## What I learned building this

- How embeddings turn text into vectors where semantic similarity = numerical closeness
- The full RAG pipeline: chunking strategy, why overlap matters, retrieval, and *grounding* the prompt to reduce hallucination
- The **agent loop**: the LLM never executes code itself — it requests a function call, your code runs it, and the result is fed back in; this request → execute → return cycle is the core mechanic behind every "AI agent"
- The difference between built-in tools (e.g. Google Search grounding, which runs on Google's servers) and custom function tools (which run as local Python functions)
- Practical constraints of working with free-tier LLM APIs (rate limits, retry/backoff handling)

## Possible next steps

- Persist chat history across sessions (currently resets per app restart)
- Support multiple documents / a persistent vector store instead of in-memory
- Add streaming responses
- Deploy with a more production-grade backend (FastAPI) in front of the model calls

---

*Built as a hands-on project to learn RAG and agentic AI from first principles.*
