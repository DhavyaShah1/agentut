from google import genai 
import os 
from dotenv import load_dotenv 
from google.genai import types 
import json
import chromadb

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open ("Roadmap.md","r",encoding="utf-8") as f: text = f.read() # reading/loading the doc

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
collection = chroma_client.create_collection(name = "roadmap")

chunks = get_chunks(text)

for i,chunks in enumerate(chunks):      # converting chunks to embeddings 
    result = client.models.embed_content(
        model = "gemini-embedding-001",
        contents = chunks 
    )
    embedding = result.embeddings[0].values
    collection.add(
        ids=[str(i)],
        embeddings = embedding,
        documents=[chunks]
    )

def search_documents(query: str) -> str:
    """Searches the user's personal career roadmap document and returns the most relevant excerpts.
    Use this whenever the question is about the user's roadmap, projects, study plan, or career strategy.

    Args:
        query: The search query, based on what the user wants to know.
    """
    try:
        q_embedding = client.models.embed_content(
            model="gemini-embedding-001",
            contents=query
        ).embeddings[0].values

        result = collection.query(
            query_embeddings=[q_embedding],
            n_results=3
        )
        retrieved_chunks = result["documents"][0]
        distances = result["distances"][0]

        print(f"[search_documents called] query='{query}'")
        for dist, chunk in zip(distances, retrieved_chunks):
            print(f"  distance={dist:.4f} | preview: {chunk[:100]}...")
        print()

        return "\n\n".join(retrieved_chunks)
    except Exception as e:
        return f"Error: {e}"
    
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


HISTORY_FILE = "chat_history.json"

def save_history(chat):
    history = chat.get_history()
    data = [
        {"role": msg.role, "text": msg.parts[0].text}
        for msg in history
    ]
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE) as f:
        data = json.load(f)
    return [
        types.Content(role=item["role"], parts=[types.Part(text=item["text"])])
        for item in data
    ]
chat = client.chats.create(
    model="gemini-3.6-flash",
    history=load_history(),
    config={"tools": [search_documents, calculate, google_search]}
)
r1 = chat.send_message("What projects should I build according to my roadmap?")
print("Answer 1:", r1.text, "\n")

r2 = chat.send_message("What is 45 * 12?")
print("Answer 2:", r2.text, "\n")

r3 = chat.send_message("Who created you?")
print("Answer 3:", r3.text, "\n") 

r4 = chat.send_message("What has trump said today?")
print("Answer 4:", r4.text, "\n") 
r5= chat.send_message("According to my roadmap, what's my cumulative applications target for the end of the month? Multiply that number by 3.")
print("Answer 5:", r5.text, "\n")






        