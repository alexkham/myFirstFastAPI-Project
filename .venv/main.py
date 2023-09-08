#Fast API is awesome
from fastapi import FastAPI
import app


app=FastAPI()

@app.get("/")
def home():
    return {"view":"home"}


@app.get("/ask")
def ask():
    return {"question":"who are you?"}

@app.get("/ask-next")
def ask_next():
    return {"question":"who are you  NEXT?"}

@app.get("/ask-next2")
def ask_next2():
    return {"question":"who are you  NEXT-2?"}


@app.get("/add/{x}/{y}")
def add(x,y):
    result=float(x)+float(y)
    
    return {"result":str(result)}

@app.get("/multiply")
def multiply(x,y):
    result=float(x)*float(y)
    
    return {"result":str(result)}

