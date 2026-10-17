# 30-Day Backend Sprint: Progress & Deliverables Tracker

Use this tracker to log your progress across the 30-day curriculum. Whenever you finish a day's deliverable and review questions, mark it completed.

---

## Overall Sprint Status

* **Current Active Day:** Day 1
* **Days Completed:** 0 / 30
* **Test Suite Pass Rate:** 25 / 25 passed
* **Target Completion Date:** 30 days from Day 1 start

---

## WEEK 1: Core Relational Architecture & The Request Lifecycle

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **01** | Python 3.12+ & Clean Project Architecture | `In Progress` | — | Local venv running FastAPI server (`uvicorn`) | [ ] |
| **02** | Relational Modeling with PostgreSQL & SQLAlchemy 2.0 | `Pending` | — | Standalone table creation script & psql connection | [ ] |
| **03** | Foreign Keys, Cascade Deletes & Eager Loading | `Pending` | — | Cascade deletion verified in PostgreSQL shell | [ ] |
| **04** | Schema Migrations with Alembic | `Pending` | — | Migration lifecycle tested (`upgrade head` / `downgrade -1`) | [ ] |
| **05** | FastAPI Dependency Injection & Session Lifecycle | `Pending` | — | `get_db` session generator reconstructed from memory | [ ] |
| **06** | The Full Vertical Slice (Router $\rightarrow$ Service $\rightarrow$ DB) | `Pending` | — | New `GET /api/v1/applications/{id}` endpoint tested | [ ] |
| **07** | Week 1 Integration Drill & Closed-Book Defense | `Pending` | — | Architectural diagram drawn & Week 1 Log completed | [ ] |

---

## WEEK 2: Authentication, Security & Multi-Tenant Isolation

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **08** | User Registration & Cryptographic Bcrypt Hashing | `Pending` | — | 60-character bcrypt hash verified in DB | [ ] |
| **09** | Stateless Authentication with JWT & OAuth2 Bearer | `Pending` | — | Token generation & Swagger authorization verified | [ ] |
| **10** | Auth Middleware & Route Protection (401 vs 403) | `Pending` | — | All 6 authentication tests passing (`test_auth.py`) | [ ] |
| **11** | Multi-Tenant Isolation Barrier (Preventing BOLA) | `Pending` | — | Negative cross-tenant isolation test passing | [ ] |
| **12** | Nested Relational Endpoints & Journal Notes | `Pending` | — | Note lifecycle tests passing (`test_interviews_and_notes.py`) | [ ] |
| **13** | Adversarial Input Sanitization & Enum Validation | `Pending` | — | 3 edge-case validations added to Pydantic schemas | [ ] |
| **14** | Week 2 Security & Isolation Defense Drill | `Pending` | — | Mutation test drill executed & Week 2 Log completed | [ ] |

---

## WEEK 3: Automated Testing Rigor, Optimization & Production Readiness

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **15** | Pytest Fundamentals & Asynchronous HTTPX Client | `Pending` | — | Pre-seeded job application fixture added in `conftest.py` | [ ] |
| **16** | Ephemeral Test Database Harness | `Pending` | — | Full suite running in under 20 seconds | [ ] |
| **17** | Writing Comprehensive Integration Tests | `Pending` | — | 3 new integration tests committed with 100% pass | [ ] |
| **18** | Security Isolation Test Suite Mastery | `Pending` | — | All 6 isolation tests reconstructed and passing | [ ] |
| **19** | Database Indexing & Query Optimization | `Pending` | — | `EXPLAIN ANALYZE` before-and-after query metrics recorded | [ ] |
| **20** | Containerization with Docker & Docker Compose | `Pending` | — | JobPulse & PostgreSQL running via `docker-compose up -d` | [ ] |
| **21** | Week 3 Infrastructure & Testing Consolidation | `Pending` | — | Tests executed inside Docker container & Week 3 Log | [ ] |

---

## WEEK 4: Analytics Engine, Independent Feature Extension & Job Launch

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **22** | Funnel Analytics Calculation Engine | `Pending` | — | All 3 analytics calculation tests passing | [ ] |
| **23** | Independent Feature Extension (Schema & Migration) | `Pending` | — | `InterviewScorecard` Alembic migration created & applied | [ ] |
| **24** | Independent Feature Extension (Routers & Services) | `Pending` | — | Interactive Swagger UI reflecting scorecard endpoints | [ ] |
| **25** | Independent Feature Extension (Pytest Verification) | `Pending` | — | Test suite expanded to 28+ passing tests | [ ] |
| **26** | Continuous Integration (CI) with GitHub Actions | `Pending` | — | Green passing CI badge on GitHub repository | [ ] |
| **27** | Production Cloud Deployment | `Pending` | — | Live public Swagger documentation hosted on Render/Railway | [ ] |
| **28** | Mock Technical Interview Drill 1 (Databases & Architecture) | `Pending` | — | Verbal answers recorded and self-critiqued | [ ] |
| **29** | Mock Technical Interview Drill 2 (Security, APIs & Testing) | `Pending` | — | 4 interview answers delivered verbally in under 3 mins each | [ ] |
| **30** | GitHub Optimization & The Outreach Campaign | `Pending` | — | 5 targeted outreach messages sent to tech leads | [ ] |
