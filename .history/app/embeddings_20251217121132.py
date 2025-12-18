import json, os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_PATH = "app/data/shl_assessments.json"
INDEX_PATH = "app/data/faiss.index"

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model

def build_index():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [
        d["name"] + " " + d["description"] + " " + " ".join(d["test_type"])
        for d in data
    ]

    model = get_model()
    emb = model.encode(texts)
    emb = np.array(emb).astype("float32")

    index = faiss.IndexFlatL2(emb.shape[1])
    index.add(emb)
    faiss.write_index(index, INDEX_PATH)

def search_similar(query, top_k=10):
    if not os.path.exists(INDEX_PATH):
        build_index()

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    index = faiss.read_index(INDEX_PATH)
    model = get_model()

    q_emb = model.encode([query])
    q_emb = np.array(q_emb).astype("float32")

    _, I = index.search(q_emb, top_k)
    return [data[i] for i in I[0]]