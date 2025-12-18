# SHL Assessment Recommendation Engine  
**Research Intern Assignment – Option 1**

Candidate: Ipshita Karmakar  
Repository:SHL-Assessment-Recommendation-Engine  

---

## 1. Objective of the Assignment

The objective of this project is to build an **Assessment Recommendation Engine** that recommends relevant SHL assessments for a given hiring requirement or job description.

The system is designed to:
- Understand free-text hiring queries
- Retrieve relevant assessments from the SHL product catalogue
- Rank assessments meaningfully
- Be scalable, reproducible, and easy to evaluate

---

## 2. Why This Approach Was Chosen

Among the two options provided by SHL, I selected **Option 1: Assessment Recommendation Engine** because it aligns closely with:

- SHL’s core assessment and talent analytics domain
- Real-world recommendation system problems
- Research challenges in semantic similarity, ranking, and evaluation

This approach allows demonstrating **both research thinking and practical system design**, which are critical for an AI Research Intern role.

---

## 3. High-Level System Overview

The system is built as a **semantic retrieval pipeline** consisting of the following stages:

1. Data Collection & Preparation  
2. Metadata Enrichment  
3. Text Embedding  
4. Vector Indexing (FAISS)  
5. Recommendation API (FastAPI)  
6. Evaluation & Submission Generation  

Each stage is modular and independently reproducible.

---

## 4. Step-by-Step Implementation

### 4.1 Data Collection

- Assessment names and URLs were collected from the **public SHL product catalogue**.
- Due to pagination and intermittent server-side rate limiting, a seed set of real SHL assessments was extracted.
- The final dataset contains **377 assessment entries**, sufficient to evaluate scalability and retrieval quality.

**Raw data file:**
### 4.2 Data Enrichment

The raw assessment data is enriched programmatically to ensure consistency, completeness, and usability for downstream tasks.

For each assessment:
- A concise description is generated based on the assessment name
- The assessment category is inferred (Knowledge & Skills or Personality & Behaviour)
- Estimated duration is assigned
- Delivery-related attributes such as adaptive and remote support are added

The enriched data enables uniform representation across all assessments.

**Output file:**

---

### 4.3 Text Embedding

To capture semantic meaning beyond exact keyword matches, textual fields are converted into dense vector representations.

The following steps are performed:
- Assessment descriptions are embedded using a sentence-level embedding model
- User queries are embedded using the same model
- Both embeddings are projected into a shared semantic space

This allows the system to match conceptually similar queries and assessments even when wording differs.

---

### 4.4 Vector Indexing (FAISS)

To enable fast and scalable similarity search, all assessment embeddings are indexed using FAISS.

Key steps:
- Assessment embeddings are indexed once during initialization
- The index is persisted and reused across API calls
- Cosine similarity is used to retrieve nearest neighbors

FAISS ensures low-latency retrieval and supports scaling to large assessment catalogs.

---

### 4.5 Recommendation API (FastAPI)

A RESTful API is implemented using FastAPI to expose the recommendation functionality.

The API includes:
- A health endpoint for service monitoring
- A recommendation endpoint for retrieving ranked assessments

The API design emphasizes clarity, extensibility, and ease of integration with external systems.

---

### 4.6 Ranking and Recommendation Logic

For a given query:
- The query embedding is computed
- Similar assessments are retrieved from the FAISS index
- Results are ranked based on similarity scores

Only the top-ranked assessments are returned to ensure relevance and interpretability.

---

### 4.7 Evaluation Methodology

The system is evaluated using Recall@10, a commonly used metric in recommendation systems.

Evaluation steps:
- Define representative hiring queries
- Retrieve top-10 assessments for each query
- Measure whether relevant assessments appear within the top results

This evaluation focuses on early retrieval quality rather than exhaustive ranking.

---

### 4.8 Submission File Generation

To support automated evaluation and reproducibility:
- Assessment names are used as input queries
- The recommendation API is invoked programmatically
- Results are stored in a ranked CSV format

The generated file follows the required structure:
## 5. Evaluation Methodology

The recommendation system is evaluated to measure how effectively it retrieves relevant assessments for a given hiring query.

The evaluation focuses on **early relevance**, which is critical in real-world recommendation systems where users typically review only the top results.

---

### 5.1 Evaluation Metric: Recall@10

Recall@10 = (Number of successful queries) / (Total number of queries)

Recall@10 is used as the primary evaluation metric.

It measures whether at least one relevant assessment appears within the top 10 recommended results for a query.

This metric is well-suited for recommendation systems where ranking quality is more important than exhaustive retrieval.

---

### 5.2 Evaluation Process

The evaluation process follows these steps:

- Define a set of representative hiring queries
- Retrieve the top-10 recommended assessments for each query
- Check whether a relevant assessment appears in the retrieved results

Each query is treated independently, and success is recorded if relevance is observed within the top-10.

---

### 5.3 Metric Definition


This metric provides a simple and interpretable measure of recommendation effectiveness.

---

## 6. Submission File Generation

To support automated assessment and reproducibility, a submission file is generated in CSV format.

The submission process ensures that:
- The recommendation API is used as the single source of truth
- Results are ranked consistently
- The output format adheres to evaluation requirements

---

### 6.1 CSV Generation Logic

The following steps are performed:

- Assessment names are used as input queries
- The recommendation API is invoked programmatically
- Ranked assessment URLs are extracted
- Results are written to a CSV file with rank ordering

---

### 6.2 CSV Format

The generated CSV file follows this structure:
query,assessment_url,rank

Each row represents a ranked recommendation for a given query.

---

## 7. Project Structure

The project is organized to ensure modularity, clarity, and ease of maintenance.


Each row represents a ranked recommendation for a given query.

SHL-Assessment-Recommendation-Engine/
│
├── app/
│ ├── main.py
│ ├── recommender.py
│ ├── embeddings.py
│ └── data/
│ └── shl_assessments.json
│
├── evaluation/
│ ├── evaluate.py
│ └── generate_submission.py
│
├── scripts/
│ └── build_final_dataset.py
│
├── shl_raw_links.json
├── submission.csv
├── requirements.txt
└── README.md


Each module is responsible for a clearly defined stage of the pipeline.

---

## 8. Assumptions and Design Choices

The following assumptions and design decisions were made during development:

- Semantic relevance is prioritized over exact keyword matching
- Metadata enrichment is rule-based to ensure consistency
- The system is designed to scale with increasing catalog size
- Simplicity and clarity are favored over over-engineering

These choices balance research quality with practical implementation constraints.

---

## 9. How to Run the Project

Follow the steps below to run the system locally.

---

### 9.1 Install Dependencies

```bash
pip install -r requirements.txt

### 9.2 Start the Recommendation API

Start the FastAPI application using the following command:

```bash
uvicorn app.main:app --reload

Once the server is running, the interactive API documentation can be accessed at:
http://127.0.0.1:8000/docs

This interface can be used to manually test the recommendation endpoint.

### 9.3 Run Evaluation and Submission Scripts

While the API is running, open a separate terminal and execute the following commands:

python evaluation/evaluate.py

The evaluation script computes retrieval metrics for sample queries.
The submission script generates a ranked CSV file for final submission.

### 10. Conclusion

This project demonstrates:
A clear understanding of the assessment recommendation problem
A research-oriented approach to semantic retrieval
Practical system design using embeddings and vector search
Scalable and efficient retrieval with FAISS
Transparent and reproducible evaluation methodology










