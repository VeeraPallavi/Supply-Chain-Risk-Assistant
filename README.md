# Enterprise GenAI Supply Chain Risk Intelligence Assistant

## Overview

The Enterprise GenAI Supply Chain Risk Intelligence Assistant is a Retrieval-Augmented Generation (RAG) and Multi-Agent AI system designed to investigate operational risks across supply chain processes.

The platform analyzes order and inventory data, retrieves relevant historical records using semantic search, identifies operational risks, generates recommendations, and produces AI-powered executive investigation reports.

---

## Problem Statement

Traditional supply chain management systems rely on dashboards, predefined business rules, and manual analysis to monitor inventory levels and order operations. While these systems provide visibility into supply chain activities, they often lack intelligent reasoning, explainability, and proactive decision support.

This project leverages Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and Multi-Agent Systems to perform end-to-end supply chain risk investigation, helping supply chain managers make data-driven decisions.

---

## Features

### Operational Risk Assessment

- Delayed Orders Detection
- Pending Deliveries Detection
- Inventory Shortage Detection
- Transportation Cost Risk Detection

### Multi-Agent Architecture

- Retrieval Agent
- Risk Agent
- Recommendation Agent
- Reporting Agent

### AI-Powered Executive Reporting

- Executive Investigation Reports
- Risk Explanations
- Actionable Recommendations

### Explainable AI

- Evidence-Based Responses
- Grounded LLM Outputs
- Business Rule Validation

---

## Architecture

```text
User Query
     │
     ▼
FastAPI API Layer
     │
     ▼
SupplyChainWorkflow
     │
 ┌───┼─────────────────────┐
 │   │                     │
 ▼   ▼                     ▼
Retrieval Agent      Risk Agent
                           │
                           ▼
                Recommendation Agent
                           │
                           ▼
                    Reporting Agent
                           │
                           ▼
                 Executive Investigation Report
```

---


## Project Structure

```text
Supply-Chain-Assistant/
│
├── data/
│   ├── orders.csv
│   └── inventory.csv
│
├── vector_db/
│   ├── faiss.index
│   └── documents.pkl
│
├── src/
│   ├── agents/
│   │   ├── retrieval_agent.py
│   │   ├── risk_agent.py
│   │   ├── recommendation_agent.py
│   │   └── reporting_agent.py
│   │
|   ├── llm/
|   |   ├── groq_client.py
|   |
│   ├── rag/
|   |   ├── data_loader.py
|   |   ├── document_builder.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── orchestration/
│   │   ├── models.py
|   |   ├── agents.py
│   │   └── pydantic_orchestrator.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   └── models/
│       └── api_models.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/supply-chain-risk-intelligence-assistant.git

cd supply-chain-risk-intelligence-assistant
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API=your_groq_api_key
API_KEY=your_api_key
```

---

## Build Vector Database

Run the vector store creation script:

```bash
python build_vector_store.py
```

This step:

- Loads datasets
- Creates documents
- Generates embeddings
- Builds FAISS index
- Stores vector embeddings

Generated files:

```text
vector_db/faiss.index
vector_db/documents.pkl
```

---

## Running the CLI Application

```bash
python main.py
```

Example:

```text
Ask a Supply Chain Question:

Which orders got delayed?
```

---

## Running FastAPI

Start FastAPI server:

```bash
uvicorn src.api.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Guardrails Implemented

### Grounding Guardrail

- LLM responses are generated only from retrieved evidence.

### Business Rule Guardrail

- Inventory replenishment is recommended only when:

```text
Stock Level < Reorder Level
```

### Output Format Guardrail

Every response contains:

- Documents
- Risks
- Recommendations
- Report

### Hallucination Prevention

- The model is instructed not to assume unsupported facts.

---

## Future Enhancements

- Investigation History Storage
- Risk Severity Scoring
- Streamlit Dashboard
- Hybrid Search (BM25 + Vector Search)
- JWT Authentication
- Monitoring and Logging

---
