# The 30-Day QA / SDET Hands-on Engineering Roadmap (Verifiable Competency Track)

**Target Audience:** Fresh BS Computer Science / Software Engineering Graduates  
**Target Role:** Associate QA Engineer, Junior SQA, or Junior SDET (Software Development Engineer in Test) targeting roles asking for **0 to 6–12 months of experience**.  
**System Under Test (SUT):** **JobPulse API** (`backend/app`) — A live, multi-tenant recruitment tracking service with JWT authentication, relational PostgreSQL database, and 25 passing test suites.

---

## The 3-Tier Skill Prioritization Framework

To avoid the critical pitfall of learning too many tools superficially, this curriculum prioritizes skills into three clear tiers:

```
+----------------------------------------------------------------------------------------------------+
|                                     CURRICULUM PRIORITIZATION                                      |
+--------------------+-----------------------------------------------+-------------------------------+
| Tier               | Skill Focus                                   | Target Competence Level       |
+--------------------+-----------------------------------------------+-------------------------------+
| **Tier 1: Core**   | • STLC, Test Design (BVA/EP), Bug Reports     | Deep, intuitive fluency;      |
| *(70% of time)*    | • HTTP/REST, Postman API testing, Auth tokens | able to design and execute    |
|                    | • Python, Pytest, Function-scoped Fixtures    | without external assistance.  |
|                    | • SQL joins, Aggregations & DB Data Integrity |                               |
|                    | • Git & basic GitHub Actions CI/CD            |                               |
+--------------------+-----------------------------------------------+-------------------------------+
| **Tier 2: Working**| • Playwright Page Object Model (Python)       | Demonstrable proof-of-work;   |
| *(20% of time)*    | • Newman CLI headless execution               | working test suites integrated|
|                    | • OWASP API Security (BOLA, Mass Assignment)  | into repository.              |
+--------------------+-----------------------------------------------+-------------------------------+
| **Tier 3: Exposure**| • Locust load & latency baseline experiment  | Working conceptual knowledge; |
| *(10% of time)*    | • Single controlled performance experiment    | one well-documented report.   |
+--------------------+-----------------------------------------------+-------------------------------+
```

---

## The Daily 4-Hour Execution Routine

Every single day is structured into a disciplined 4-hour block:
* **Block 1 (120 Mins): Hands-on Automation & Testing** (Postman, Pytest, Playwright, SQL).
* **Block 2 (45 Mins): Test Design & Algorithmic Problem Solving** (Test matrix design + 1 LeetCode problem).
* **Block 3 (35 Mins): Defect Auditing & Edge-Case Interrogation** (Negative testing & boundary analysis).
* **Block 4 (20 Mins): Technical Interview Drill & Spoken Defense** (Verbal defense of QA principles).


---

# WEEK 1: Modern STLC & Test Design Mastery (The Engineering Foundation)

### Day 1: SDLC vs. STLC & Enterprise Test Planning
* **Concepts:** Software Development Life Cycle (SDLC) vs. Software Testing Life Cycle (STLC), Agile Scrum ceremonies (Sprint Planning, Daily Standup, Backlog Refinement, Retrospective).
* **Hands-on Task:** Write a formal **Test Plan Document** for JobPulse (`docs/test_plans/jobpulse_test_plan.md`): Scope, Out of Scope, Test Environment, Resource Allocation, Entry/Exit Criteria, Risks & Mitigation.
* **DSA / Logic Drill:** [LeetCode 217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Hash Set vs Sorting time/space trade-offs).
* **Interview Drill:** *"What is the difference between a Test Plan, a Test Strategy, and a Test Case?"*
  - *Answer:* A Test Strategy is a high-level organizational policy defining test approaches; a Test Plan is a project-specific document detailing scope, schedule, and resources; a Test Case is an executable specification containing pre-conditions, steps, and expected results.
* **Deliverable:** A committed markdown Test Plan for the JobPulse recruitment platform.

---

### Day 2: Boundary Value Analysis (BVA) & Equivalence Partitioning (EP)
* **Concepts:** Black-box test design techniques: 2-point and 3-point Boundary Value Analysis ($N-1, N, N+1$), Equivalence Class Partitioning (valid and invalid classes).
* **Hands-on Task:** Analyze JobPulse Pydantic schemas (`app/schemas/application.py`):
  - Company name length (Min 1, Max 100 characters).
  - Status field (Enum: `APPLIED`, `INTERVIEWING`, `OFFERED`, `REJECTED`).
  - Draft an Equivalence Class and Boundary Value Test Matrix in Markdown identifying valid partitions and invalid injection vectors.
* **DSA / Logic Drill:** [LeetCode 1: Two Sum](https://leetcode.com/problems/two-sum/) ($O(N)$ hash map).
* **Interview Drill:** *"Why do bugs disproportionately cluster at boundary values rather than in the center of equivalence classes?"*
  - *Answer:* Developers frequently make off-by-one errors in conditional logic (`<` instead of `<=`, `>` instead of `>=`), and loop bounds or index ranges typically fail at extreme thresholds.
* **Deliverable:** A completed BVA/EP matrix with at least 12 test conditions.

---

### Day 3: Decision Table & State Transition Testing
* **Concepts:** Complex business logic testing, Combinatorial testing, Finite State Machines (FSM).
* **Hands-on Task:** Map the **State Transition Diagram** for a Job Application:
  - Allowed transitions: `APPLIED` $\rightarrow$ `INTERVIEWING` $\rightarrow$ `OFFERED` or `REJECTED`.
  - Disallowed transitions: `REJECTED` $\rightarrow$ `OFFERED` (without re-opening), or `OFFERED` $\rightarrow$ `APPLIED`.
  - Construct a Decision Table covering combinations of User Roles (Admin vs Regular User), Token Validity (Valid vs Expired), and Resource Ownership.
* **DSA / Logic Drill:** [LeetCode 242: Valid Anagram](https://leetcode.com/problems/valid-anagram/).
* **Interview Drill:** *"How do you test a complex feature with dozens of interdependent input combinations without creating an infinite test suite?"*
  - *Answer:* Use Decision Table testing and Pairwise (Orthogonal Array) testing to systematically maximize combinatorial branch coverage while minimizing redundant test cases.
* **Deliverable:** A State Transition Matrix for JobPulse application statuses.

---

### Day 4: Writing Enterprise-Grade Test Cases
* **Concepts:** Test Case Anatomy: Test ID, Title, Priority (P1–P4), Severity, Pre-conditions, Test Data, Execution Steps, Expected Result, Actual Result, Post-conditions.
* **Hands-on Task:** Write **15 production-grade test cases** for the JobPulse Authentication and Application modules:
  - 5 Happy Path test cases.
  - 7 Negative / Edge-case test cases (SQL injection string, Unicode characters, 10,000-char string, expired token).
  - 3 Security test cases (cross-user access attempts).
* **DSA / Logic Drill:** [LeetCode 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Stack data structure).
* **Interview Drill:** *"What constitutes a good test case?"*
  - *Answer:* A good test case is clear, reproducible by any engineer without ambiguity, independent of other test cases, has a single specific assertion, and includes exact test data and expected outcomes.
* **Deliverable:** A markdown file `jobpulse_test_cases.md` containing all 15 formatted test cases.

---

### Day 5: Professional Defect Lifecycle & Bug Reporting
* **Concepts:** Bug Life Cycle: `New` $\rightarrow$ `Assigned` $\rightarrow$ `Open` $\rightarrow$ `Fixed` $\rightarrow$ `Retest` $\rightarrow$ `Closed` (or `Reopened` / `Deferred`). Severity (Impact on system) vs. Priority (Urgency to business).
* **Hands-on Task:** Deliberately break a feature in JobPulse (e.g. comment out a cascade delete or omit user validation). Author **2 formal Jira-style Bug Reports**:
  - Bug Title: `[Security][Auth] User B can view User A's private notes via direct ID query`
  - Severity: `Critical / Blocker` | Priority: `P1 - High`
  - Environment details, full curl reproduction steps, server stack trace, expected vs actual behavior.
* **DSA / Logic Drill:** [LeetCode 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/).
* **Interview Drill:** *"Give an example of a bug with High Severity but Low Priority, and another with Low Severity but High Priority."*
  - *Answer:* High Severity / Low Priority: The application crashes completely when running on Windows 7 (severe crash, but negligible user base). Low Severity / High Priority: The company logo on the main landing page is misspelled or broken (trivial functional impact, but extreme brand/reputational urgency).
* **Deliverable:** 2 formatted defect markdown files adhering to enterprise Jira standards.

---

### Day 6: Exploratory Testing & Heuristic Cheat Sheets
* **Concepts:** Session-Based Test Management (SBTM), Charter-driven testing, James Bach's Heuristic Test Strategy Model (HTSM).
* **Hands-on Task:** Conduct a 60-minute time-boxed Exploratory Testing session on JobPulse. Test input boundary limits, rapid repeated clicks (race conditions), special characters (`<script>alert(1)</script>`, `' OR 1=1 --`), and session timeouts.
* **DSA / Logic Drill:** [LeetCode 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Floyd's Fast & Slow pointers).
* **Interview Drill:** *"What is the difference between Ad-hoc testing, Monkey testing, and Exploratory testing?"*
  - *Answer:* Ad-hoc testing is unstructured without planning; Monkey testing uses random, senseless inputs without intelligence; Exploratory testing is simultaneous learning, test design, and test execution guided by analytical heuristics.
* **Deliverable:** A completed Exploratory Testing Charter summary logging anomalies found.

---

### Day 7: Week 1 STLC Consolidation & Closed-Book Audit
* **Concepts:** Active recall, test artifact organization.
* **Hands-on Task:** Package your Week 1 deliverables into a clean Git repository folder `qa_artifacts/manual_testing/`. Review all test cases against ISTQB standards.
* **DSA / Logic Drill:** Review Week 1 problems: solve LeetCode 1 and LeetCode 20 from scratch in under 15 minutes each.
* **Interview Drill:** Conduct a 20-minute spoken mock interview: *"Walk me through the STLC phases and explain how QA integrates into a two-week Agile sprint."*
* **Deliverable:** Week 1 Learning Log completed with 100% test artifacts committed to Git.

---

# WEEK 2: Advanced API Testing & Postman Automation

### Day 8: HTTP Protocol Deep-Dive & REST Architecture for QA
* **Concepts:** HTTP request/response anatomy, Idempotence (`GET`, `PUT`, `DELETE` vs `POST`, `PATCH`), HTTP Headers (`Content-Type`, `Authorization`, `Accept`), Status code categories (2xx, 3xx, 4xx, 5xx).
* **Hands-on Task:** Launch JobPulse (`uvicorn app.main:app --reload`). Inspect network traffic using browser DevTools or curl. Send requests to all endpoints and record status codes for both valid and invalid payloads.
* **DSA / Logic Drill:** [LeetCode 704: Binary Search](https://leetcode.com/problems/binary-search/) ($O(\log N)$).
* **Interview Drill:** *"Why should a DELETE request return 204 No Content or 200 OK, and what should happen if you DELETE the same resource twice?"*
  - *Answer:* A successful DELETE returns 204 (no body) or 200. Because DELETE is idempotent in REST, subsequent requests on the same ID should return 404 Not Found (or 204), but must never alter server state further.
* **Deliverable:** An API HTTP Status Code Verification Table for all 12 JobPulse endpoints.

---

### Day 9: Postman Collections, Environments & Variables
* **Concepts:** Postman Workspaces, Collections, Folders, Global vs. Environment vs. Collection variables, Pre-request scripts.
* **Architectural Rule (Postman vs. Pytest):**
  - **Postman:** Use for interactive API exploration, endpoint prototyping, and a concise shareable smoke/regression collection executed via Newman CLI.
  - **Pytest:** Use for deep, maintainable, code-based automation with modular fixtures, parameterized edge cases, and direct database integrity assertions.
  - *Do not build two identical giant test suites across both tools; leverage each for its distinct engineering strength.*
* **Hands-on Task:** Create a Postman Collection: `JobPulse API Test Suite`:
  - Set up an `Localhost` environment variable with `base_url = http://127.0.0.1:8000`.
  - Create a Pre-request script that generates random dynamic user emails using `{{$randomEmail}}` and dynamic company names.
* **DSA / Logic Drill:** [LeetCode 167: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/).
* **Interview Drill:** *"How do you parameterize API tests in Postman to run against Development, Staging, and Production environments without modifying test scripts?"*
  - *Answer:* Use Postman Environment variables (e.g. `{{base_url}}`, `{{auth_token}}`). Swap the active environment file or pass environment JSON files dynamically via Newman in CI/CD.
* **Deliverable:** A clean Postman Collection exported as JSON (`jobpulse_collection.json`).

---

### Day 10: Writing JavaScript Test Assertions in Postman
* **Concepts:** Postman `pm.test()`, Chai assertion library, status verification, JSON response parsing, response time assertions.
* **Hands-on Task:** Write automated assertions in Postman for `POST /api/v1/auth/login`:
  1. `pm.response.to.have.status(200);`
  2. `pm.expect(pm.response.responseTime).to.be.below(500);`
  3. `pm.response.to.have.header("content-type");`
  4. Parse the JWT: `pm.environment.set("token", pm.response.json().access_token);`
* **DSA / Logic Drill:** [LeetCode 15: 3Sum](https://leetcode.com/problems/3sum/).
* **Interview Drill:** *"How do you validate JSON schema compliance in Postman test scripts?"*
  - *Answer:* Use `tv4.validate()` or `ajv` inside `pm.test()`, defining the expected JSON schema structure (required fields, types, formats) and asserting that the response matches the schema.
* **Deliverable:** 8 Postman requests with automated assertions verifying status, response time, and payload structure.

---

### Day 11: End-to-End API Chaining & Dynamic Workflows
* **Concepts:** Workflow chaining: passing IDs and tokens across dependent requests in a simulated user journey.
* **Hands-on Task:** Build an automated end-to-end chain in Postman:
  1. `POST /api/v1/auth/register` $\rightarrow$ Store credentials.
  2. `POST /api/v1/auth/login` $\rightarrow$ Extract JWT token into `{{token}}`.
  3. `POST /api/v1/applications/` $\rightarrow$ Create application, extract `{{app_id}}`.
  4. `POST /api/v1/applications/{{app_id}}/notes` $\rightarrow$ Create note.
  5. `GET /api/v1/applications/{{app_id}}` $\rightarrow$ Verify note is present.
  6. `DELETE /api/v1/applications/{{app_id}}` $\rightarrow$ Assert 200/204.
  7. `GET /api/v1/applications/{{app_id}}` $\rightarrow$ Assert 404 Not Found.
* **DSA / Logic Drill:** [LeetCode 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/).
* **Interview Drill:** *"What is the risk of test dependencies in API chaining, and how do you handle cleanup if step 3 fails?"*
  - *Answer:* Dependent tests can cause cascading failures. Mitigate this by ensuring test scripts clean up their generated state in teardown scripts or by seeding independent test data per collection run.
* **Deliverable:** A completely automated, green-passing 7-step API journey running in Postman Collection Runner.

---

### Day 12: Negative API Testing & OWASP API Security Boundaries
* **Concepts:** OWASP API Security Top 10 (BOLA/IDOR, Mass Assignment, Unrestricted Resource Consumption, Error Information Leakage).
* **Hands-on Task:** Author dedicated negative security tests in Postman:
  1. **BOLA / IDOR:** Attempt to fetch User A's application using User B's JWT token (Assert `404 Not Found`).
  2. **Mass Assignment:** Submit JSON with client-injected protected fields (e.g. `user_id: 999` or `is_admin: true`) to verify the server rejects or ignores them.
  3. **Resource Consumption:** Send extreme pagination parameters (`GET /applications?limit=1000000`) and verify safe bounds handling.
  4. **Authentication Boundary:** Attempt actions with expired, malformed, or missing Bearer tokens (Assert `401 Unauthorized`).
  5. **Data Protection:** Verify that raw database error traces and stack traces are never exposed in response bodies.
* **DSA / Logic Drill:** [LeetCode 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/).
* **Interview Drill:** *"What is Mass Assignment in API security, and how do you test for it?"*
  - *Answer:* Mass assignment occurs when an API binds client-provided JSON directly to data models without filtering out protected attributes. QA tests this by injecting administrative or ownership fields (`is_admin`, `role`, `user_id`) into payload bodies and asserting that the server does not persist the unauthorized fields.
* **Deliverable:** 6 security-focused negative tests integrated into your Postman suite.

---

### Day 13: CLI Automation with Newman & Rich HTML Reporting
* **Concepts:** Postman CLI test runner (`newman`), automated reporting (`newman-reporter-htmlextra`), headless test execution.
* **Hands-on Task:**
  1. Install Newman globally: `npm install -g newman newman-reporter-htmlextra`.
  2. Run the collection from the terminal:
     ```bash
     newman run jobpulse_collection.json -e Localhost.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports/api_test_report.html
     ```
  3. Open and inspect the generated interactive HTML report detailing all passed and failed assertions.
* **DSA / Logic Drill:** [LeetCode 153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/).
* **Interview Drill:** *"How do you integrate Postman collections into a continuous integration (CI) pipeline?"*
  - *Answer:* Export the collection and environment as JSON, install Newman in a CI container (e.g. GitHub Actions), and execute Newman via bash command with JUnit or HTML reporting flags.
* **Deliverable:** A committed `reports/api_test_report.html` file visually documenting 25+ automated API assertions.

---

### Day 14: Week 2 API Consolidation & Rolling Application Launch 1
* **Concepts:** Headless pipeline review + **Rolling Job Market Applications**.
* **Hands-on Task:**
  1. Create a PowerShell runner `run_api_tests.ps1` that spins up JobPulse, executes Newman, verifies 100% pass, and tears down the service.
  2. **Active Market Step:** Do not wait until Day 30 to apply. Begin scanning and submitting applications for **Associate QA Engineer, Trainee QA, or Junior Functional QA** roles on LinkedIn and Rozee.pk. These postings (e.g., Stickler Minds / QA SONIC, Big Entities) prioritize candidates who know STLC fundamentals, write clear bug reports, and understand HTTP/Postman APIs.
* **DSA / Logic Drill:** [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/).
* **Interview Drill:** Practice explaining your Postman/Newman automation framework out loud in under 3 minutes.
* **Deliverable:** Week 2 Learning Log complete; Newman automated test suite verified; initial 3 applications submitted.

---

# WEEK 3: Code-Based Automation with Python, Pytest & Playwright

### Day 15: Pytest Fundamentals & Rigorous Fixture Scoping
* **Concepts:** Pytest architecture, test discovery (`test_*.py`), fixtures (`@pytest.fixture`), fixture scope hierarchy, setup/teardown via `yield`.
* **The Fixture Scoping Standard:**
  - **`scope="function"` (Default):** Mandatory for all mutable test data (creating users, jobs, notes). Guarantees complete test isolation; tests must never fail due to execution order.
  - **`scope="session"`:** Strictly reserved for immutable, expensive resources (e.g., starting an external test server process or loading static configurations). Never use session scope for shared mutable state.
* **Hands-on Task:** Inspect `backend/tests/conftest.py`. Write a dedicated test fixture that provisions a fresh test user, yields the client, and automatically cleans up the user on teardown.
* **DSA / Logic Drill:** [LeetCode 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/).
* **Interview Drill:** *"Why can `scope='session'` fixtures lead to flaky tests, and when should you strictly use `scope='function'`?"*
  - *Answer:* Session-scoped fixtures persist state across all tests. If Test A mutates data created in a session fixture, Test B might fail if executed after Test A but pass when run alone. Function scope ensures each test starts with a clean slate.
* **Deliverable:** A clean test fixture demonstrating `yield` teardown and function-scoped data isolation.

---

### Day 16: Building an Asynchronous API Automation Framework
* **Concepts:** `httpx.AsyncClient`, asynchronous testing (`@pytest.mark.asyncio`), mocking, separating test logic from HTTP client logic.
* **Hands-on Task:** Create a standalone QA automation project directory `tests_automation/`:
  - Build an `ApiClient` class that handles authentication headers, base URLs, and common methods (`get`, `post`, `delete`).
  - Write 5 automated Pytest integration tests calling the running JobPulse service over HTTP.
* **DSA / Logic Drill:** [LeetCode 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/).
* **Interview Drill:** *"What is the difference between synchronous testing with `requests` and asynchronous testing with `httpx`?"*
  - *Answer:* `requests` blocks the thread during network I/O; `httpx` supports non-blocking `async`/`await`, allowing concurrent execution of multiple API calls and direct testing of async ASGI backends (like FastAPI).
* **Deliverable:** A committed `ApiClient` wrapper class and 5 passing Pytest integration tests.

---

### Day 17: Database Verification Testing with SQL
* **Concepts:** White-box and Gray-box testing, backend state validation, verifying that API operations execute correct SQL mutations.
* **Hands-on Task:** Write a Pytest test that:
  1. Calls `POST /api/v1/applications/` via API.
  2. Connects directly to the PostgreSQL database using SQLAlchemy.
  3. Queries `SELECT * FROM job_applications WHERE company = 'Target Corp'`.
  4. Asserts that the database row matches the API response, confirming foreign keys, timestamps, and default values.
* **DSA / Logic Drill:** [LeetCode 100: Same Tree](https://leetcode.com/problems/same-tree/).
* **Interview Drill:** *"Why is API response verification alone insufficient for enterprise software testing?"*
  - *Answer:* An API may return `200 OK` while silently failing to commit transactions to the database, leaving orphaned foreign key records, or truncating data columns. Direct database verification confirms physical persistence and integrity.
* **Deliverable:** A Pytest test script containing direct database assertions alongside HTTP assertions.

---

### Day 18: Security & Controlled Mutation Testing (OWASP BOLA & Mass Assignment)
* **Concepts:** Automated security verification, testing negative authorization matrixes, controlled mutation testing.
* **Hands-on Task:** Study `backend/tests/test_security_isolation.py`. Build a comprehensive Pytest test file `test_security_matrix.py`:
  - Seed `User_A` and `User_B`.
  - Execute read, update, and delete requests on `User_A` records using `User_B` credentials (assert `404 Not Found`).
  - Execute Mass Assignment tests attempting to alter `user_id` or promote accounts via payload tampering.
  - **Controlled Mutation Exercise:** In a local git branch, temporarily comment out the ownership check in `app/crud/application.py`. Run your test suite to confirm it fails immediately (detecting the vulnerability), then revert the branch.
* **DSA / Logic Drill:** [LeetCode 543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/).
* **Interview Drill:** *"What is Controlled Mutation Testing and how does it validate test suite quality?"*
  - *Answer:* Mutation testing involves deliberately introducing a bug into application code to verify whether the test suite detects and fails upon the mutation. A test suite that continues passing despite introduced bugs is ineffective.
* **Deliverable:** A passing 6-test security isolation suite and documentation of the controlled mutation experiment.

---

### Day 19: Modern Web UI Automation with Playwright (Python)
* **Concepts:** Playwright vs Selenium, auto-waiting, browser contexts, selectors (Role, Text, CSS, XPath), headless vs headed execution.
* **UI Scope Transparency:** JobPulse is a backend API service. Rather than falsely claiming a complete consumer web application exists, browser automation targets the live interactive OpenAPI/Swagger UI (`/docs`) or a dedicated minimal single-page HTML test interface, demonstrating real browser interaction (filling credentials, button clicks, DOM assertions) while keeping portfolio claims completely honest.
* **Hands-on Task:**
  1. Install Playwright: `pip install pytest-playwright && playwright install`.
  2. Launch JobPulse Swagger UI in Playwright: `page.goto("http://127.0.0.1:8000/docs")`.
  3. Write a script that automatically clicks the `/auth/login` endpoint accordion, fills in credentials, clicks "Execute", and asserts that the response code is 200.
* **DSA / Logic Drill:** [LeetCode 572: Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/).
* **Interview Drill:** *"Why is Playwright rapidly replacing Selenium in modern tech companies?"*
  - *Answer:* Playwright has built-in auto-waiting (eliminating fragile `sleep()` and explicit waits), runs headless browsers via modern DevTools protocols with native multi-tab/context isolation, intercepts network requests natively, and executes 3–5x faster than WebDriver.
* **Deliverable:** A working Playwright script interacting with the live Swagger UI.

---

### Day 20: The Page Object Model (POM) Design Pattern
* **Concepts:** Design patterns in test automation, Page Object Model (POM), component reusability, test maintainability.
* **Hands-on Task:** Structure your Playwright tests using POM:
  - Create `pages/swagger_page.py` containing element locators and action methods (`expand_endpoint()`, `execute_request()`, `get_response_code()`).
  - Create `tests/test_ui_swagger.py` containing clean assertion logic that calls the page object methods without hardcoded selectors.
* **DSA / Logic Drill:** [LeetCode 235: Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/).
* **Interview Drill:** *"What is the Page Object Model (POM), and what problem does it solve in test automation?"*
  - *Answer:* POM is an architectural pattern that separates web page element locators and interactions into dedicated classes, keeping test files focused purely on assertions. When a UI element changes, you update only one locator in the page object class rather than refactoring dozens of test scripts.
* **Deliverable:** A clean Page Object Model framework in Python with Playwright.

---

### Day 21: Rich Reporting with Allure & Rolling Application Launch 2
* **Concepts:** Test metrics, test execution visualization, Allure Framework (`allure-pytest`) + **Market Application Checkpoint**.
* **Hands-on Task:**
  1. Install Allure: `pip install allure-pytest`.
  2. Run your combined API and UI tests: `pytest --alluredir=reports/allure_results`.
  3. Generate and view the interactive dashboard displaying pass/fail percentages, test duration, and step-by-step logs.
  4. **Active Market Step:** Apply to 5 additional Associate QA / Automation Trainee openings. Candidates presenting both manual test design rigor and clean Python/Pytest suites have a major screening advantage over those with only manual or generic tutorial portfolios.
* **DSA / Logic Drill:** Review binary search and trees.
* **Interview Drill:** Spoken review of Pytest fixtures and Playwright POM architecture.
* **Deliverable:** Week 3 Learning Log complete; Allure dashboard generated; 5 applications tracked.

---

# WEEK 4: Performance, CI/CD, Portfolio Packaging & Interview Launch

### Day 22: Controlled Performance Baseline Experiment with Locust
* **Concepts:** Non-functional testing, Load testing, Requests Per Second (RPS), Latency percentiles (P50, P90, P95, P99), Error Rate vs Throughput.
* **Execution Rule (Controlled Experiment vs. Badge):**
  - *Do not attempt to become a full-scale performance engineer in one day. Focus on conducting one well-controlled, reproducible load experiment.*
  - Distinguish between simulated users, spawn rate, user wait time, and actual backend throughput.
  - Understand the performance paradox: If P95 latency drops while error rates surge, the system is failing fast, not performing well.
* **Hands-on Task:**
  1. Install Locust: `pip install locust`.
  2. Create `performance/locustfile.py` defining a realistic user scenario: login, browse applications with realistic `between(1, 3)` wait times.
  3. Run a controlled 5-minute test with 50 users (spawn rate 5/sec) against local JobPulse.
  4. Document: Baseline latency, peak RPS, error percentage, P50, P95, and P99 response times, and local hardware constraints.
* **DSA / Logic Drill:** [LeetCode 200: Number of Islands](https://leetcode.com/problems/number-of-islands/).
* **Interview Drill:** *"What is the difference between Load Testing, Stress Testing, and Spike Testing?"*
  - *Answer:* Load testing evaluates system behavior under expected normal user traffic; Stress testing pushes the system beyond its capacity limit to identify breaking points and graceful degradation; Spike testing analyzes how the system recovers from sudden, massive traffic surges.
* **Deliverable:** A committed `locustfile.py` and a markdown summary documenting baseline vs. peak percentiles and error rates.

---

### Day 23: Continuous Integration (CI) with GitHub Actions
* **Concepts:** Automated quality gates, CI pipelines, matrix builds, failure notifications.
* **Hands-on Task:** Create `.github/workflows/qa_automation.yml` in your automation repository:
  1. Spin up PostgreSQL and Python 3.12 containers.
  2. Start the JobPulse backend service.
  3. Execute Newman API tests and Pytest integration tests.
  4. Publish the test results and HTML reports as GitHub Action artifacts.
* **DSA / Logic Drill:** [LeetCode 133: Clone Graph](https://leetcode.com/problems/clone-graph/).
* **Interview Drill:** *"What is a 'flaky test' in CI/CD, what causes it, and how do you resolve it?"*
  - *Answer:* A flaky test intermittently passes or fails without code changes. It is typically caused by race conditions, hardcoded timing delays (`sleep`), shared mutable database state across tests, or external network dependencies. Resolve it by using explicit condition waits, isolated test fixtures, and mock boundaries.
* **Deliverable:** A green passing GitHub Actions workflow badge (`QA Tests: Passing`).

---

### Day 24: AI-Augmented QA & Synthetic Data Generation
* **Concepts:** Generative AI in modern SQA, synthetic test data generation, automated contract fuzzing, Playwright CodeGen.
* **Hands-on Task:**
  1. Use an LLM with structured prompts to generate 50 realistic edge-case job applications (including Unicode, emojis, SQL strings, localized Pakistani names).
  2. Build a data-driven Pytest script reading these synthetic records from a JSON file and asserting validation responses.
  3. Use Playwright CodeGen (`playwright codegen`) to record interactive flows and refactor the generated code into clean Page Objects.
* **DSA / Logic Drill:** [LeetCode 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/).
* **Interview Drill:** *"How do you leverage Generative AI in modern Quality Assurance without compromising test accuracy?"*
  - *Answer:* Use AI to generate complex synthetic test datasets, identify overlooked combinatorial edge cases, and scaffold boilerplate Page Objects, while strictly maintaining human review of test assertions and oracle validation.
* **Deliverable:** A data-driven test file executing 50 synthetic test cases.

---

### Day 25: Packaging the QA Automation Portfolio Repository
* **Concepts:** Portfolio proof-of-work, documentation clarity, README engineering.
* **Hands-on Task:** Create and push a dedicated public GitHub repository: `jobpulse-qa-automation-framework`:
  ```
  jobpulse-qa-automation/
  ├── postman/              # Exported Postman collection & environment JSON
  ├── playwright_ui/        # Page Object Model Playwright tests
  ├── pytest_api/           # Pytest API integration tests & security checks
  ├── performance/          # Locust load testing scripts & experiment report
  ├── reports/              # Sample Allure & Newman HTML reports
  ├── .github/workflows/    # CI/CD pipeline running all tests on push
  └── README.md             # Architecture diagram, test metrics & setup guide
  ```
* **DSA / Logic Drill:** Review the Blind 15 problem set.
* **Deliverable:** A clean, organized repository showcasing full-stack QA capabilities.

---

### Day 26: GitHub README Polish & Visual Proof
* **Hands-on Task:** Polish your repository README:
  - Add passing build badges (GitHub Actions CI: Passed).
  - Embed a Mermaid diagram showing the test architecture: `GitHub Actions -> Newman -> Pytest -> Playwright -> PostgreSQL`.
  - Add screenshots of the interactive Allure Dashboard and Locust performance charts.
  - Provide a 1-line command to run the entire suite: `pytest` or `npm run test:api`.
* **DSA / Logic Drill:** Re-solve LeetCode 1 and 217 in under 10 minutes total.
* **Deliverable:** A portfolio README that immediately proves verifiable hands-on competence to any tech lead.

---

### Day 27: Mock Technical Interview 1 (STLC, Test Design & SQL)
* **Exercise:** Conduct a 45-minute timed mock interview covering:
  1. *Walk me through how you design test cases for a new feature from a user story.*
  2. *Explain Boundary Value Analysis and Equivalence Partitioning with real examples.*
  3. *Write an SQL query to find duplicate applications in a table.*
  4. *What do you do if a developer rejects your bug as "not reproducible"?*
* **Deliverable:** Record verbal answers, analyze hesitation, and refine concise technical delivery.

---

### Day 28: Mock Technical Interview 2 (Automation, APIs, Security & Flaky Tests)
* **Exercise:** Conduct a 45-minute timed mock interview covering:
  1. *Explain the architecture of your Pytest and Playwright automation framework.*
  2. *How do you test for Broken Object-Level Authorization (BOLA) in an API?*
  3. *What are Pytest fixtures and how do you manage setup and teardown?*
  4. *How do you diagnose and eliminate flaky tests in a CI/CD pipeline?*
* **Deliverable:** Confident, fluent delivery of all 4 questions in under 3 minutes each.

---

### Day 29: Resume & Profile Optimization (Verifiable Competence Framing)
* **Hands-on Task:** Rewrite your resume experience section to showcase **verifiable hands-on automation achievements and proof of work**:
  ```markdown
  ### Quality Assurance & Test Automation Engineer (Portfolio Project) — JobPulse Platform
  *Python, Pytest, Playwright, Postman, Newman, PostgreSQL, Docker, GitHub Actions, Locust*

  * Architected an end-to-end test automation framework for JobPulse, a multi-tenant recruitment tracking service with 35+ passing integration, UI, and security tests in CI.
  * Authored formal STLC artifacts: Test Plans, Boundary Value & Equivalence Partitioning matrices, and Jira-standard defect reports with cURL repros.
  * Implemented code-based API integration tests in Pytest with isolated fixtures and direct PostgreSQL assertions, verifying database commits and relational cascades.
  * Engineered automated OWASP API security tests validating multi-tenant boundary isolation (BOLA/IDOR) and mass-assignment protection.
  * Built a UI automation test suite using Python and Playwright following the Page Object Model (POM) pattern with auto-waiting locators.
  * Configured GitHub Actions CI/CD workflows executing automated tests on push and publishing interactive Allure & Newman HTML artifacts.
  * Conducted a controlled performance benchmark using Locust, evaluating throughput and P50/P95/P99 latency percentiles under concurrent user load.
  ```
* **Deliverable:** Updated resume and LinkedIn profile reflecting an Automation QA / Junior SDET candidate with verifiable code evidence.

---

### Day 30: Targeted Outreach Campaign & Interview Launch
* **Execution:** Send 5 targeted messages to SQA Leads, Engineering Managers, and Tech Recruiters at Pakistani software houses (Systems Limited, Arbisoft, 10Pearls, Devsinc, Emumba) and remote international startups:
  > *"Hi [Name], I noticed your team’s emphasis on automated software quality at [Company]. I recently engineered a full-stack QA automation framework for JobPulse—a multi-tenant recruitment platform. The suite includes 35+ automated integration tests in Pytest, Playwright UI tests using Page Object Model, Newman API pipelines in GitHub Actions, and Locust load benchmarks.  
  > Here is my GitHub repository with passing CI badges and test reports: [Link].  
  > I’d welcome 3 minutes of your candid feedback on my test architecture and assertion strategy. Are you open to sharing your perspective?"*
* **Final Deliverable:** 5 targeted messages sent; complete 30-Day QA/SDET Sprint finished!

