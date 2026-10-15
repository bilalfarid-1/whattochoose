# The 30-Day Zero-Tutorial AI Backend Sprint

A tactical, high-intensity 30-day execution blueprint for computer science and software engineering graduates. This roadmap completely eliminates passive video courses, tutorials, and superficial framework-hopping. Every single hour is active, hands-on, and grounded in our 4 empirical learning protocols.

---

## 1. The Daily Operating Architecture (4 Hours / Day)

Do not spend 8 hours in passive exhaustion. Four focused, high-leverage hours using deliberate practice will yield more progress in 30 days than 6 months of passive video watching.

```
+-----------------------------------------------------------------------------------------+
|                                DAILY 4-HOUR TIME ALLOCATION                             |
+-----------------------------+-----------------------------+-----------------------------+
| Block 1: Hands-On Systems   | Block 2: Fundamental DSA    | Block 3: Verification & Socratic
| (120 Minutes - 50%)         | (60 Minutes - 25%)          | (60 Minutes - 25%)          |
+-----------------------------+-----------------------------+-----------------------------+
| • Protocol 1: Subgoal Build | • Solve 1-2 LeetCode items  | • Protocol 2: Adversarial   |
| • Writing production code   |   using Socratic DSA Coach  |   attack on your code       |
| • Writing PyTest tests      | • Two Pointers, Hash Maps,  | • Protocol 4: Verbal Feynman|
| • Database migrations       |   Binary Search, Trees      |   interrogation / defense   |
+-----------------------------+-----------------------------+-----------------------------+
```

---

## 2. Weekly Milestone Progression

```
Week 1: Relational Modeling & Schema Invariants (PostgreSQL, Async SQLAlchemy 2.0)
   │
   ▼
Week 2: Asynchronous REST Architecture & Defensive Schemas (FastAPI, Pydantic v2)
   │
   ▼
Week 3: Automated Testing & Adversarial Verification (PyTest, httpx, Mocking)
   │
   ▼
Week 4: Productionization, CI/CD, Containerization & Live Deployment (Docker, Render)
```

---

## 3. Day-by-Day Tactical Execution Plan

### WEEK 1: Relational Data Architecture & Database Invariants

#### Day 1: Relational Schema Modeling from Scratch
* **Core Topic:** Relational database normalization (1NF, 2NF, 3NF), primary keys, foreign key cascade options (`ON DELETE CASCADE` vs `SET NULL`).
* **Hands-on Action:** Open a local PostgreSQL database. Design a relational schema for a multi-tenant job application tracking system (Users, Companies, JobApplications, InterviewStages).
* **AI Protocol:** Run Protocol 1 with the Socratic Mentor. Have the AI interrogate your schema normalization.
* **DSA Focus:** LeetCode #1: Two Sum (Hash Map pattern, $O(N)$ time, $O(N)$ space).

#### Day 2: Asynchronous Database Sessions & SQLAlchemy 2.0
* **Core Topic:** Declarative Base, mapped columns (`Mapped[int]`, `Mapped[str]`), async engine creation, connection pooling parameters (`pool_size=10`, `max_overflow=20`).
* **Hands-on Action:** Implement `app/models/` using SQLAlchemy 2.0 async. Write an asynchronous session dependency using `async_sessionmaker`.
* **AI Protocol:** Ask the Socratic Mentor: *"Explain what happens to the connection pool if an unhandled exception occurs before session commit."*
* **DSA Focus:** LeetCode #217: Contains Duplicate (Set lookups).

#### Day 3: Schema Migrations with Alembic
* **Core Topic:** Managing database evolutions, autogenerate vs manual revisions, migration rollback invariants.
* **Hands-on Action:** Initialize Alembic (`alembic init -t async alembic`). Configure `env.py` to recognize your declarative models. Run your first migration `alembic upgrade head`.
* **DSA Focus:** LeetCode #242: Valid Anagram (Frequency count vs sorting).

#### Day 4: Complex Relational Joins & The N+1 Query Problem
* **Core Topic:** Eager loading (`selectinload`, `joinedload`) vs lazy loading in asynchronous SQLAlchemy.
* **Hands-on Action:** Write queries that fetch a User along with all their JobApplications and InterviewStages in a single optimized query.
* **AI Protocol:** Run Protocol 2 (Adversarial Tester): Challenge the AI to point out any hidden $N+1$ query cascades in your queries.
* **DSA Focus:** LeetCode #125: Valid Palindrome (Two Pointers pattern).

#### Day 5: Indexing Strategies & Query Optimization
* **Core Topic:** B-Tree indexes, compound indexes, unique indexes, PostgreSQL `EXPLAIN ANALYZE`.
* **Hands-on Action:** Add appropriate indexes on foreign keys (`user_id`, `company_id`) and status fields. Run `EXPLAIN ANALYZE` on a search query to verify index scan vs sequential table scan.
* **DSA Focus:** LeetCode #167: Two Sum II - Input Array Is Sorted (Two Pointers).

#### Days 6–7: Active Recall Rebuild & Feynman Defense
* **Day 6 (Active Recall):** Delete `app/models/` and re-create your database schema and async session engine from memory in under 30 minutes without looking at documentation.
* **Day 7 (Feynman Interrogation):** Run Protocol 4 with the Architecture Challenger. Defend why you chose PostgreSQL relational tables over a single MongoDB JSON document.

---

### WEEK 2: Asynchronous REST Architecture & Defensive Schemas

#### Day 8: Modern Pydantic v2 Schemas & Data Validation
* **Core Topic:** Strict type validation, custom field validators (`@field_validator`), serialization schemas, and separating Create/Read/Update representations.
* **Hands-on Action:** Build request and response schemas for all entities in `app/schemas/`. Enforce valid email regex, non-empty company names, and salary range bounds.
* **DSA Focus:** LeetCode #20: Valid Parentheses (Stack pattern).

#### Day 9: Asynchronous FastAPI Routing & Dependency Injection
* **Core Topic:** FastAPI path operations, dependency injection (`Depends`), query parameters, pagination envelopes (`page`, `size`, `total`).
* **Hands-on Action:** Implement CRUD endpoints for Companies and Job Applications in `app/api/v1/endpoints/`.
* **AI Protocol:** Socratic Mentor: Discuss the difference between path dependencies and middleware for request validation.
* **DSA Focus:** LeetCode #155: Min Stack (State tracking).

#### Day 10: Cryptographic Authentication (Bcrypt & Password Hashing)
* **Core Topic:** Salting, computational cost factors in bcrypt/Argon2, timing attacks, storing password hashes.
* **Hands-on Action:** Implement `app/core/security.py` using `passlib.context.CryptContext` with bcrypt. Implement user signup and password verification.
* **AI Protocol:** Run Protocol 2 (Adversarial Tester): Ask the AI to identify security vulnerabilities in your password handling.
* **DSA Focus:** LeetCode #704: Binary Search (Array search invariants).

#### Day 11: JWT Token Generation & Refresh Rotation
* **Core Topic:** JSON Web Tokens (Header, Payload, Signature), HMAC-SHA256, access token expiry (15–30 mins), refresh token rotation.
* **Hands-on Action:** Implement JWT creation, decoding, and an authentication dependency (`get_current_user`) that extracts the Bearer token from the `Authorization` header.
* **DSA Focus:** LeetCode #74: Search a 2D Matrix (Matrix binary search).

#### Day 12: Object-Level Authorization (Preventing BOLA / IDOR)
* **Core Topic:** Broken Object-Level Authorization (OWASP Top 10 API #1).
* **Hands-on Action:** Ensure that an authenticated user cannot view, update, or delete an application belonging to another user. Enforce `WHERE user_id = current_user.id` on every query.
* **AI Protocol:** Run Protocol 2 (Adversarial Tester): Challenge the AI to construct a request payload that bypasses your user ID check.
* **DSA Focus:** LeetCode #33: Search in Rotated Sorted Array.

#### Days 13–14: Active Recall & Architecture Interrogation
* **Day 13 (Active Recall):** Create a blank file `auth_scratch.py`. Write a complete JWT issuance and verification system with bcrypt hashing from memory in 20 minutes.
* **Day 14 (Feynman Interrogation):** Run Protocol 4: Defend the security trade-offs of stateless JWTs vs stateful Redis sessions in a live technical interview simulation.

---

### WEEK 3: Automated Testing & Adversarial Verification

#### Day 15: PyTest Foundations & Asynchronous HTTP Client
* **Core Topic:** PyTest fixtures, test discovery, asynchronous test execution (`pytest-asyncio`), `httpx.AsyncClient`.
* **Hands-on Action:** Configure `backend/tests/conftest.py` with an in-memory SQLite database or isolated test PostgreSQL database.
* **DSA Focus:** LeetCode #141: Linked List Cycle (Fast and Slow Pointers).

#### Day 16: Integration Testing for Auth & CRUD
* **Core Topic:** Testing status codes (`201 Created`, `200 OK`, `401 Unauthorized`, `403 Forbidden`, `422 Unprocessable Entity`).
* **Hands-on Action:** Write 6 integration tests covering user registration, valid login, invalid password, duplicate email registration, and protected endpoint access.
* **DSA Focus:** LeetCode #206: Reverse Linked List.

#### Day 17: Database Rollback Invariants in Tests
* **Core Topic:** Ensuring tests are completely isolated and do not pollute the database state between test runs using transactional rollbacks.
* **Hands-on Action:** Implement a PyTest fixture that wraps every test in an isolated transaction and automatically rolls it back on teardown.
* **DSA Focus:** LeetCode #21: Merge Two Sorted Lists.

#### Day 18: Testing Concurrency & Boundary Conditions
* **Core Topic:** Simulating race conditions, boundary pagination (`page=0`, `size=100000`), special character injection.
* **Hands-on Action:** Write 4 defensive tests that pass malicious or extreme payloads and assert that the API rejects them with clean HTTP 422 errors instead of crashing with a 500 error.
* **DSA Focus:** LeetCode #104: Maximum Depth of Binary Tree (Recursion / DFS).

#### Day 19: AI Mutation Testing Sprint
* **Core Topic:** Mutation testing to expose gaps in test coverage.
* **Hands-on Action:** Execute Protocol 3 (Mutation Drill). Have the AI inject 3 subtle bugs into your CRUD logic. Run pytest. If your tests pass without catching the bugs, write new assertions until they catch them.
* **DSA Focus:** LeetCode #226: Invert Binary Tree.

#### Days 20–21: End-to-End Test Suite Hardening
* **Day 20:** Run `pytest -v --cov=app` to measure test coverage. Achieve $\ge 85\%$ test coverage across all routers and CRUD services.
* **Day 21 (Feynman Defense):** Explain the difference between Unit, Integration, and End-to-End tests to the Architecture Challenger. Defend why mocking the database in backend tests can hide critical SQL syntax bugs.

---

### WEEK 4: Productionization, CI/CD, Containerization & Live Deployment

#### Day 22: Dockerizing the Backend
* **Core Topic:** Multi-stage Docker builds, `.dockerignore`, non-root container users, entrypoint scripts.
* **Hands-on Action:** Write a production-ready `Dockerfile` and build the container locally (`docker build -t jobpulse-backend .`). Verify that the container runs and responds to health check requests.
* **DSA Focus:** LeetCode #100: Same Tree (Tree traversal).

#### Day 23: Multi-Container Orchestration with Docker Compose
* **Core Topic:** Service networking, environment variables, PostgreSQL service container, database health-check dependencies (`depends_on: condition: service_healthy`).
* **Hands-on Action:** Write a `docker-compose.yml` that boots up PostgreSQL and FastAPI together with a single `docker compose up --build` command.
* **DSA Focus:** LeetCode #572: Subtree of Another Tree.

#### Day 24: Continuous Integration with GitHub Actions
* **Core Topic:** Automated pipelines on git push, running linters (Ruff/Flake8) and automated test suites in a clean GitHub virtual machine.
* **Hands-on Action:** Create `.github/workflows/ci.yml`. Push a commit to GitHub and watch your test suite execute automatically with a green checkmark.
* **DSA Focus:** LeetCode #235: Lowest Common Ancestor of a Binary Search Tree.

#### Day 25: Live Cloud Deployment (Render / Railway + Hosted PostgreSQL)
* **Core Topic:** Production cloud hosting, managing production environment secrets (`DATABASE_URL`, `SECRET_KEY`), executing migrations on startup.
* **Hands-on Action:** Create a free PostgreSQL database on Neon.tech or Supabase. Deploy your backend to Render.com. Verify that the public Swagger URL (`https://your-app.onrender.com/docs`) is accessible worldwide.
* **DSA Focus:** LeetCode #70: Climbing Stairs (Dynamic Programming / Fibonacci).

#### Day 26: Real-World AI Integration (Structured Summaries)
* **Core Topic:** Calling LLM APIs (OpenAI or Google Gemini) to generate structured resume/job application insights with Pydantic output validation and error fallbacks.
* **Hands-on Action:** Add a `/analyze` endpoint that calls an LLM, parses the response into a validated Pydantic model, and handles rate limits gracefully.
* **DSA Focus:** LeetCode #198: House Robber (1D DP).

#### Days 27–28: Full-Stack Integration & Final Polish
* **Day 27:** Connect the modern Single-Page Application (SPA) dashboard (`frontend/index.html`) to your live deployed backend API. Verify all Kanban board moves, interview logs, and metrics update the live PostgreSQL database.
* **Day 28:** Clean Git history, update the root `README.md` with architectural diagrams, live demo URLs, API documentation, and test execution instructions.

#### Days 29–30: The Capstone Mock Technical Interview & Outreach Sprint
* **Day 29 (Capstone Technical Defense):** Run a 60-minute mock technical interview with the Architecture Challenger prompt. Record your answers. Refine your explanations for every trade-off in your stack.
* **Day 30 (Launch & Outreach):** Send 5 personalized outreach messages to Engineering Managers and Tech Leads at mid-sized software export houses in Lahore, Karachi, or Islamabad using the verified outreach template from our playbook.
