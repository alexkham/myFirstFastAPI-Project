#Fast API is awesome
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"view":"home"}


@app.get("/ask")
def ask():
    return {"question":"who are you?"}


@app.get("/add/{x}/{y}")
def add(x,y):
    result=float(x)+float(y)
    
    return {"result":str(result)}

@app.get("/multiply")
def multiply(x,y):
    result=float(x)*float(y)
    
    return {"result":str(result)}