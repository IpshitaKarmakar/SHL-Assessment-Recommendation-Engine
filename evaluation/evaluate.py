import csv
import json
import requests

API_URL = "http://127.0.0.1:8000/recommend"
DATASET_FILE = "app/data/shl_assessments.json"

# Load all assessment names from JSON
with open(DATASET_FILE, "r", encoding="utf-8") as f:
    assessments = json.load(f)

queries = [item["name"] for item in assessments]

with open("submission.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["query", "assessment_url", "rank"])

    for query in queries:
        response = requests.post(
            API_URL,
            json={"query": query}
        ).json()

        results = response["recommended_assessments"]

        for rank, item in enumerate(results, start=1):
            writer.writerow([query, item["url"], rank])

print("✅ submission.csv created successfully")
print("Total queries processed:", len(queries))
