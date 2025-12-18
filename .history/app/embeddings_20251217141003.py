import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

DATA_PATH = "app/data/shl_assessments.json"
INDEX_PATH = "app/data/faiss.index"

_model = None
_index = None
_data = None


# -----------------------------
# Lazy load embedding model
# -----------------------------
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model


# -----------------------------
# Build FAISS index (run once)
# -----------------------------
def build_faiss_index():
    global _index, _data

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        _data = json.load(f)

    texts = [
        item["name"] + " " + item["description"]
        for item in _data
    ]

    model = get_model()
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)   # cosine similarity
    faiss.normalize_L2(embeddings)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    _index = index


# -----------------------------
# Load FAISS index safely
# -----------------------------
def get_faiss_index():
    global _index, _data

    if _index is not None and _data is not None:
        return _index, _data

    # Load data
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        _data = json.load(f)

    # Build index if missing
    if not os.path.exists(INDEX_PATH):
        build_faiss_index()
    else:
        _index = faiss.read_index(INDEX_PATH)

    return _index, _data


# -----------------------------
# Search similar assessments
# -----------------------------
def search_similar(query, top_k=5):
    index, data = get_faiss_index()

    model = get_model()
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    faiss.normalize_L2(query_embedding)

    _, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
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
