# QA / SDET Technical Interview Handbook: Top Questions & Answers (Entry-Level & Junior SDET / Automation QA)

**Target Role:** Junior QA Engineer / Associate SQA / SDET (0–12 Months Experience)  
**Context:** Curated from interview evaluations across tier-1 Pakistani software houses (**Systems Limited, Arbisoft, 10Pearls, Devsinc, Emumba**) and global remote tech employers.

---

## Section 1: Core STLC, Agile & Defect Management

### Q1: What is the exact difference between Verification and Validation?
* **Model Answer:**  
  * **Verification** evaluates work products (specifications, architecture, code) against stated requirements and design constraints: *"Are we building the product right?"* While frequently associated with static analysis (reviews, inspections, linting), verification can also be dynamic (e.g. verifying that an API payload strictly adheres to an OpenAPI schema specification).
  * **Validation** evaluates whether the delivered software satisfies real-world user operational needs and intended business outcomes: *"Are we building the right product?"* This focuses on fitness for purpose in target environments (e.g., end-to-end user workflows, user acceptance testing, exploratory scenario validation).
  *(Avoid the oversimplified trap that verification is strictly static and validation is strictly dynamic; both employ static and dynamic verification techniques.)*

### Q2: What is the difference between Bug Severity and Bug Priority? Give practical examples.
* **Model Answer:**  
  * **Severity** reflects the technical impact of a defect on the system architecture (Critical, Major, Minor, Trivial).  
  * **Priority** reflects the business urgency of fixing the defect (High, Medium, Low).
  * *High Severity, Low Priority:* The application completely crashes when exporting a report on Windows 7. (Severe crash, but Windows 7 users represent <0.1% of clients).
  * *Low Severity, High Priority:* The company CEO's name is misspelled or the corporate logo is inverted on the main login screen. (Zero technical crash, but urgent brand/reputational damage).

### Q3: What do you do when a developer marks your bug report as "Not Reproducible" or "Works on My Machine"?
* **Model Answer:**  
  1. I review my own bug report to ensure I documented exact environment details (browser version, OS, screen resolution, test account role).
  2. I re-attempt reproduction in a clean, isolated environment (incognito window, cleared cache, fresh database user).
  3. If still reproducible, I record a concise screen recording or capture network HAR logs and console stack traces.
  4. I personally approach the developer, schedule a brief 5-minute screen-share, demonstrate the defect on their local build or staging, and help identify the difference in environment configuration or database state.

### Q4: When is testing officially "done"? (Exit Criteria)
* **Model Answer:**  
  Testing is never infinite; it concludes when pre-defined **Exit Criteria** established in the Test Plan are met:
  1. 100% of planned critical and high-priority test cases executed.
  2. Zero open Critical or Blocker defects (all P1/P2 defects resolved and verified).
  3. Pre-agreed code coverage or automated regression test pass thresholds achieved (>95%).
  4. Product Owner / QA Lead formally signs off on the release build.

---

## Section 2: Formal Test Design Techniques

### Q5: Explain Boundary Value Analysis (BVA) and why it is essential.
* **Model Answer:**  
  Boundary Value Analysis is a black-box test design technique based on the empirical observation that software defects cluster heavily at the boundaries of input ranges rather than in the center. For a range $[1, 100]$:
  * **2-Point Boundary Values:** Test the exact boundary and the immediate invalid neighbor: $0, 1$ (lower boundary) and $100, 101$ (upper boundary).
  * **3-Point Boundary Values:** Test $N-1, N, N+1$: $0, 1, 2$ and $99, 100, 101$.
  * *Why essential:* Developers frequently write `<` instead of `<=`, or loop index ranges $0 \dots N$ causing off-by-one errors.

### Q6: How do you design tests using Equivalence Class Partitioning (ECP)?
* **Model Answer:**  
  Equivalence Class Partitioning divides the input domain into classes of data from which all members are presumed to be treated identically by the software. Testing one value from each partition represents the entire class:
  * *Example:* A banking transfer field accepts PKR 100 to PKR 50,000.
    - **Valid Equivalence Class:** Any amount between 100 and 50,000 (e.g., PKR 5,000).
    - **Invalid Class 1 (Below range):** PKR 99 or PKR -10.
    - **Invalid Class 2 (Above range):** PKR 50,001.
    - **Invalid Class 3 (Non-numeric):** `"ten thousand"`, empty string, special characters.

### Q7: What is the difference between Smoke Testing, Sanity Testing, and Regression Testing?
* **Model Answer:**  
  * **Smoke Testing (Build Verification Test):** Broad and shallow. Executed on a brand-new build to verify critical core functionalities are working before accepting the build for testing.
  * **Sanity Testing:** Narrow and deep. Executed on a stable build following a minor bug fix to quickly verify that the specific bug was fixed and immediate adjacent functionality is intact.
  * **Regression Testing:** Comprehensive. Executing previously passed test suites to ensure that recent code modifications or new features have not inadvertently broken existing working capabilities.

---

## Section 3: API Testing & Postman / pytest Automation

### Q8: What makes an HTTP method "Idempotent"? Are methods like PATCH idempotent?
* **Model Answer:**  
  An HTTP method is **idempotent** (RFC 9110) if the intended effect on the server of multiple identical requests is the same as for a single request.
  * **Inherently Idempotent:** `GET`, `HEAD`, `OPTIONS` (safe methods), `PUT` (complete state replacement), `DELETE` (deleting once or multiple times leaves the resource deleted, even if subsequent status codes change from 200/204 to 404).
  * **Non-Idempotent by Default:** `POST` (submitting 5 times creates 5 distinct resource records without an idempotency key).
  * **The PATCH Nuance (RFC 5789):** `PATCH` is **neither inherently non-idempotent nor inherently idempotent**—its idempotency depends entirely on the operation semantics:
    - *Idempotent PATCH:* `{"status": "OFFERED"}` or `{"name": "Alice"}` produces the exact same server state regardless of repetitions.
    - *Non-Idempotent PATCH:* `{"action": "increment_counter", "by": 1}` or JSON Patch `add` operations that append items to a list mutate state on every execution.

### Q9: What is the difference between HTTP Status Codes 401 Unauthorized and 403 Forbidden?
* **Model Answer:**  
  * **401 Unauthorized:** The client has **not authenticated** or the provided credentials (JWT token, API key) are missing, expired, or cryptographically invalid. (Analogy: *"You have no passport."*)
  * **403 Forbidden:** The server **knows who the client is**, but the authenticated identity lacks permission to access the requested resource. (Analogy: *"Your passport is valid, but you are not allowed in the cockpit."*)

### Q10: How do you chain API requests in Postman?
* **Model Answer:**  
  I extract dynamic values from the response of an initial request and store them in environment variables, then reference those variables in subsequent requests:
  1. In the `Tests` tab of the Login endpoint:
     ```javascript
     const jsonData = pm.response.json();
     pm.environment.set("jwt_token", jsonData.access_token);
     ```
  2. In the `Authorization` header of the subsequent `POST /applications` endpoint:
     `Bearer {{jwt_token}}`
  3. In the Tests tab of `POST /applications`:
     ```javascript
     pm.environment.set("application_id", pm.response.json().id);
     ```
  4. In the subsequent request: `GET /applications/{{application_id}}`.

### Q11: What is Broken Object-Level Authorization (BOLA/IDOR), and how do you test for it?
* **Model Answer:**  
  BOLA (OWASP API Security Top 10 #1) occurs when an API endpoint accepts an object ID directly from a client request without verifying that the authenticated user owns that entity.
  * **How I test it:**
    1. Authenticate `User_A` and create a resource (e.g. `Application ID: 45`).
    2. Authenticate `User_B` and obtain `User_B`'s valid JWT token.
    3. Send a request to `GET /applications/45` or `DELETE /applications/45` using `User_B`'s token.
    4. **Pass Criteria:** The API must strictly return `404 Not Found` (or `403 Forbidden`). If it returns `200 OK` or leaks User A's data, a critical BOLA vulnerability exists.

---

## Section 4: Python & Pytest Automation Architecture

### Q12: Explain the purpose and lifecycle of Pytest Fixtures.
* **Model Answer:**  
  Pytest fixtures provide explicit, modular dependency injection for tests, managing setup and teardown lifecycles. Using the `yield` statement:
  ```python
  @pytest.fixture(scope="function")
  def test_db_session():
      db = SessionLocal()  # Setup: Create isolated DB session
      try:
          yield db         # Test runs here
      finally:
          db.rollback()    # Teardown: Rollback changes
          db.close()       # Return connection to pool
  ```
  * `scope="function"` runs per test (ensuring strict isolation).
  * `scope="session"` runs once per entire test suite run (ideal for Docker containers or test server startup).

### Q13: How do you run data-driven tests in Pytest?
* **Model Answer:**  
  Using the `@pytest.mark.parametrize` decorator, which executes the same test function across multiple datasets:
  ```python
  @pytest.mark.parametrize("status, expected_code", [
      ("APPLIED", 200),
      ("INTERVIEWING", 200),
      ("INVALID_STATUS", 422),
      ("", 422),
  ])
  def test_application_status_validation(client, status, expected_code):
      response = client.post("/applications", json={"status": status})
      assert response.status_code == expected_code
  ```

---

## Section 5: Web UI Automation with Playwright

### Q14: Explain the Page Object Model (POM) pattern and its advantages.
* **Model Answer:**  
  The Page Object Model (POM) is an architectural design pattern that abstracts web pages into reusable classes. Each web page has a corresponding class representing locators and user actions; test scripts interact exclusively with the page object methods.
  * **Advantages:**
    - **Maintainability:** If an element's selector changes (e.g. `input#email` becomes `input#user-email`), you update one line in the Page Object class rather than editing 50 separate test scripts.
    - **Readability:** Tests read like business steps (`login_page.login(user, pass); dashboard.verify_welcome()`) rather than messy locator syntax.
    - **Code Reusability:** Common workflows (login, checkout, navigation) are written once.

### Q15: What causes "Flaky Tests" in UI automation, and how do you resolve them?
* **Model Answer:**  
  A flaky test intermittently passes and fails on identical code.
  * **Root Causes:**
    1. Hardcoded sleep delays (`time.sleep(5)`): If network latency exceeds 5 seconds, the test fails.
    2. Shared database state across concurrent tests.
    3. Animations and asynchronous DOM rendering.
  * **Solutions:**
    1. Replace sleep statements with **Explicit Event Waits** or use **Playwright's auto-waiting** mechanisms which automatically wait for element visibility, stability, and clickability before acting.
    2. Enforce test isolation: generate unique test data per test run so tests never collide.
    3. Intercept and mock third-party network requests (e.g. analytics or ad trackers) to eliminate external latency spikes.

---

## Section 6: Database & SQL Testing

### Q16: Why should a QA Engineer test the database directly rather than relying only on the UI or API response?
* **Model Answer:**  
  Relying solely on UI/API responses can mask critical data defects:
  1. An API might return `200 OK` while failing to commit transactions to the database, resulting in data loss.
  2. Data truncation: A user inputs a 500-character description; the UI displays it from local state, but the database column is `VARCHAR(100)` and silently truncated the data.
  3. Orphaned records: Deleting a parent user may fail to delete related application notes if foreign key cascades are missing. Direct SQL assertions (`SELECT COUNT(*) FROM notes WHERE user_id = X`) prove true relational integrity.

### Q17: Write an SQL query to find duplicate emails in a `users` table.
* **Model Answer:**
  ```sql
  SELECT email, COUNT(*) AS count
  FROM users
  GROUP BY email
  HAVING COUNT(*) > 1;
  ```

---

## Section 7: Performance & CI/CD Testing

### Q18: What is the difference between P50, P90, P95, and P99 latency percentiles in load testing?
* **Model Answer:**  
  Averages hide latency spikes. Percentiles reveal the true user experience distribution:
  * **P50 (Median):** 50% of requests were completed faster than this time.
  * **P90:** 90% of requests were completed faster than this time.
  * **P95:** 95% of requests completed faster; the slowest 5% experienced higher latency.
  * **P99:** The critical tail latency: 99% of requests completed faster; 1 out of 100 users experienced this delay. Enterprise SLAs are almost always based on P95 or P99 response times.

### Q19: How do you configure an automated regression test suite to run on every GitHub Pull Request, and how is it enforced?
* **Model Answer:**  
  1. **CI Workflow Definition (`.github/workflows/ci.yml`):**
     - Trigger on `pull_request` to target branches (`main`, `develop`).
     - Spin up isolated service containers (e.g. PostgreSQL).
     - Check out code, install pinned dependencies, start services with readiness checks.
     - Execute the test harness: `pytest` (primary code-based runner) and/or Postman CLI (optional collection runner; note that Postman has transitioned Native Git / Collection v3 workflows from Newman to Postman CLI).
     - Emit exit code `0` on 100% pass, or non-zero on any failure.
     - Publish test reports and trace artifacts (`actions/upload-artifact`).
  2. **Enforcement (Branch Protection & Quality Gates):**
     - *Crucial Distinction:* Merely having a workflow run does NOT automatically prevent merges. Quality gate enforcement requires configuring **Branch Protection Rules** or **Repository Rulesets** in GitHub settings.
     - Mark the test job (e.g. `test-automation`) as a **Required Status Check**.
     - Require branches to be up to date before merging, ensuring the PR cannot be merged if the CI test suite fails.

---

## Section 8: Real-World Edge Cases & Diagnostic Reasoning

### Q20: A requirement says an application status must be valid, but it does not define every allowed transition. How would you test it?
* **Model Answer:**  
  1. **Defect Prevention at Requirements Stage:** Flag that missing transition rules represent a requirements defect. Raise an inquiry with the Product Owner / Business Analyst to define a formal finite state transition matrix.
  2. **Exploratory State Modeling:** Build an $N \times N$ matrix covering all known states (`APPLIED`, `INTERVIEWING`, `OFFERED`, `REJECTED`, `WITHDRAWN`).
  3. **Forward vs. Backward Transitions:** Test intuitive forward progressions (`APPLIED` $\rightarrow$ `INTERVIEWING`) alongside counter-intuitive or destructive backward transitions (`REJECTED` $\rightarrow$ `OFFERED`, or `OFFERED` $\rightarrow$ `APPLIED`).
  4. **Idempotency & Self-Transitions:** Test transitions to the existing state (`APPLIED` $\rightarrow$ `APPLIED`) to verify whether timestamps or audit logs update erroneously.
  5. **Concurrent Transitions:** Fire competing transition requests simultaneously to verify that row-level locking or optimistic concurrency prevents corrupt intermediate states.

### Q21: A defect appears only when a user submits a form twice quickly. How would you investigate it?
* **Model Answer:**  
  This is a classic client-server race condition / double-submission defect (missing UI debouncing or missing server-side idempotency/database transaction isolation).
  * **Reproduction:** Use an asynchronous script (e.g., Python `asyncio` or Locust) firing two identical `POST` requests with the exact same payload within 10 milliseconds.
  * **Database Verification:** Inspect the database to see whether two duplicate rows were created with identical or microsecond-differing timestamps, or whether an unhandled unique constraint error produced a `500 Internal Server Error`.
  * **Defensive Engineering Recommendations:**
    - *Client side:* Immediately disable the submission button upon the first click (debouncing / visual loading state).
    - *Server side (Defense-in-depth):* Require an `Idempotency-Key` (UUID) header cached temporarily in Redis, or enforce a composite unique constraint in PostgreSQL (`user_id`, `company_id`, `job_title`) to gracefully reject duplicate submissions with `409 Conflict`.

### Q22: A low-severity visual defect blocks the primary checkout action. What severity and priority would you assign?
* **Model Answer:**  
  * **Severity:** **Critical / Blocker**  
  * **Priority:** **P1 - Urgent / Blocker**
  * *Reasoning:* Even though the root cause is a visual or CSS defect (e.g., an invisible `z-index` overlay or unstyled translucent banner covering a button), a defect's severity is measured by its **functional impact on the user and system**. Because the primary checkout action is impossible to complete, the entire revenue stream is blocked. It must be triaged as a top-priority blocker.

### Q23: A POST request times out after the server may have committed the record. The client retries. What should happen?
* **Model Answer:**  
  This represents the fundamental network timeout ambiguity in distributed REST APIs.
  * **Unprotected Failure:** The server commits the record, the network drops the response, the client retries, and the server commits a duplicate record or crashes with a database unique violation.
  * **Enterprise Standard:** The API should support client-generated **Idempotency Keys** (`Idempotency-Key: <UUID>`). When the server receives the retry with the existing key, it recognizes that the record was already committed and returns the previously generated `201 Created` or `200 OK` response with the existing resource payload without re-executing business logic.
  * *Fallback:* If idempotency keys are not supported, the database unique constraint should reject the duplicate with `409 Conflict`, allowing the client to query `GET` to confirm whether the record exists.

### Q24: A valid user requests another tenant's resource. Should the API return 403 Forbidden or 404 Not Found?
* **Model Answer:**  
  In multi-tenant architectures, returning **`404 Not Found`** is generally preferred over `403 Forbidden` to prevent **Resource Enumeration and Information Disclosure**.
  * If User B requests `/api/v1/applications/45` (owned by User A), returning `403 Forbidden` confirms that resource #45 actually exists in the system, confirming an attacker's ID guessing attempt.
  * Returning `404 Not Found` indicates that the resource simply does not exist within User B's tenant boundary, denying the attacker any confirmation of existing data.
  * *Exception:* If the application is single-tenant where resource existence is known but role permissions are restricted (e.g. an employee accessing an executive admin payroll URL), `403 Forbidden` is standard.

### Q25: A client submits a JSON body containing user_id or is_admin even though those fields should be server-controlled. What do you test?
* **Model Answer:**  
  This tests for **Mass Assignment / Broken Object Property Level Authorization (OWASP API #3)**.
  * **Test Strategy:**
    1. Send a request to `POST /api/v1/applications/` containing `{"user_id": 999, "company": "Stripe"}` while authenticated as User 1.
    2. Check the database directly via SQL: Assert that the created record is associated with User 1 (from the authenticated JWT session), NOT User 999.
    3. Send `{"is_admin": true}` during registration or user profile update: Verify that the database column remains `is_admin = False`.
    4. Assert that the server either ignores unauthorized fields or strictly rejects them with `422 Unprocessable Entity` (e.g., Pydantic `extra = "forbid"`).

### Q26: Page 2 of an API response contains duplicate records that were on page 1. Is this necessarily a bug?
* **Model Answer:**  
  Not necessarily; this is a known characteristic of **Offset-Based Pagination** (`LIMIT ... OFFSET ...`) operating on a live, mutable dataset (known as **Data Drift**).
  * If Page 1 returns records 1–10, and while the user is viewing Page 1, a new record is inserted at index 0, all records shift down by one. When the client requests Page 2 (`OFFSET 10`), record #10 appears again at index 11.
  * **How to evaluate:**
    - Check if the query has a deterministic `ORDER BY` clause with tie-breakers (`ORDER BY created_at DESC, id DESC`). Missing deterministic ordering IS a bug.
    - If the API uses **Cursor-Based / Keyset Pagination** (`WHERE id < last_seen_id LIMIT 10`), duplicates across pages ARE a defect, as cursors remain stable against concurrent inserts.

### Q27: A Playwright test passes locally but fails in CI. What is your systematic investigation order?
* **Model Answer:**  
  1. **Examine CI Artifacts First:** Inspect the Playwright HTML report, `trace.zip` (trace viewer), video recordings, and failure screenshots to observe what the browser was rendering at the failure point.
  2. **Viewport & Responsive Layout:** CI runners default to specific headless dimensions (e.g. 800x600). Elements visible on a 1080p local screen may be hidden behind hamburger menus or responsive drawers in CI.
  3. **Headless & Timing Differences:** CI virtual machines often have lower CPU allocation. Tests relying on implicit timing or short timeouts fail in CI while passing locally. Always use Playwright's auto-waiting locators rather than arbitrary sleeps.
  4. **Data Isolation:** Check whether the CI database was seeded properly and whether concurrent tests corrupted shared data.
  5. **Network/Font Dependencies:** Check if external web fonts or CDN assets are timing out or blocked in the CI runner environment.

### Q28: Two tests pass independently but fail when run together or in parallel. What could explain this?
* **Model Answer:**  
  This indicates **Test Pollution** and lack of test atomicity.
  * **Shared Mutable Database State:** Test A creates a user with `test@example.com`. When run concurrently or in sequence, Test B fails due to a duplicate email conflict, or Test A deletes data that Test B expected.
  * **Fixture Scope Misconfiguration:** Using `scope="session"` for mutable fixtures instead of `scope="function"`.
  * **Resource/Port Collisions:** Running parallel workers (`pytest -n 4`) against a single server port or shared database file without database isolation.
  * **Global State Mutation:** Modifying environment variables (`os.environ`) or class-level singletons in one test without tearing them down in a `finally` block.

### Q29: The API returns 201 Created, but the SQL query cannot find the new record immediately. What do you investigate?
* **Model Answer:**  
  1. **Uncommitted Database Transaction:** Check if backend code called `db.add()` but omitted `db.commit()`, or if the transaction is pending inside a connection session that hasn't closed.
  2. **Asynchronous Processing (Eventual Consistency):** Check if the API accepts the payload, enqueues it to a message broker (Celery / RabbitMQ / Redis), and returns 201 before a background worker finishes writing to the database.
  3. **Read/Write Replica Lag:** Did the test SQL query connect to a read-replica while the API wrote to the primary master? Asynchronous replication delays can cause reads to lag behind writes.
  4. **Target Schema Discrepancy:** Verify that the test query and the API are connected to the exact same database instance and schema.

### Q30: A delete operation removes a parent record. Should related records always cascade-delete?
* **Model Answer:**  
  No; cascade deletion is a specific business domain choice, not an automatic rule.
  * **CASCADE:** Appropriate when child entities have no independent meaning without the parent (e.g., deleting a `JobApplication` should cascade-delete its `ApplicationNotes` and `InterviewStages`).
  * **RESTRICT (`ON DELETE RESTRICT`):** Mandatory when child records represent legal, financial, or auditing history (e.g., deleting a `Company` must be restricted if active candidate applications or contracts reference it).
  * **SET NULL (`ON DELETE SET NULL`):** Appropriate when child records should persist but lose their association (e.g., deleting a recruiter user account should set `assigned_recruiter_id = NULL` on job applications without deleting the applications).

### Q31: P95 latency improves, but the error rate doubles under load. Is the test a success?
* **Model Answer:**  
  **No; this is a classic performance testing false-positive.**
  * When a server is overwhelmed, it often short-circuits and fails fast with immediate errors (`500 Internal Server Error`, `503 Service Unavailable`, or `504 Gateway Timeout`) within 5 milliseconds without executing database queries or business logic.
  * These fast-failing error responses pull down the response-time percentiles, making P95 latency look lower when the system is actually crashing.
  * *Golden Rule:* Latency metrics are only meaningful for successful transactions. A performance test fails immediately if error rates exceed acceptable thresholds (typically <0.1% or <1%).

### Q32: How would you distinguish a database bottleneck from an application or load-generator bottleneck?
* **Model Answer:**  
  Monitor three independent telemetry layers simultaneously:
  1. **Load Generator (Locust runner):** Inspect runner CPU/RAM. If client CPU is 100%, the generator is saturated and cannot dispatch requests at the target rate.
  2. **Application Server (FastAPI / Uvicorn):** If application CPU is pegged at 100% while database CPU is low, the bottleneck is in application logic (CPU-heavy JSON serialization, unoptimized Python algorithms, insufficient worker processes).
  3. **Database Server (PostgreSQL):** If application CPU is low (waiting on I/O) while PostgreSQL CPU, memory, or disk I/O is saturated and active connections (`pg_stat_activity`) are queued with high wait times, the bottleneck is in the database (missing indexes, missing connection pooling, table locks).

### Q33: Should a flaky test simply be retried until it passes in CI?
* **Model Answer:**  
  **No; automatic retries are a dangerous antipattern when used as a substitute for fixing root causes.**
  * While retry plugins (`pytest-rerunfailures`) can serve as an emergency short-term measure to unblock CI, relying on them has severe consequences:
    1. It conceals real race conditions, memory leaks, and concurrency defects that will manifest in production.
    2. It significantly inflates CI pipeline duration and infrastructure costs.
    3. It produces "alert fatigue" and destroys engineering trust in test suites.
  * *Correct Protocol:* Quarantine the flaky test to an isolated non-blocking suite, log a high-priority defect, reproduce with stress loops (`pytest --count=100`), and fix root causes (deterministic fixtures, auto-waiting locators, independent database state).

### Q34: How do you distinguish an application-level duplicate check from database-enforced uniqueness, and why is this critical in concurrency testing?
* **Model Answer:**  
  * **Application-Level Check:** The server executes `SELECT * FROM users WHERE email = ?`. If `None`, it executes `INSERT INTO users ...`.
    - *The Concurrency Flaw:* Under concurrent traffic, two simultaneous requests execute the `SELECT` check at the same millisecond. Both receive `None`, both proceed to `INSERT`, and duplicate records are committed (a classic Time-of-Check to Time-of-Use / TOCTOU race condition).
  * **Database-Enforced Uniqueness:** An explicit database constraint or unique index (`UNIQUE (email)` or composite `UNIQUE (user_id, company_id)`).
    - Even if concurrent requests pass the application check, the database engine uses atomic transaction locks to commit the first insert and immediately reject the second.
  * *QA Testing Strategy:* In concurrency tests, send simultaneous requests with identical keys. Verify that:
    1. The database strictly prevents duplicates.
    2. The API catches the database `IntegrityError` and returns a clean `409 Conflict` rather than an unhandled `500 Internal Server Error`.

### Q35: How do you systematically distinguish a genuine application defect from a faulty test?
* **Model Answer:**  
  When an automated test fails, never assume the application is broken before validating the test:
  1. **Verify the Oracles & Requirements:** Check the user story, OpenAPI specification, or business requirements document. Did the requirement change, making the test assertion obsolete?
  2. **Isolate the Test Execution:** Run the failing test in isolation (`pytest tests/test_app.py::test_specific -v -s`). If it passes alone, the failure is a test defect caused by shared state pollution or fixture ordering.
  3. **Inspect Request & Database State:** Print the full HTTP request payload, response status, response body, and query the database directly. Is the test sending invalid seed data or missing required foreign keys?
  4. **Manual / cURL Reproduction:** Reproduce the exact request using `curl` or Postman against the local backend. If `curl` succeeds while the automated test fails, the test has a defect (e.g., incorrect header formatting, timing race condition). If `curl` also fails with unexpected state, it is a genuine application defect.


