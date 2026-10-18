# JobPulse System Under Test (SUT) Contract & Architecture Specification

**Component:** System Under Test (SUT) Reference  
**Application Name:** JobPulse  
**Technology Stack:** Python 3.12, FastAPI, PostgreSQL (SQLAlchemy + Alembic), Pydantic v2, Pytest  
**Repository Scope:** Local / Authorized Test Environment  
**Document Purpose:** Provide independent reviewers with the complete API route inventory, authentication semantics, and architectural isolation models required to evaluate the test coverage in the QA Career Roadmap.

---

## 1. Architectural Overview & Tenant Isolation

JobPulse is an open-source, multi-tenant job application tracking system engineered to demonstrate production-grade backend trade-offs. It serves as the primary System Under Test throughout the 30-Day QA Roadmap and Days 31–60 Extension.

### Tenancy & Security Boundary Model
1. **Multi-Tenant Isolation:** Every job application, interview stage, and interview note is owned by a specific `user_id`.
2. **Access Control (RBAC/BOLA):** Users may only view, update, or delete their own applications and nested records. A request by User B to access or mutate User A's resource ID must be rejected by the API with `404 Not Found` (JobPulse strictly enforces a non-disclosing 404 security model to eliminate resource enumeration vectors, though generic REST contracts sometimes permit 403 Forbidden).
3. **Shared Company Directory:** The company entity directory (`/api/v1/companies/`) is global and shared across all authenticated users, allowing candidates to link applications to standardized company records safely.

---

## 2. Complete Endpoint Inventory (20 Business Operations)

The JobPulse API exposes **20 business API operations across 13 unique business path templates**, plus one generated OpenAPI schema endpoint:

| # | HTTP Method | Path Template | Operation / Description | Auth Required | Request Content-Type | Expected Success Code |
|:---|:---|:---|:---|:---:|:---|:---:|
| 1 | `POST` | `/api/v1/auth/register` | Register new user account | No | `application/json` | `201 Created` |
| 2 | `POST` | `/api/v1/auth/login` | Authenticate user via JSON payload | No | `application/json` | `200 OK` |
| 3 | `POST` | `/api/v1/auth/login/oauth` | Authenticate user via OAuth2 Password Bearer flow | No | `application/x-www-form-urlencoded` | `200 OK` |
| 4 | `GET` | `/api/v1/auth/me` | Retrieve current authenticated user profile | Yes | N/A | `200 OK` |
| 5 | `GET` | `/api/v1/companies/` | List all companies in directory | Yes | N/A | `200 OK` |
| 6 | `POST` | `/api/v1/companies/` | Create a new company record | Yes | `application/json` | `201 Created` |
| 7 | `GET` | `/api/v1/companies/{company_id}` | Retrieve specific company details | Yes | N/A | `200 OK` |
| 8 | `GET` | `/api/v1/applications/` | List job applications for current user | Yes | N/A | `200 OK` |
| 9 | `POST` | `/api/v1/applications/` | Create a new job application | Yes | `application/json` | `201 Created` |
| 10 | `GET` | `/api/v1/applications/{application_id}` | Retrieve specific application details | Yes | N/A | `200 OK` |
| 11 | `PATCH` | `/api/v1/applications/{application_id}` | Partially update job application | Yes | `application/json` | `200 OK` |
| 12 | `DELETE`| `/api/v1/applications/{application_id}` | Delete job application and cascade children | Yes | N/A | `204 No Content` |
| 13 | `GET` | `/api/v1/applications/{application_id}/interviews` | List interview stages for application | Yes | N/A | `200 OK` |
| 14 | `POST` | `/api/v1/applications/{application_id}/interviews` | Schedule interview stage for application | Yes | `application/json` | `201 Created` |
| 15 | `PATCH` | `/api/v1/interviews/{interview_id}` | Update interview outcome / notes | Yes | `application/json` | `200 OK` |
| 16 | `DELETE`| `/api/v1/interviews/{interview_id}` | Delete interview stage record | Yes | N/A | `204 No Content` |
| 17 | `GET` | `/api/v1/applications/{application_id}/notes` | List journal notes for application | Yes | N/A | `200 OK` |
| 18 | `POST` | `/api/v1/applications/{application_id}/notes` | Append journal note to application | Yes | `application/json` | `201 Created` |
| 19 | `DELETE`| `/api/v1/notes/{note_id}` | Delete journal note record | Yes | N/A | `204 No Content` |
| 20 | `GET` | `/api/v1/analytics/` | Aggregate metrics & pipeline funnel data | Yes | N/A | `200 OK` |
| 21 | `GET` | `/api/v1/openapi.json` | Generated OpenAPI 3.1 specification schema | No | N/A | `200 OK` |

---

## 3. Key QA Engineering Distinction: Authentication Semantics

A critical area evaluated by the roadmap's Week 2 and Week 3 exercises is differentiating authentication request contracts:
1. **`POST /api/v1/auth/login` (Standard API Client flow):**  
   Accepts standard JSON body: `{"email": "user@example.com", "password": "securepassword"}`.  
   Returns JWT bearer token in JSON: `{"access_token": "...", "token_type": "bearer"}`.
2. **`POST /api/v1/auth/login/oauth` (Swagger UI / OAuth2 specification flow):**  
   Requires form-urlencoded body conforming to RFC 6749: `username=user@example.com&password=securepassword`.  
   Submitting JSON to this endpoint triggers a `422 Unprocessable Entity` validation error.

The roadmap requires learners to test both endpoints, write negative cases for malformed bodies, and explain this distinction during technical interviews.

---

## 4. Automated Backend Test Baseline

The backend includes a pre-existing 25-test suite (`backend/tests/`) validating multi-tenancy, token generation, Alembic migrations, and data isolation. Learners in the roadmap write their own *external* black-box test suites (Postman, Pytest + Requests, and Playwright) against the running server without modifying the application source code.
