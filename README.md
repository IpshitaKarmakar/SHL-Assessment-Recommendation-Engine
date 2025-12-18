Candidate: Ipshita Karmakar 
Repository: SHL-Assessment-Recommendation-Engine

1. Objective of the Assignment
The objective of this project is to build an Assessment Recommendation Engine that recommends relevant SHL assessments for a given hiring requirement or job description.
The system should:
Understand free-text hiring queries
Retrieve relevant assessments from the SHL product catalogue
Rank them meaningfully
Be scalable, reproducible, and easy to evaluate

2. Why This Approach Was Chosen
Among the two options provided by SHL, I selected Option 1: Assessment Recommendation Engine because it aligns closely with:
SHL’s core assessment and talent analytics domain
Real-world recommendation system problems
Research challenges in semantic similarity, ranking, and evaluation
This approach allows demonstrating both research thinking and practical system design, which are critical for an AI Research Intern role.

3. High-Level System Overview
The system is built as a semantic retrieval pipeline with the following stages:
Data Collection & Preparation
Metadata Enrichment
Text Embedding
Vector Indexing (FAISS)
Recommendation API (FastAPI)
Evaluation & Submission Generation
Each stage is modular and independently reproducible.

4. Step-by-Step Implementation
4.1 Data Collection
Assessment names and URLs were collected from the public SHL product catalogue.
Due to pagination and intermittent server-side rate limiting, a seed set of real SHL assessments was extracted.
The final dataset contains 377 assessment entries, sufficient to evaluate scalability and retrieval quality.
Raw data file:
shl_raw_links.json
Each entry contains:

{
  "name": "Python (New)",
  "url": "https://www.shl.com/products/product-catalog/view/python-new/"
}

4.2 Data Enrichment
The raw data is programmatically enriched to ensure consistency and usability.
For each assessment:
A short description is generated
Test type is inferred (Knowledge & Skills / Personality & Behaviour)
Duration and delivery flags are added
Final dataset file:
app/data/shl_assessments.json
Each enriched entry contains:
name
url
description
test_type
duration
adaptive_support
remote_support
This enrichment ensures the dataset is structured, consistent, and reproducible.

4.3 Text Embedding
To move beyond keyword-based matching:
Both assessment descriptions and user queries are converted into dense vector embeddings
Sentence Transformers are used to capture semantic meaning
This enables the system to match:
“Python backend developer”
even if exact keywords differ.

4.4 Vector Indexing with FAISS
To support fast and scalable retrieval:
All assessment embeddings are indexed using FAISS
The index is built once and reused for all queries
Nearest-neighbor search retrieves the most relevant assessments efficiently
FAISS allows the system to scale to large catalog sizes with low latency.

4.5 Recommendation API (FastAPI)
The system exposes a REST API using FastAPI.
Health Endpoint
GET /health

Response:

{
  "status": "healthy"
}

Recommendation Endpoint
POST /recommend

Request:

{
  "query": "Python backend developer"
}


Response:

{
  "recommended_assessments": [
    {
      "name": "Python (New)",
      "url": "...",
      "description": "...",
      "test_type": ["Knowledge & Skills"],
      "duration": 20,
      "adaptive_support": "No",
      "remote_support": "Yes"
    }
  ]
}
The API is designed to be: Simple, Extensible and Easy to integrate into downstream systems

5. Evaluation Methodology
5.1 Metric Used: Recall@10
The system is evaluated using Recall@10, a standard metric for recommendation systems.
5.2 Evaluation Process
A set of representative hiring queries is defined
The top-10 recommendations are retrieved for each query
A query is considered successful if at least one relevant assessment appears in the top-10
5.3 Metric Formula
Recall@10 = (Number of successful queries) / (Total number of queries)
This metric measures how effectively the system retrieves relevant assessments early in the ranking.

6. Submission CSV Generation
To ensure reproducibility and automated evaluation:
Assessment names are used as queries
The recommendation API is called programmatically
Results are saved in a ranked CSV format

CSV format:
query,assessment_url,rank

This file is generated using:
evaluation/generate_submission.py

7. Project Structure
SHL-Assessment-Recommendation-Engine/
│
├── app/
│   ├── main.py
│   ├── recommender.py
│   ├── embeddings.py
│   └── data/
│       └── shl_assessments.json
│
├── evaluation/
│   ├── evaluate.py
│   └── generate_submission.py
│
├── scripts/
│   └── build_final_dataset.py
│
├── shl_raw_links.json
├── submission.csv
├── requirements.txt
└── README.md

8. Assumptions and Design Choices
Focused on semantic relevance rather than exact keyword matching
Metadata enrichment is rule-based for consistency
Designed for scalability and reproducibility
Prioritized clarity and maintainability over complexity

9. How to Run the Project
pip install -r requirements.txt
uvicorn app.main:app --reload (http://127.0.0.1:8000/docs)
This below code should run in an another terminal while the above localhost should be in a running state:
python evaluation/evaluate.py
python evaluation/generate_submission.py

11. Conclusion
This project demonstrates:
Strong problem understanding
Research-oriented thinking
Practical system design
Scalable semantic retrieval
Clean evaluation methodology

The solution closely mirrors real-world assessment recommendation systems and aligns well with SHL’s domain and expectations for an AI Research Intern.
