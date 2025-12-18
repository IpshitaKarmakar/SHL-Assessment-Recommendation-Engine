from app.embeddings import search_similar

def recommend_assessments(query, top_k=10):
    candidates = search_similar(query, top_k=20)

    tech, behavior = [], []
    for c in candidates:
        types = [t.lower() for t in c.get("test_type", [])]
        if "knowledge" in types:
            tech.append(c)
        elif "personality" in types:
            behavior.append(c)
        else:
            tech.append(c)

    result = tech[:int(top_k*0.6)] + behavior[:top_k]
    return result[:top_k]