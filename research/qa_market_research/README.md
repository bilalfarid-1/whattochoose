# SQA & SDET Research, Curriculum & Interview Suite (2025–2026)

This directory houses the empirical labor market research, two-phase job-ready automation roadmap, and technical interview handbook for **Software Quality Assurance (SQA) Engineers** and **Software Development Engineers in Test (SDETs)** targeting entry-level, associate, and junior automation roles.

---

## Suite Documents

| Document | Purpose & Scope | Direct Link |
| :--- | :--- | :--- |
| **1. Market Analysis Paper** | Empirical macroeconomic analysis synthesizing P@SHA 2025, SBP exports ($4.6B), AI-era testing transitions, and tier-1 Pakistani hiring requirements (Arbisoft, Systems Ltd, 10Pearls, Emumba, Devsinc). | [qa_sdet_market_analysis.md](qa_sdet_market_analysis.md) |
| **2. 30-Day Job-Ready Roadmap** | Core 4-hour deliberate practice blueprint building demonstrable entry-level competence (STLC, Postman, Python/pytest, SQL, multi-user authorization, Playwright, and CI/CD). | [30_day_job_ready_qa_roadmap.md](30_day_job_ready_qa_roadmap.md) |
| **3. Days 31–60 Extension** | Optional second-phase depth extension (suite maintainability, contract testing, failure diagnostics, controlled performance testing, and specialization branches). | [days_31_60_qa_automation_extension.md](days_31_60_qa_automation_extension.md) |
| **4. Technical Interview Handbook** | 35 in-depth technical questions with model answers covering test design techniques, API security (OWASP BOLA & Mass Assignment), pytest fixtures, Playwright POM, SQL queries, flaky tests, and diagnostic reasoning. | [qa_interview_handbook.md](qa_interview_handbook.md) |
| **5. Legacy Roadmap (Archived)** | Historical single-file roadmap retained as a redirect stub to preserve external links. | [30_day_qa_sdet_hands_on_roadmap.md](30_day_qa_sdet_hands_on_roadmap.md) |

---

## Two-Phase Curriculum Architecture

```
+---------------------------------------------------------------------------------------------------------+
|                                  PHASE 1: 30-DAY JOB-READY QA ROADMAP                                   |
+-----------------------------+-----------------------------+-----------------------+---------------------+
| WEEK 1: STLC & Test Design  | WEEK 2: HTTP & Postman      | WEEK 3: Python/pytest | WEEK 4 & FINAL:     |
| (Days 1–7)                  | (Days 8–14)                 | (Days 15–21)          | (Days 22–30)        |
+-----------------------------+-----------------------------+-----------------------+---------------------+
| • SDLC/STLC Agile workflows | • RFC 9110 HTTP semantics   | • pytest fixtures     | • Playwright Web UI |
| • Boundary Value Analysis   | • Status codes & idempotency| • Parameterization    | • Web-first asserts |
| • Equivalence Partitioning  | • Postman collections & vars| • Safe data cleanup   | • Trace diagnostics |
| • Decision Tables & FSM     | • Positive/negative flows   | • Direct SQL audits   | • GitHub Actions CI |
| • Structured Defect Reports | • Validation testing        | • OWASP BOLA tests    | • CV & Portfolio    |
| • Exploratory Charters      | • Collection report         | • API test report     | • Mock interview    |
| • Day 7 Consolidation       | • Day 14 Consolidation & CV | • Day 21 Consolidation| • Day 30 Readiness  |
+-----------------------------+-----------------------------+-----------------------+---------------------+

+---------------------------------------------------------------------------------------------------------+
|                               PHASE 2: DAYS 31–60 QA AUTOMATION EXTENSION                               |
+-----------------------------+-----------------------------+-----------------------+---------------------+
| BLOCK 1: API Maintainability| BLOCK 2: UI Observability   | BLOCK 3: Security & CI| BLOCK 4 & 5: Evals  |
| (Days 31–37)                | (Days 38–44)                | (Days 45–51)          | & Launch (Days 52–60|
+-----------------------------+-----------------------------+-----------------------+---------------------+
| • Test refactoring & helpers| • User-facing locators      | • Multi-tenant matrix | • 1 Specialization: |
| • Environment & secret safety| • Page/context fixtures    | • Mass assignment     |   - LLM Evals (Node)|
| • Schema & contract testing | • End-to-end critical flow  | • Token expiry checks |   - Mobile testing  |
| • Negative edge cases       | • Failure trace analysis    | • Constraint audits   |   - Locust perf     |
| • Data lifecycle & cleanup  | • Cross-browser/mobile check| • Reproducible CI     |   - JS/TS sampler   |
| • Catch-up & Rest days      | • Catch-up & Rest days      | • Catch-up & Rest days| • Clean-clone & Mock|
+-----------------------------+-----------------------------+-----------------------+---------------------+
```

---

## System Under Test (SUT)

All testing exercises throughout this suite are grounded in **[JobPulse API](../../backend)** (`backend/app`), a live multi-tenant FastAPI service featuring relational PostgreSQL models, JWT authentication, and automated integration test harnesses.

### Audited Route Inventory
The JobPulse backend exposes **20 business API operations across 13 unique business path templates**, plus 1 auto-generated documentation schema route (`GET /api/v1/openapi.json`), totaling 21 routable endpoints under `/api/v1`:

1. **Authentication (4 operations):**
   - `POST /api/v1/auth/register` (Register new account)
   - `POST /api/v1/auth/login` (JSON login with `email` and `password`)
   - `POST /api/v1/auth/login/oauth` (OAuth2 `application/x-www-form-urlencoded` form data for Swagger UI)
   - `GET /api/v1/auth/me` (Retrieve authenticated profile)
2. **Companies (3 operations):**
   - `GET /api/v1/companies/` (List company directory)
   - `POST /api/v1/companies/` (Create or get company record)
   - `GET /api/v1/companies/{company_id}` (Retrieve company details)
3. **Job Applications (5 operations):**
   - `GET /api/v1/applications/` (List user's applications)
   - `POST /api/v1/applications/` (Create job application)
   - `GET /api/v1/applications/{application_id}` (Retrieve application details — tenant isolated)
   - `PATCH /api/v1/applications/{application_id}` (Update application status/fields — tenant isolated)
   - `DELETE /api/v1/applications/{application_id}` (Delete application — tenant isolated)
4. **Interviews (4 operations):**
   - `GET /api/v1/applications/{application_id}/interviews` (List interview stages — nested)
   - `POST /api/v1/applications/{application_id}/interviews` (Schedule interview stage — nested)
   - `PATCH /api/v1/interviews/{interview_id}` (Update interview outcome/notes — direct)
   - `DELETE /api/v1/interviews/{interview_id}` (Delete interview stage — direct)
5. **Notes & Debriefs (3 operations):**
   - `GET /api/v1/applications/{application_id}/notes` (List debrief journal notes — nested)
   - `POST /api/v1/applications/{application_id}/notes` (Create debrief note — nested)
   - `DELETE /api/v1/notes/{note_id}` (Delete debrief note — direct)
6. **Funnel Analytics (1 operation):**
   - `GET /api/v1/analytics/` (Compute user funnel conversion metrics)

*UI Practice Fallback:* For browser UI automation, SauceDemo is explicitly labeled as a public practice fallback if the candidate chooses not to run the local JobPulse SPA frontend.
