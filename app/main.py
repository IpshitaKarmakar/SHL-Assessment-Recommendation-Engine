from fastapi import FastAPI
from app.recommender import recommend_assessments

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(payload: dict):
    query = payload.get("query", "")
    return {"recommended_assessments": recommend_assessments(query)}