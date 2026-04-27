from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Body, Query
from ollama import Client
from rag.queues.worker import  process_query
from rag.client.rq_client import get_queue


app = FastAPI()
client = Client(
    host="http://localhost:11434"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/chat")
# def chat(message: str = Body(..., description="The message")):
#     response = client.chat(model="gemma2:2b", messages=[
#         {"role":"user","content":message}
#     ])
#     return {"response":response.message.content}

@app.post('/chat')
async def chat(query:str =  Query(..., description="The chat query of users")):
    job = get_queue().enqueue(process_query, query)
    return {"status":"queued","job_id":job.id}
