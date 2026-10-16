# The 30-Day Day-by-Day Backend Engineering Roadmap (JobPulse Masterclass)

**Target Audience:** Fresh BS Computer Science / Software Engineering Graduates  
**Primary Goal:** Transition from generalist "tutorial copy-paster" to a verifiable **Junior Backend / Associate Software Engineer** specializing in **Python (FastAPI + PostgreSQL + Pytest)**.  
**Core Training Ground:** **JobPulse** (`backend/app`) — a production-grade, multi-tenant recruitment tracking and analytics API.

---

## The Daily 4-Hour Execution Blueprint

Every single day is divided into a strict, disciplined 4-hour block:
* **Block 1 (120 mins): Hands-on Backend Engineering** on JobPulse (Code, Schema, Routers, Services).
* **Block 2 (45 mins): Data Structures & Algorithms (DSA)** (1 targeted LeetCode problem).
* **Block 3 (35 mins): Testing & Adversarial Edge-Case Audit** (Pytest test suite & boundaries).
* **Block 4 (20 mins): Closed-Book Technical Interview Drill** (Explaining concepts without looking at code).

---

# WEEK 1: Core Relational Architecture & The Request Lifecycle

### Day 1: Modern Python 3.12+ & Clean Project Architecture
* **Concepts:** Python Type Hinting (`str | None`, `Annotated`), Pydantic v2 schemas vs dataclasses, virtual environments (`venv`).
* **JobPulse Task:** Explore `backend/app/main.py` and `backend/app/core/config.py`. Trace how environment variables (`DATABASE_URL`, `SECRET_KEY`) are loaded through `pydantic_settings.BaseSettings`.
* **DSA Drill:** [LeetCode 217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Hash Set vs Sorting time/space trade-offs).
* **Interview Drill of the Day:** *"Why use Pydantic schemas for request validation instead of parsing raw JSON dictionaries?"*
  - *Answer:* Pydantic provides runtime data parsing, automatic serialization, strict type coercion, and auto-generates OpenAPI documentation.
* **Daily Deliverable:** Set up the local Python virtual environment, install requirements, and run the FastAPI development server (`uvicorn app.main:app --reload`).

---

### Day 2: Relational Modeling with PostgreSQL & SQLAlchemy 2.0
* **Concepts:** Relational tables, Primary Keys (`UUID` vs `Integer`), Column constraints (`nullable=False`, `unique=True`, `default`), Declarative Base.
* **JobPulse Task:** Inspect `backend/app/models/application.py` and `backend/app/models/user.py`. Trace how `Base = declarative_base()` maps Python classes directly to PostgreSQL tables.
* **DSA Drill:** [LeetCode 1: Two Sum](https://leetcode.com/problems/two-sum/) (One-pass Hash Map $O(N)$ lookup).
* **Interview Drill of the Day:** *"What is the difference between an auto-incrementing integer primary key and a UUID?"*
  - *Answer:* Auto-incrementing integers are fast and compact (4–8 bytes), but vulnerable to ID enumeration attacks. UUIDs prevent enumeration and allow client-side key generation in distributed systems, but occupy 16 bytes and fragment B-Tree indexes if unsorted.
* **Daily Deliverable:** Write a standalone scratch script that connects to PostgreSQL and creates the raw tables.

---

### Day 3: Relational Foreign Keys, Cascade Deletes & Eager Loading
* **Concepts:** Foreign Key constraints (`ForeignKey("users.id")`), cascading deletions (`ondelete="CASCADE"`), Relationships (`relationship`, `back_populates`), and Lazy vs Eager loading.
* **JobPulse Task:** Trace the relationship between `User` and `JobApplication`. Deliberately test what happens when a User is deleted: does PostgreSQL cascade the delete to their applications, or raise an `IntegrityError`?
* **DSA Drill:** [LeetCode 242: Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Frequency counter using hash maps or fixed-size array).
* **Interview Drill of the Day:** *"What is the N+1 query problem in ORMs, and how do you resolve it in SQLAlchemy?"*
  - *Answer:* The N+1 problem occurs when querying $N$ parent records triggers $N$ secondary queries for child relations. It is solved using eager loading (`joinedload` for one-to-one/many-to-one, or `selectinload` for one-to-many collections).
* **Daily Deliverable:** Verify in PostgreSQL shell (`psql`) that foreign key constraints and cascade rules are physically enforced at the database engine level.

---

### Day 4: Schema Migrations with Alembic
* **Concepts:** Schema version control, migration history, `alembic revision --autogenerate`, `alembic upgrade head`, and migration rollbacks (`alembic downgrade -1`).
* **JobPulse Task:** Inspect `backend/alembic/` and `backend/alembic/versions/`. Run `alembic history`. Create a test migration adding a new column (e.g. `notes: Optional[str]`), apply it, verify the PostgreSQL schema, and then cleanly downgrade it.
* **DSA Drill:** [LeetCode 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Categorization using sorted strings or character frequency tuples as dictionary keys).
* **Interview Drill of the Day:** *"Why is it unacceptable to run `Base.metadata.create_all()` in production?"*
  - *Answer:* `create_all()` only creates missing tables; it cannot modify existing columns, add constraints, or perform data backfills. Migrations provide deterministic, auditable, and rollback-capable schema evolutions.
* **Daily Deliverable:** A successfully executed Alembic migration lifecycle verified in `backend/tests/test_migrations.py`.

---

### Day 5: FastAPI Dependency Injection & Session Lifecycle
* **Concepts:** Asynchronous framework patterns, Dependency Injection (`Depends`), Generator functions (`yield`), Connection Pooling (`pool_size`, `max_overflow`).
* **JobPulse Task:** Inspect `backend/app/core/database.py`. Trace the `get_db()` dependency: understand why `yield db` is enclosed in a `try...finally` block to guarantee database sessions are returned to the pool even during unhandled exceptions.
* **DSA Drill:** [LeetCode 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Hash Map + Bucket Sort or Min-Heap).
* **Interview Drill of the Day:** *"Explain the purpose of FastAPI's `Depends` system."*
  - *Answer:* `Depends` implements Inversion of Control (IoC), decoupling route logic from database connection management, authentication, and service instantiation while ensuring clean resource disposal.
* **Daily Deliverable:** Reconstruct the `get_db` session generator function completely from memory in a blank scratch file.

---

### Day 6: The Full Vertical Slice (Router $\rightarrow$ Service $\rightarrow$ DB)
* **Concepts:** Clean separation of concerns: Pydantic Schemas (Input/Output DTOs), FastAPI Router (HTTP boundaries), Service Layer (Business logic), and SQLAlchemy Model (Persistence).
* **JobPulse Task:** Trace the complete journey of `POST /api/v1/applications`:
  1. Client sends JSON payload $\rightarrow$ 2. Pydantic validates input $\rightarrow$ 3. Auth dependency injects current user $\rightarrow$ 4. Service adds record to DB session $\rightarrow$ 5. Session commits $\rightarrow$ 6. Pydantic serializes response model.
* **DSA Drill:** [LeetCode 128: Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) ($O(N)$ consecutive sequence detection using hash sets).
* **Interview Drill of the Day:** *"Why should database models never be directly returned as API responses?"*
  - *Answer:* Direct model exposure leaks internal schema details (e.g., password hashes, internal foreign keys), creates circular reference serialization bugs, and tightly couples API contracts to database tables.
* **Daily Deliverable:** A newly added endpoint `GET /api/v1/applications/{id}` that validates ID ownership and returns 404 for non-existent records.

---

### Day 7: Week 1 Integration Drill & Closed-Book Defense
* **Concepts:** Cognitive consolidation, spaced repetition, architecture drawing.
* **JobPulse Task:** On a whiteboard or blank paper, draw the complete architectural diagram of JobPulse: Client $\rightarrow$ Router $\rightarrow$ Dependency $\rightarrow$ ORM $\rightarrow$ PostgreSQL. Run `pytest backend/tests/test_applications.py`.
* **DSA Drill:** Review all 6 DSA problems from Week 1. Re-solve LeetCode 1 (Two Sum) and LeetCode 49 (Group Anagrams) in under 15 minutes each.
* **Interview Drill of the Day:** Conduct a 15-minute mock defense: *"Explain the end-to-end lifecycle of an HTTP request in your backend service."*
* **Daily Deliverable:** Complete Week 1 Learning Log entry recording all bugs found and concepts mastered.

---

# WEEK 2: Authentication, Security & Multi-Tenant Isolation

### Day 8: User Registration & Cryptographic Password Hashing
* **Concepts:** Password security, rainbow table attacks, Salt rounds, cryptographic hashing functions (`bcrypt`, `argon2`), why plaintext passwords must never touch the database.
* **JobPulse Task:** Inspect `backend/app/core/security.py` and `backend/app/api/v1/endpoints/auth.py`. Trace `get_password_hash()` and `verify_password()`.
* **DSA Drill:** [LeetCode 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Two-pointer string comparison, alphanumeric filtering).
* **Interview Drill of the Day:** *"Why is SHA-256 unsuitable for password storage, while Bcrypt or Argon2 is required?"*
  - *Answer:* SHA-256 is designed for fast cryptographic throughput (billions of hashes/sec on GPUs), making it vulnerable to brute-force attacks. Bcrypt is deliberately computationally expensive and includes an adaptive cost factor and automatic salting.
* **Daily Deliverable:** Register a test user and inspect the PostgreSQL `users` table to confirm passwords are stored exclusively as 60-character bcrypt hash strings.

---

### Day 9: Stateless Authentication with JWT & OAuth2 Bearer
* **Concepts:** Stateless tokens, JSON Web Tokens (Header, Payload, Signature), `HS256` symmetric signing, token expiration (`exp`), and Bearer headers.
* **JobPulse Task:** Inspect `create_access_token()` in `backend/app/core/security.py`. Trace how the user's `sub` (subject/user_id) is encoded into the token payload and signed using `SECRET_KEY`.
* **DSA Drill:** [LeetCode 167: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Two-pointer technique on sorted array $O(1)$ space).
* **Interview Drill of the Day:** *"What are the trade-offs between stateless JWT authentication and stateful server-side sessions?"*
  - *Answer:* JWTs eliminate server-side session lookups (enabling horizontal scaling without distributed caches), but cannot be easily revoked before expiration without maintaining a token blacklist.
* **Daily Deliverable:** Successfully authenticate via Swagger UI (`/docs`) and verify the Bearer token generation.

---

### Day 10: Auth Middleware & Route Protection
* **Concepts:** HTTP Authorization headers (`Bearer <token>`), token decoding, payload validation, handling `401 Unauthorized` vs `403 Forbidden`.
* **JobPulse Task:** Inspect `get_current_user` in `backend/app/api/deps.py`. Trace what happens when:
  1. No token is provided.
  2. An expired token is provided.
  3. A malformed signature is provided.
* **DSA Drill:** [LeetCode 15: 3Sum](https://leetcode.com/problems/3sum/) (Sorting + Two Pointers, avoiding duplicate triplets).
* **Interview Drill of the Day:** *"What is the exact HTTP distinction between 401 Unauthorized and 403 Forbidden?"*
  - *Answer:* `401 Unauthorized` means authentication is missing or invalid (unauthenticated). `403 Forbidden` means the server knows who the user is, but the user does not have permission to access the resource (unauthorized).
* **Daily Deliverable:** Run `pytest backend/tests/test_auth.py` and confirm all 6 authentication test cases pass.

---

### Day 11: The Multi-Tenant Isolation Barrier (Preventing BOLA / IDOR)
* **Concepts:** Broken Object-Level Authorization (OWASP API Top 10 #1 vulnerability), Multi-tenancy, scoped SQL queries.
* **JobPulse Task:** Open `backend/app/api/v1/endpoints/applications.py`. Analyze how every database query contains `filter(JobApplication.user_id == current_user.id)`. Understand why querying by `id` alone allows User B to steal User A's data.
* **DSA Drill:** [LeetCode 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Greedy two-pointer area maximization).
* **Interview Drill of the Day:** *"How do you architect an API to prevent Broken Object-Level Authorization (BOLA)?"*
  - *Answer:* Never rely on client-supplied entity IDs alone; enforce tenant ownership boundaries at the database query level by filtering against the cryptographically verified `user_id` extracted from the auth session.
* **Daily Deliverable:** Add a negative test case proving that attempting to fetch User A's application with User B's token returns `404 Not Found`.

---

### Day 12: Nested Relational Endpoints & Journal Notes
* **Concepts:** One-to-Many nested relationships, cascading foreign keys, parent-child data validation.
* **JobPulse Task:** Inspect `backend/app/models/application_note.py` and the notes endpoints. Ensure creating a note verifies both:
  1. The parent job application exists.
  2. The parent job application belongs to the requesting user.
* **DSA Drill:** [LeetCode 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Two-pointer boundary tracking).
* **Interview Drill of the Day:** *"How do you handle cascade deletes when deleting a parent record with multiple child collections?"*
  - *Answer:* Configure `cascade="all, delete-orphan"` in SQLAlchemy relationships alongside database-level `ondelete="CASCADE"` foreign key constraints to ensure relational consistency without memory bloat.
* **Daily Deliverable:** Run `pytest backend/tests/test_interviews_and_notes.py` and confirm all note lifecycle tests pass.

---

### Day 13: Adversarial Input Sanitization & Enum Validation
* **Concepts:** Defensive API design, Enum validation (`ApplicationStatus`), length limits, SQL injection prevention via parameterized queries.
* **JobPulse Task:** Attempt to pass invalid payloads to `POST /api/v1/applications`:
  - Pass invalid status: `"status": "CELEBRATING"`.
  - Pass 10,000 characters in company name.
  - Verify that Pydantic intercepts these errors and returns structured `422 Unprocessable Entity` responses before the database is touched.
* **DSA Drill:** [LeetCode 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Stack data structure for bracket matching).
* **Interview Drill of the Day:** *"How does SQLAlchemy protect applications from SQL injection attacks?"*
  - *Answer:* SQLAlchemy uses parameterized queries, treating user input strictly as literal values rather than executable SQL code, preventing malicious query manipulation.
* **Daily Deliverable:** Document 3 edge-case validations in `app/schemas/application.py`.

---

### Day 14: Week 2 Security & Isolation Defense Drill
* **Concepts:** Security review, mutation testing, adversarial mindset.
* **JobPulse Task:** Run the complete security isolation test suite: `pytest backend/tests/test_security_isolation.py`. Deliberately remove `user_id` filtering from one endpoint, observe the test fail, and restore it.
* **DSA Drill:** Review LeetCode 20 (Valid Parentheses) and LeetCode 15 (3Sum). Solve [LeetCode 155: Min Stack](https://leetcode.com/problems/min-stack/).
* **Interview Drill of the Day:** *"If an attacker captures a valid JWT, how can the backend invalidate it before its expiration time?"*
  - *Answer:* By using a token revocation list stored in an in-memory datastore (e.g., Redis) or implementing short-lived access tokens (15 mins) paired with revocable refresh tokens stored in the database.
* **Daily Deliverable:** Complete Week 2 Learning Log entry verifying 100% pass on all security isolation tests.

---

# WEEK 3: Automated Testing Rigor, Optimization & Production Readiness

### Day 15: Pytest Fundamentals & Asynchronous HTTPX Client
* **Concepts:** Automated test runners, test discovery conventions, Pytest fixtures (`@pytest.fixture`), asynchronous test clients (`AsyncClient`).
* **JobPulse Task:** Inspect `backend/tests/conftest.py`. Trace how test fixtures setup clean environments and inject mock tokens into request headers.
* **DSA Drill:** [LeetCode 150: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Stack evaluation of arithmetic expressions).
* **Interview Drill of the Day:** *"Why use integration tests with a real database instead of mocking all database calls?"*
  - *Answer:* Mocking everything tests your assumptions about the database, not actual database behavior. Real database integration tests catch constraint violations, migration bugs, and SQL dialect discrepancies.
* **Daily Deliverable:** Write a new test fixture in `conftest.py` that generates pre-seeded job application records.

---

### Day 16: Ephemeral Test Database Harness
* **Concepts:** Test isolation, ephemeral databases (SQLite in-memory vs dedicated test PostgreSQL), transactions rollback after each test.
* **JobPulse Task:** Trace how `conftest.py` overrides `get_db` using `app.dependency_overrides`. Confirm that tests run in an isolated environment that never touches development or production data.
* **DSA Drill:** [LeetCode 704: Binary Search](https://leetcode.com/problems/binary-search/) (Standard binary search implementation $O(\log N)$).
* **Interview Drill of the Day:** *"How do you guarantee test isolation so Test A never influences the results of Test B?"*
  - *Answer:* By wrapping each test case in a database transaction that rolls back upon test completion, or by creating and dropping a fresh database schema per test session.
* **Daily Deliverable:** Execute `pytest -v backend/tests` and confirm all tests run in under 20 seconds.

---

### Day 17: Writing Comprehensive Integration Tests
* **Concepts:** Happy path testing, edge-case testing, status code verification, schema response verification.
* **JobPulse Task:** Inspect `backend/tests/test_applications.py`. Write 3 new test cases:
  1. Test listing applications with pagination (`limit=5`, `offset=10`).
  2. Test updating an application status from `APPLIED` to `INTERVIEWING`.
  3. Test deleting an application and asserting that related notes are cascade-deleted.
* **DSA Drill:** [LeetCode 74: Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Binary search mapping 2D matrix to 1D index).
* **Interview Drill of the Day:** *"What is the difference between unit tests, integration tests, and end-to-end tests?"*
  - *Answer:* Unit tests verify isolated functions in memory; integration tests verify communication across boundaries (API to Database); end-to-end tests verify complete user journeys across frontend and backend.
* **Daily Deliverable:** A committed test file with 100% pass rate.

---

### Day 18: Security Isolation Test Suite Mastery
* **Concepts:** Multi-user fixture setups (`user_a`, `user_b`), cross-tenant read/write attempts, assertion of 404/403 responses.
* **JobPulse Task:** Study `backend/tests/test_security_isolation.py`. Reconstruct the test `test_user_b_cannot_modify_or_delete_user_a_application` line by line without assistance.
* **DSA Drill:** [LeetCode 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Modified binary search with inflection point).
* **Interview Drill of the Day:** *"Why should a cross-tenant unauthorized request return 404 instead of 403 in certain security contexts?"*
  - *Answer:* Returning 403 confirms to an attacker that the resource exists (ID enumeration). Returning 404 completely hides the existence of the resource from unauthorized actors.
* **Daily Deliverable:** All 6 security isolation tests running and passing cleanly.

---

### Day 19: Database Indexing & Query Optimization
* **Concepts:** B-Tree indexes, Composite indexes, Full-table scans (`Seq Scan` vs `Index Scan`), PostgreSQL `EXPLAIN ANALYZE`.
* **JobPulse Task:** Open PostgreSQL CLI (`psql`). Run `EXPLAIN ANALYZE SELECT * FROM job_applications WHERE user_id = 1;`. Add an index on `user_id` via Alembic and observe the execution plan transition from Sequential Scan to Index Scan.
* **DSA Drill:** [LeetCode 153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Binary search finding pivot).
* **Interview Drill of the Day:** *"When should you NOT add an index to a database column?"*
  - *Answer:* Do not index columns with low cardinality (e.g. booleans), tables with heavy write/insert throughput where index rebalancing creates overhead, or small tables where a sequential scan is faster than index lookup.
* **Daily Deliverable:** Record before-and-after query timing metrics in your daily log.

---

### Day 20: Containerization with Docker & Docker Compose
* **Concepts:** Docker images, layers, Multi-stage builds, Container networks, Port mapping, `docker-compose.yml`.
* **JobPulse Task:** Inspect `backend/Dockerfile` and `backend/docker-compose.yml`. Build the container image: `docker-compose build`. Spin up both FastAPI and PostgreSQL services with `docker-compose up -d`.
* **DSA Drill:** [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Iterative pointer reversal).
* **Interview Drill of the Day:** *"What is the advantage of containerizing an application with Docker?"*
  - *Answer:* Docker eliminates environment discrepancies ("works on my machine"), standardizes dependencies, isolates system processes, and enables identical runtime behavior across development, staging, and production.
* **Daily Deliverable:** JobPulse running cleanly inside Docker containers with PostgreSQL mounted on local persistent volumes.

---

### Day 21: Week 3 Infrastructure & Testing Consolidation
* **Concepts:** Testing suite review, container validation, closed-book recall.
* **JobPulse Task:** Run tests inside the Docker container: `docker-compose run backend pytest backend/tests`. Ensure all 25 tests execute successfully in the containerized environment.
* **DSA Drill:** [LeetCode 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Floyd’s Cycle-Finding Algorithm / Fast & Slow pointers).
* **Interview Drill of the Day:** *"Explain the difference between a process, a thread, and an asynchronous event loop."*
  - *Answer:* A process has independent memory space; threads share process memory and are scheduled by the OS; an event loop runs on a single thread and uses non-blocking I/O multiplexing to handle concurrent requests without thread-switching overhead.
* **Daily Deliverable:** Week 3 Learning Log complete; Dockerized JobPulse verified.

---

# WEEK 4: Analytics Engine, Independent Feature Extension & Job Launch

### Day 22: Building the Funnel Analytics Calculation Engine
* **Concepts:** SQL Aggregations (`COUNT`, `GROUP BY`, `FILTER`), conversion rates, recruitment funnel calculations.
* **JobPulse Task:** Inspect `backend/app/api/v1/endpoints/analytics.py`. Trace how JobPulse computes total applications, interview conversion rates, offer percentages, and rejection distributions.
* **DSA Drill:** [LeetCode 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (Recursive DFS vs iterative BFS).
* **Interview Drill of the Day:** *"How do you handle floating-point division by zero when calculating analytical percentages in Python/SQL?"*
  - *Answer:* In Python, guard with `total > 0 else 0.0`. In SQL, use `NULLIF(denominator, 0)` or `CASE WHEN denominator > 0 THEN ... ELSE 0 END` to prevent database exceptions.
* **Daily Deliverable:** Run `pytest backend/tests/test_analytics.py` and confirm all 3 analytics calculation tests pass.

---

### Day 23: Independent Feature Extension (Part 1: Schema & Migration)
* **Goal:** Demonstrate genuine engineering competence by adding a brand-new feature to JobPulse **without copying code**.
* **Feature Requirement:** Add an `InterviewScorecard` model allowing users to record technical feedback, score (1–10), and interviewer names for each interview stage.
* **JobPulse Task:**
  1. Define the SQLAlchemy model in `backend/app/models/interview_scorecard.py`.
  2. Define Pydantic request/response schemas in `backend/app/schemas/scorecard.py`.
  3. Generate and run an Alembic migration: `alembic revision --autogenerate -m "add interview scorecard"`.
* **DSA Drill:** [LeetCode 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) (Recursive tree traversal).
* **Interview Drill of the Day:** *"How do you version-control database schema changes in a team environment?"*
  - *Answer:* Every schema modification is checked into git as an Alembic migration script; migrations are automatically executed in CI/CD before deploying application binaries.
* **Daily Deliverable:** A valid Alembic migration file applied to your local PostgreSQL database.

---

### Day 24: Independent Feature Extension (Part 2: Routers & Services)
* **JobPulse Task:**
  1. Implement CRUD router endpoints: `POST /api/v1/interviews/{id}/scorecards` and `GET /api/v1/interviews/{id}/scorecards`.
  2. Enforce multi-tenant validation: ensure User B cannot add or read a scorecard on User A's interview.
* **DSA Drill:** [LeetCode 100: Same Tree](https://leetcode.com/problems/same-tree/) (Structural tree equivalence).
* **Interview Drill of the Day:** *"What is the difference between PUT and PATCH in RESTful API design?"*
  - *Answer:* `PUT` completely replaces the target entity (requiring all fields); `PATCH` applies partial modifications to specific fields without overwriting omitted attributes.
* **Daily Deliverable:** Interactive Swagger documentation reflecting the new scorecard endpoints.

---

### Day 25: Independent Feature Extension (Part 3: Pytest Verification)
* **JobPulse Task:** Write dedicated integration tests for your new scorecard feature:
  - Test successful creation and retrieval.
  - Test rejection of invalid scores (e.g. score = 15 when maximum is 10).
  - Test cross-tenant isolation (User B attempting to view User A's scorecard).
* **DSA Drill:** [LeetCode 543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) (Bottom-up depth computation).
* **Interview Drill of the Day:** *"How do you test validation constraints on Pydantic models?"*
  - *Answer:* Pass out-of-range payloads to the endpoint via `AsyncClient` and assert that the response status code is `422 Unprocessable Entity` with specific field error details.
* **Daily Deliverable:** The test suite expands from 25 to 28+ passing tests (`pytest backend/tests`).

---

### Day 26: Continuous Integration (CI) with GitHub Actions
* **Concepts:** Automated linting (Ruff / Flake8), continuous integration workflows, automated test pipelines on pull requests.
* **JobPulse Task:** Inspect or create `.github/workflows/ci.yml`. Configure GitHub Actions to automatically run:
  1. Python dependency installation.
  2. Code linting.
  3. PostgreSQL service container startup.
  4. Full Pytest test suite execution.
* **DSA Drill:** [LeetCode 572: Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) (Tree matching algorithm).
* **Interview Drill of the Day:** *"What is Continuous Integration and why is it essential?"*
  - *Answer:* CI automatically builds, lints, and tests code changes on every commit, preventing broken builds and regressions from reaching the main production branch.
* **Daily Deliverable:** A green passing CI badge on your GitHub repository (`pytest: passing`).

---

### Day 27: Production Cloud Deployment
* **Concepts:** Production hosting (Render, Railway, Fly.io), Managed cloud databases (Neon, Supabase), environment variable management in the cloud.
* **JobPulse Task:** Deploy JobPulse to Render or Railway connected to a free-tier managed PostgreSQL instance. Run migrations on the production database.
* **DSA Drill:** [LeetCode 235: Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Exploiting BST ordering property).
* **Interview Drill of the Day:** *"How do you manage production database connection limits when deploying serverless or multi-worker backend APIs?"*
  - *Answer:* Use connection pooling proxies (e.g. PgBouncer) and configure SQLAlchemy `pool_size` and `max_overflow` to prevent exhausting PostgreSQL's `max_connections` ceiling.
* **Daily Deliverable:** A live public URL hosting JobPulse with interactive Swagger UI (`https://your-jobpulse.onrender.com/docs`).

---

### Day 28: Mock Technical Interview Drill 1 (Databases & Architecture)
* **Exercise:** Conduct a 45-minute timed closed-book mock interview (using the Socratic prompts or with a peer):
  1. *Explain the database schema of JobPulse and why you normalized company and application tables.*
  2. *How do database transactions guarantee data integrity during multi-table writes?*
  3. *How do B-Tree indexes improve query performance, and what is the write-performance cost?*
  4. *What happens if an Alembic migration fails halfway through execution?*
* **DSA Drill:** [LeetCode 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) (Grid DFS/BFS connected components).
* **Daily Deliverable:** Record your verbal answers on voice memo, review them, and eliminate filler words and hesitation.

---

### Day 29: Mock Technical Interview Drill 2 (Security, APIs & Testing)
* **Exercise:** Conduct a 45-minute timed closed-book mock interview:
  1. *How does your API prevent User B from accessing User A's private data? Show the code.*
  2. *Explain the lifecycle of a JWT token from generation to verification.*
  3. *Why did you choose FastAPI over Django or Flask for this project?*
  4. *Walk me through your Pytest test suite: how do you test endpoints without modifying your local database?*
* **DSA Drill:** [LeetCode 133: Clone Graph](https://leetcode.com/problems/clone-graph/) (Graph DFS with hash map cloning).
* **Daily Deliverable:** Confident, concise verbal defense of all 4 questions in under 3 minutes each.

---

### Day 30: GitHub Optimization & The Outreach Campaign
* **JobPulse Task:** Polish the root GitHub README:
  - Add the live Swagger UI link.
  - Embed the Mermaid architecture diagram.
  - List the passing test badge (28+ tests passed).
  - Add setup instructions for Docker Compose.
* **Outreach Execution:** Send 5 targeted messages to Engineering Leads and Tech Recruiters at Pakistani software houses (Arbisoft, Emumba, VentureDive, 10Pearls, Motive) and remote startups:
  > *"Hi [Name], I noticed your team builds high-throughput services at [Company]. I recently engineered JobPulse—a multi-tenant recruitment tracking API built with FastAPI and PostgreSQL, featuring 28 automated integration tests verifying multi-tenant security and Alembic migrations. Here is the live Swagger documentation: [Link] and GitHub repo: [Link]. I’d welcome 5 minutes of your feedback on my schema and test architecture."*
* **DSA Drill:** Final review of the Blind 15 Core Problem Set.
* **Daily Deliverable:** 5 targeted outreach messages sent; live portfolio deployed; full 30-Day Sprint complete!

---

## 4-Metric Progression Scorecard

Use this scorecard at the end of each week to measure genuine engineering growth:

| Metric | Target Standard | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Independent Completion** | Can code schema, routes, and services from memory | [ ] | [ ] | [ ] | [ ] |
| **Debugging Ability** | Can diagnose stack traces and fix failing Pytest fixtures | [ ] | [ ] | [ ] | [ ] |
| **Technical Explanation** | Can verbally articulate architectural trade-offs to senior leads | [ ] | [ ] | [ ] | [ ] |
| **System Verification** | All integration and security tests execute and pass | [ ] | [ ] | [ ] | [ ] |
