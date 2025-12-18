#print("Evaluation placeholder")
import requests

API_URL = "http://127.0.0.1:8000/recommend"

# Test queries with expected keywords (pseudo ground truth)
EVAL_DATA = [
    {
        "query": "Python backend developer",
        "keywords": ["python"]
    },
    {
        "query": "Java software engineer",
        "keywords": ["java"]
    },
    {
        "query": "Candidate with teamwork and leadership skills",
        "keywords": ["personality", "team", "leadership"]
    },
    {
        "query": "Data analyst with SQL skills",
        "keywords": ["data", "sql"]
    },
    {
        "query": "Frontend developer with React",
        "keywords": ["frontend", "javascript", "react"]
    }
]

TOP_K = 10


def is_relevant(assessment, keywords):
    text = (assessment["name"] + " " + assessment["description"]).lower()
    return any(k in text for k in keywords)


def evaluate():
    hits = 0

    for item in EVAL_DATA:
        response = requests.post(
            API_URL,
            json={"query": item["query"]}
        ).json()

        recommendations = response["recommended_assessments"][:TOP_K]

        found = any(
            is_relevant(rec, item["keywords"])
            for rec in recommendations
        )

        if found:
            hits += 1

        print(f"Query: {item['query']}")
        print("Relevant found:", found)
        print("-" * 50)

    recall_at_10 = hits / len(EVAL_DATA)

    print("\n📊 Evaluation Result")
    print(f"Recall@10: {recall_at_10:.2f}")


if __name__ == "__main__":
    evaluate()
