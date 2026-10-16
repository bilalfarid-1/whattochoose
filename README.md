# What To Choose — 2026 Software Engineering Labor Market Research & JobPulse Platform

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)](https://www.postgresql.org/)
[![Backend Tests](https://img.shields.io/badge/Backend%20Tests-25%20Passing-success.svg)](backend/tests/)
[![Research Checks](https://img.shields.io/badge/Research%20Checks-Passing-success.svg)](research/tests/)
[![AI Learning Framework](https://img.shields.io/badge/AI%20Framework-6%20Passing-success.svg)](ai_learning_research/tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Author:** Muhammad Bilal Farid  
*BS Software Engineering Graduate & Independent Technology Analyst*  
*Islamabad/Rawalpindi, Pakistan*  
*Repository:* [github.com/bilalfarid-1/whattochoose](https://github.com/bilalfarid-1/whattochoose)

---

## Overview

This repository unites three complementary engineering deliverables:

1. **Empirical Market Research Brief (`/research`):**  
   An in-depth empirical investigation titled *"The Shifting Landscape of Entry-Level Software Engineering: An Empirical Market Analysis and Strategic Guide for Pakistani Graduates"*. It analyzes macroeconomic normalization (post-ZIRP), SWE-bench Verified coding agent progression, and Pakistan IT industry dynamics ($4.60B reported FY26 ICT exports, 21.4% CAGR vs. 71.8% senior hiring preference per P@SHA 2025).

2. **AI-Augmented Engineering Mastery Framework (`/ai_learning_research`):**  
   A research-informed learning framework grounded in empirical studies, designed to master Python Backend Systems Engineering using AI as a deliberate cognitive amplifier. Synthesizing 16 categorized scholarly references across Cognitive Science, Computing Education (ACM SIGCSE / ICER), and HCI (ACM CHI), it helps graduates avoid passive tutorial bingeing through 4 operational learning protocols, research-informed system prompts, and a 30-Day Active-Learning Sprint.

3. **JobPulse Platform (`/backend` & `/frontend`):**  
   A production-style portfolio application built to operationalize the research recommendations. It provides a job application tracker, interview stage manager, debrief journal, funnel conversion analytics, and an interactive market research visualizer built with synchronous **FastAPI**, **SQLAlchemy 2.0**, **PostgreSQL**, **Pydantic v2**, **Alembic**, **PyTest**, and a modern **Tailwind/Vanilla JS Single-Page Application (SPA)**, utilizing FastAPI's worker threadpool to handle blocking database operations safely.

---

## Repository Structure

```
whattochoose/
│
├── frontend/                           # Interactive Modern Single-Page Application (SPA)
│   └── index.html                      # Pipeline Kanban, Conversion Analytics & Research Explorer
│
├── backend/                            # Production-Style FastAPI REST API
│   ├── app/
│   │   ├── main.py                     # App entrypoint (serves API & Dashboard UI)
│   │   ├── core/                       # Config (Pydantic Settings), DB engine, JWT/Bcrypt security
│   │   ├── models/                     # SQLAlchemy 2.0 ORM models (User, Company, Application, Interview, Note)
│   │   ├── schemas/                    # Pydantic v2 request/response schemas
│   │   ├── crud/                       # Database repository operations & funnel analytics
│   │   ├── api/                        # Versioned API v1 routers & JWT auth dependency
│   │   └── static/                     # Embedded static build
│   ├── alembic/                        # Versioned database migration scripts
│   ├── alembic.ini                     # Alembic migration configuration
│   ├── tests/                          # 25 passing PyTest unit, integration, migration & cross-user security tests
│   ├── docker-entrypoint.sh            # Container migration runner & process supervisor
│   ├── Dockerfile                      # Python 3.12 slim container
│   ├── docker-compose.yml              # Local dev multi-container setup with PostgreSQL 16
│   └── requirements.txt                # Backend dependencies
│
├── ai_learning_research/               # AI-Augmented Learning Science & Execution Protocols
│   ├── README.md                       # Navigation guide & overview
│   ├── SOURCES.md                      # Academic bibliographic audit (ACM SIGCSE, ICER, CHI, Wharton)
│   ├── framework/                      # Cognitive architecture & the 6 deadly anti-patterns
│   ├── protocols/                      # Socratic decomposition, adversarial review, mutation drills, Feynman
│   ├── prompts/                        # Research-informed prompts with graduated assistance guardrails
│   ├── roadmap/                        # 30-Day Active-Learning Backend Sprint (JobPulse focus)
│   └── tests/                          # 6 passing tests checking citation identifiers and document consistency
│
└── research/                           # Empirical Labor Market Research & Datasets
    ├── paper/
    │   ├── main_manuscript.md          # Complete whitepaper & analysis brief
    │   ├── references.bib              # BibTeX citation library
    │   └── figures/                    # 300 DPI publication figures (Fig 1 - Fig 4)
    ├── data/
    │   ├── raw/
    │   │   ├── longitudinal_se_data.json # Multi-year harmonized empirical dataset
    │   │   └── IHLIDXUSTPSOFTDEVE.csv    # Official daily FRED Indeed postings series (2020-2026)
    │   ├── processed/                  # Processed time-series & benchmark milestone CSVs
    │   └── SOURCES.md                  # Comprehensive source audit & provenance documentation
    ├── src/
    │   └── analyze_market_dynamics.py  # Python statistical modeling & figure generation
    ├── tests/
    │   ├── test_data_integrity.py      # Automated data integrity, CAGR math & rubric tests
    │   └── test_fred_aggregation.py    # Offline unit test for FRED annual aggregation metrics
    ├── roadmap/
    │   ├── 2026_graduate_readiness_matrix.md # Skills triage matrix
    │   └── pakistani_fresh_grad_playbook.md  # 90-day actionable execution guide
    └── walkthrough.md                  # Methodological audit & verification walkthrough
```

---

## Quickstart Guide

### Option 1: Run the Full-Stack JobPulse Application

```bash
# 1. Enter the backend directory
cd backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
alembic upgrade head

# 4. Run the automated test suite (25 passing backend tests)
python -m pytest -v

# 5. Launch the application (serves both API & Frontend Dashboard)
uvicorn app.main:app --reload --port 8000
```

Open your browser to:
* **Interactive JobPulse Web App:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)
* **Interactive OpenAPI Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

*(Alternatively, you can open `frontend/index.html` directly in any web browser to run in zero-dependency client mode!)*

---

### Option 2: Docker Compose (PostgreSQL 16 Multi-Container Dev Environment)

```bash
cd backend
# Starts PostgreSQL 16 and JobPulse API (automatically applies migrations via docker-entrypoint.sh)
docker compose up --build -d
```

---

### Option 3: Run the Empirical Research Pipeline

```bash
# 1. Run automated data integrity and FRED aggregation tests
python research/tests/test_data_integrity.py
python -m pytest -v research/tests/test_fred_aggregation.py

# 2. Run market dynamics modeling and regenerate all publication figures
python research/src/analyze_market_dynamics.py
```

---

### Option 4: Run the AI Learning Framework Consistency Tests

```bash
# Run automated consistency checks verifying citation identifiers, system prompt rules, and document structure
python -m pytest -v ai_learning_research/tests/test_protocols_and_sources.py
```

---

## Core Findings of the Research Brief

1. **Pakistan ICT Export Growth vs. Experience Bias:**  
   Pakistan's ICT export remittances expanded from $\$1.440\text{B}$ (FY20) to a reported full-year outturn of **US$ 4.60 Billion** in FY26 (**$+21.4\%$ 6-year CAGR** per SBP, Ministry of Finance, and APP reports). However, according to the P@SHA Skills Survey 2025, **$71.8\%$** of industry hiring demand across surveyed member firms is concentrated in experienced roles, creating high qualification friction for fresh graduates.

2. **The Verification Bottleneck:**  
   As autonomous coding models reduce the marginal cost of producing routine syntax ($C_{\text{gen}} \downarrow$), human engineering effort shifts toward verifying business correctness, handling non-trivial edge cases, and auditing security ($C_{\text{verif}} \uparrow$).

3. **Strategic Specialization Recommendation:**  
   Given the importance of demonstrable technical competence in a competitive entry-level market, candidates benefit from focusing deeply on a high-leverage backend stack (**Python / FastAPI + PostgreSQL + PyTest**) to build, test, deploy, and defend a substantial portfolio application rather than engaging in superficial multi-stack switching. This is a reasoned career strategy, not a causal finding established by the labor-market dataset.

---

## Suggested Citation

```bibtex
@techreport{farid2026se_market,
  title = {The Shifting Landscape of Entry-Level Software Engineering: An Empirical Market Analysis and Strategic Guide for Pakistani Graduates},
  author = {Farid, Muhammad Bilal},
  institution = {Independent Technology Analysis},
  year = {2026},
  url = {https://github.com/bilalfarid-1/whattochoose}
}
```
