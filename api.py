from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Karun AI Coding Mentor API Running"}

@app.post("/ask")
def ask_ai(data: Question):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": data.prompt,
            "stream": False
        }
    )

    return {
        "response": response.json()["response"]
    }