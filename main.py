from google import genai 
import os 
from dotenv import load_getenv 
from google.genai import types 

load_getenv()
client = genai.client(api_key=os.getenv("GEMINI_API_KEY"))

with open ("doc.md","r",encoding="utf-8") as f: text = f.read() # reading/loading the doc

def get_chunks(text,chunk_size=1000, overlap=200): # converting the doc into chunks 
    chunks=[]
    start = 0
    while(start<len(text)):
        end=start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap # or you can also do start+= chunk_size - overlap 
    return chunks 

import chromadb # setting up chromadb and making a collection 
chroma_client=chromadb.Client()
collections = chromadb.Client.create_collections(name = "roadmap")

chunks = get_chunks

for i,chunks in enumerate(chunks):      # converting chunks to embeddings 
    result = genai.client.get_embeddings(
        models = "gemini-embedding-001",
        content = chunks 
    )
    embedding = result.embeddings[0].values
    collections.add(
        id=str[i],
        embeddings = embedding,
        documents=[chunks]
    )

def search_documents(query:str)->str:  # RAG 
    """Searches the user's personal career roadmap document and returns the most relevant excerpts.
    Use this whenever the question is about the user's roadmap, projects, study plan, or career strategy.

    Args:
        query: The search query, based on what the user wants to know.
    """
    q_embedding = genai.client.get_embeddings(
        model = "gemini-embeddings-001",
        content = query
    )
    result = collections.query(
        query_embeddings=q_embedding,
        n_results = 3
    )
    retrieved_chunks = result['documents'][0]
    context="n\n".join(retrieved_chunks)
    distances = result["distances"][0]


    print(f"[search_documents called] query='{query}'")
    for dist, chunk in zip(distances, retrieved_chunks):
        print(f"  distance={dist:.4f} | preview: {chunk[:100]}...")
    print()

def calculate(expression:str)->str:
    """Evaluates a basic math expression like '12 * 4' and returns the result.

    Args:
        expression: A math expression as a string, e.g. '12 * 4'
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def google_search():
    google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
) 








        