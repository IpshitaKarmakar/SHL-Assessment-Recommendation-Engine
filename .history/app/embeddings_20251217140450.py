import json
from sentence_transformers import SentenceTransformer
import numpy as np

DATA_PATH = "app/data/shl_assessments.json"

# Lazy-loaded model (VERY IMPORTANT)
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model


def search_similar(query, top_k=5):
    # Load data
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Prepare texts
    texts = [
        item["name"] + " " + item["description"]
        for item in data
    ]

    model = get_model()

    # Encode documents and query
    doc_embeddings = model.encode(texts)
    query_embedding = model.encode([query])[0]

    # Compute cosine similarity manually
    scores = []
    for idx, emb in enumerate(doc_embeddings):
        score = np.dot(query_embedding, emb) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(emb)
        )
        scores.append((score, idx))

    # Sort by similarity
    scores.sort(reverse=True)

    results = []
    for _, idx in scores[:top_k]:
        item = data[idx]
        results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item["description"],
            "duration": item.get("duration", 30),
            "adaptive_support": item.get("adaptive_support", "Yes"),
            "remote_support": item.get("remote_support", "Yes"),
            "test_type": item.get("test_type", [])
        })

    return results
