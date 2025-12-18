import csv
import requests

API_URL = "http://127.0.0.1:8000/recommend"

queries = [
    "Python backend developer",
    "Java software engineer",
    "Candidate with leadership and teamwork skills",
    "Data analyst with SQL and Python",
    "Frontend developer with React experience"
]

with open("submission.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["query", "assessment_url", "rank"])

    for query in queries:
        response = requests.post(API_URL, json={"query": query}).json()
        results = response["recommended_assessments"]

        for rank, item in enumerate(results, start=1):
            writer.writerow([query, item["url"], rank])

print("✅ submission.csv created")
