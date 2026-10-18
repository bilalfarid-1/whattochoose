# JobPulse Backend Platform (System Under Test)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)](https://www.postgresql.org/)
[![Backend Tests](https://img.shields.io/badge/Backend%20Tests-25%20Passing-success.svg)](tests/)
[![QA Suite](https://img.shields.io/badge/QA%20Suite-60%20Days%20Ready-green.svg)](../qa/)

**JobPulse** is a production-style, multi-tenant job application tracking platform engineered with **FastAPI**, **SQLAlchemy 2.0**, **PostgreSQL 16**, **Pydantic v2**, and **Alembic**.

It serves two primary roles in this repository:
1. **The Application Service:** A fully functional REST API providing pipeline kanban management, stage tracking, journal debriefs, conversion analytics, and JWT authentication.
2. **The System Under Test (SUT):** The live, realistic target application evaluated by the **[QA & SDET Engineering Suite](../qa)**.

---

## 🏗️ Architectural Highlights & Trade-offs

```
+-----------------------------------------------------------------------------------------------------------------+
|                                          JOBPULSE SYSTEM ARCHITECTURE                                           |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
|  [ Frontend Client ]  <--->  [ FastAPI REST API (Python 3.12) ]  <--->  [ PostgreSQL 16 / SQLAlchemy 2.0 ]       |
|  • Vanilla JS SPA            • Worker Threadpool Concurrency            • Shared Company Catalog Directory       |
|  • Tailwind CSS UI           • Pydantic v2 Schema Validation            • Multi-Tenant User Applications         |
|  • Kanban & Analytics        • JWT Bearer Auth + Bcrypt                 • Private Interview Stages & Journal     |
|                                                                                                                 |
|  [ Database Migration Pipeline ]  -------------------->  [ Automated Verification Suite (25 Tests) ]             |
|  • Versioned Alembic Revisions                           • Full Transactional Rollbacks per Test Fixture        |
|  • Docker Supervisor Startup Runner                      • Strict Second-User (User B) 404 Isolation Tests      |
|  • Automated Schema Downgrade/Upgrade Lifecycle          • Comprehensive Coverage Across All CRUD Operations     |
+-----------------------------------------------------------------------------------------------------------------+
```

1. **Threadpool Concurrency Over Event-Loop Starvation:** Synchronous FastAPI route handlers execute across worker threadpools to handle blocking SQLAlchemy ORM database queries safely without starving the asynchronous event loop.
2. **Strict Multi-Tenant Row-Level Security (Non-Disclosing 404s):** When User B attempts to access, mutate, or delete User A's private application, interview stage, or note, the API returns `HTTP 404 Not Found` rather than `403 Forbidden`. This eliminates resource-enumeration attack vectors where malicious users probe for the existence of valid IDs.
3. **Automated Migration Lifecycle Testing:** [`tests/test_migrations.py`](tests/test_migrations.py) applies `alembic upgrade head`, reflects database tables and columns dynamically, tests clean `alembic downgrade base`, and reapplies migrations on a clean test database.
4. **Dual Auth Contracts:** Supports both OAuth2 standard form-encoded login (`/api/v1/auth/login/oauth`, also aliased at `/api/v1/auth/token`) and JSON body login (`/api/v1/auth/login` for API clients), allowing QA engineers to test content-type negotiation and schema enforcement.

---

## ⚡ 1-Minute Quickstart

### Option 1: Local Development (Python & SQLite / PostgreSQL)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Apply database migrations
alembic upgrade head

# 3. Run developer test suite (25 passing tests)
python -m pytest -v

# 4. Launch the API server
python -m uvicorn app.main:app --reload --port 8000
```

Open your browser to:
* **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Root Liveness Probe:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

### Option 2: Multi-Container Setup (Docker Compose with PostgreSQL 16)

```bash
# Boots PostgreSQL 16 and JobPulse API (automatically runs migrations on boot)
docker compose up --build -d
```

---

## 📋 Endpoint Inventory (20 Operations)

The JobPulse API exposes 20 operations across 13 route templates:

| Module | Method | Path | Auth | Description |
| :--- | :--- | :--- | :---: | :--- |
| **System** | `GET` | `/` | None | Welcome ping with API version. |
| **System** | `GET` | `/health` | None | Liveness health probe returning `{"status": "ok"}`. |
| **Auth** | `POST` | `/api/v1/auth/register` | None | Register new user account. |
| **Auth** | `POST` | `/api/v1/auth/login` | None | JSON-based authentication returning Bearer token. |
| **Auth** | `POST` | `/api/v1/auth/login/oauth` | Form | OAuth2 form-data login returning Bearer token (also aliased at `/api/v1/auth/token`). |
| **Auth** | `GET` | `/api/v1/auth/me` | Bearer | Retrieve current user profile. |
| **Companies** | `GET` | `/api/v1/companies/` | Bearer | Global shared directory of companies. |
| **Companies** | `POST` | `/api/v1/companies/` | Bearer | Create company record in directory. |
| **Companies** | `GET` | `/api/v1/companies/{id}` | Bearer | Retrieve single company details. |
| **Applications** | `GET` | `/api/v1/applications/` | Bearer | List current user's job applications. |
| **Applications** | `POST` | `/api/v1/applications/` | Bearer | Submit job application. |
| **Applications** | `GET` | `/api/v1/applications/{id}` | Bearer | Fetch application (returns 404 for cross-tenant ID). |
| **Applications** | `PATCH` | `/api/v1/applications/{id}` | Bearer | Update status/stage (Applied -> Interview -> Offer/Rejected). |
| **Applications** | `DELETE` | `/api/v1/applications/{id}` | Bearer | Delete application and cascade child stages/notes. |
| **Interviews** | `GET` | `/api/v1/applications/{id}/interviews` | Bearer | List interview stages for application. |
| **Interviews** | `POST` | `/api/v1/applications/{id}/interviews` | Bearer | Schedule interview stage. |
| **Interviews** | `PATCH` | `/api/v1/interviews/{id}` | Bearer | Update interview outcome / feedback. |
| **Interviews** | `DELETE` | `/api/v1/interviews/{id}` | Bearer | Delete interview stage record. |
| **Notes** | `GET` | `/api/v1/applications/{id}/notes` | Bearer | List journal entries for application. |
| **Notes** | `POST` | `/api/v1/applications/{id}/notes` | Bearer | Append journal debrief note. |
| **Notes** | `DELETE` | `/api/v1/notes/{id}` | Bearer | Delete journal note record. |
| **Analytics** | `GET` | `/api/v1/analytics/` | Bearer | User funnel conversion rates and stage distributions. |

For the complete formal contract, schemas, and BOLA policies, see [`../qa/jobpulse_sut_contract.md`](../qa/jobpulse_sut_contract.md).

---

## 🛡️ Integration with the QA Suite

This backend is designed specifically to be tested from the outside:
* Automated Postman/Newman collections test the HTTP contract.
* Pytest suites test BOLA multi-tenant boundary attacks (`User A` vs `User B`).
* SQL scripts directly verify database state transitions and foreign key cascades.
* Playwright scripts automate end-to-end browser journeys.

To explore or run the QA curriculum and test suites, see **[`../qa/README.md`](../qa/README.md)**.
