# 3D In-Vitro Lead Generation Web Agent

## Problem Statement
This project demonstrates a web-agent style lead generation system that identifies,
enriches, and ranks potential clients interested in 3D in-vitro models for drug discovery
and toxicology research.

## Approach
The solution follows three stages:
1. Identification – Target relevant professionals based on role and domain
2. Enrichment – Add company, funding, location, and publication data
3. Ranking – Assign a probability score (0–100) using weighted business signals

## Scoring Logic
- Role Fit: +30
- Funding Stage: +20
- Uses In-Vitro Technology: +15
- Open to NAMs: +10
- Hub Location: +10
- Recent Scientific Publication: +40

## Tech Stack
- Python
- Pandas
- Streamlit

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
