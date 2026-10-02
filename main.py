from google import genai 
import os 
from dotenv import load_getenv 

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

for i,chunks in enumerate(chunks):
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

def ask(question,top_k):
    q_embedding = genai.client.get_embeddings(
        model = "gemini-embeddings-001",
        content = question
    )
    result = collections.query(
        query_embeddings=q_embedding,
        n_results = top_k
    )
    retrieved_chunks = result['documents'][0]
    context="n\n".join(retrieved_chunks)

    prompt = f"answer the following question{question} strictly using the following context{context}"
    return genai.client.generate_content(
        models = "gemini-flash-3.6",
        contents = prompt
    ).text



        