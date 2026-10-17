# SQA & SDET Research, Curriculum & Interview Suite (2025–2026)

This directory houses the empirical labor market research, hands-on 30-day curriculum, and technical interview handbook for **Software Quality Assurance (SQA) Engineers** and **Software Development Engineers in Test (SDETs)** targeting entry-level to 1-year experience roles.

---

## Suite Documents

| Document | Purpose & Scope | Direct Link |
| :--- | :--- | :--- |
| **1. Market Analysis Paper** | Empirical macroeconomic analysis synthesizing P@SHA 2025, SBP exports ($4.6B), AI-era testing transitions, and tier-1 Pakistani hiring requirements (Arbisoft, Systems Ltd, 10Pearls, Emumba, Devsinc). | [qa_sdet_market_analysis.md](qa_sdet_market_analysis.md) |
| **2. 30-Day Hands-on Roadmap** | Day-by-day 4-hour deliberate practice blueprint building 1-year equivalent hands-on competence (STLC, Postman/Newman, Pytest, Playwright, SQL, CI/CD). | [30_day_qa_sdet_hands_on_roadmap.md](30_day_qa_sdet_hands_on_roadmap.md) |
| **3. Technical Interview Handbook** | 35 in-depth technical questions with model answers covering test design techniques, API security (OWASP BOLA & Mass Assignment), Pytest fixtures, Playwright POM, SQL queries, flaky tests, and real-world diagnostic reasoning. | [qa_interview_handbook.md](qa_interview_handbook.md) |

---

## 4-Week Milestone Progression

```
+---------------------------------------------------------------------------------------------------------+
|                                     30-DAY QA / SDET CURRICULUM ARCHITECTURE                            |
+-----------------------------+-----------------------------+-----------------------+---------------------+
| WEEK 1: STLC & Test Design  | WEEK 2: API Automation      | WEEK 3: Code-Based    | WEEK 4: Performance |
|                             |    (Postman & Newman)       |    (Pytest/Playwright)|    & Interview Prep |
+-----------------------------+-----------------------------+-----------------------+---------------------+
| • SDLC/STLC Agile workflows | • HTTP Protocols & REST     | • Pytest fixtures     | • Locust load tests |
| • Boundary Value Analysis   | • Postman Dynamic Env Vars  | • Asynchronous HTTPX  | • GitHub Actions CI |
| • Equivalence Partitioning  | • JavaScript assertions     | • Direct SQL audits   | • Synthetic AI data |
| • Decision Tables & FSM     | • Automated API Chaining    | • OWASP BOLA tests    | • QA Portfolio repo |
| • Jira-style Defect Reports | • Negative status assertions| • Playwright Web UI   | • 2 Mock Interviews |
| • Exploratory Charters      | • CLI Newman HTML reports   | • Page Object Model   | • Targeted Outreach |
+-----------------------------+-----------------------------+-----------------------+---------------------+
```

---

## System Under Test (SUT)

All testing exercises throughout this suite are grounded in **[JobPulse API](../../backend)** (`backend/app`), a live multi-tenant FastAPI service featuring relational PostgreSQL models, JWT authentication, and automated integration test harnesses. This eliminates tutorial toys and gives the candidate verifiable, production-style testing proof on their GitHub profile.
