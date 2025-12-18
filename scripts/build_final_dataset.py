import json

INPUT_FILE = "shl_raw_links.json"
OUTPUT_FILE = "app/data/shl_assessments.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

final_data = []

for item in raw_data:
    name_lower = item["name"].lower()

    if any(k in name_lower for k in ["personality", "behaviour", "behavior", "360"]):
        test_type = ["Personality & Behaviour"]
    else:
        test_type = ["Knowledge & Skills"]

    final_data.append({
        "name": item["name"],
        "url": item["url"],
        "description": f"SHL assessment designed to evaluate competencies related to {item['name']}.",
        "test_type": test_type,
        "duration": 20,
        "adaptive_support": "No",
        "remote_support": "Yes"
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=2)

print("✅ Final dataset saved successfully")
print("Total assessments:", len(final_data))
