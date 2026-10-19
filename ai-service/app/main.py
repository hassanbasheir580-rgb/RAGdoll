from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "RAGdoll AI service is not running"}