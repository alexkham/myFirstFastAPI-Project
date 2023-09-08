#Fast API is awesome
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"view":"home"}


@app.get("/ask")
def ask():
    return {"question":"who are you?"}
