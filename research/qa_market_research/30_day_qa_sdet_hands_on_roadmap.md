# The 30-Day QA / SDET Hands-on Engineering Roadmap (1-Year Experience Equivalent)

**Target Audience:** Fresh BS Computer Science / Software Engineering Graduates  
**Target Role:** Junior QA Engineer, Associate SQA, or Junior SDET (Software Development Engineer in Test) targeting roles asking for **0 to 6–12 months of experience**.  
**System Under Test (SUT):** **JobPulse API** (`backend/app`) — A live, multi-tenant recruitment tracking service with JWT authentication, relational PostgreSQL database, and 25 passing test suites.

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

### Day 12: Negative API Testing & Security Boundaries (OWASP BOLA)
* **Concepts:** Broken Object-Level Authorization (OWASP API #1), unauthorized access, payload fuzzing, error message information leakage.
* **Hands-on Task:** Author dedicated negative security tests in Postman:
  1. Attempt to fetch User A's application using User B's JWT token (Assert `404 Not Found`).
  2. Attempt to create an application with an expired JWT (Assert `401 Unauthorized`).
  3. Send string values in numeric ID fields (Assert `422 Unprocessable Entity`).
  4. Verify that server stack traces and raw database errors are never leaked in API response bodies.
* **DSA / Logic Drill:** [LeetCode 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/).
* **Interview Drill:** *"What is BOLA / IDOR in API testing, and how does a QA engineer systematically test for it?"*
  - *Answer:* BOLA (Broken Object-Level Authorization) occurs when an API endpoint accepts an object identifier from a client without validating that the authenticated user owns that object. QA tests this by generating two distinct user tokens (User A, User B), capturing User A's resource ID, and submitting requests to modify or read that ID using User B's token.
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

### Day 14: Week 2 API Consolidation & Newman Pipeline
* **Concepts:** Review, headless CI validation, artifact cleanup.
* **Hands-on Task:** Create a single bash/PowerShell script `run_api_tests.ps1` that spins up the JobPulse API, executes Newman, verifies 100% pass, and shuts down the server.
* **DSA / Logic Drill:** [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/).
* **Interview Drill:** Practice explaining your Postman/Newman automation framework out loud in under 3 minutes.
* **Deliverable:** Week 2 Learning Log complete; Newman automated test suite verified.

---

# WEEK 3: Code-Based Automation with Python, Pytest & Playwright

### Day 15: Pytest Fundamentals for QA Engineers
* **Concepts:** Pytest architecture, test discovery (`test_*.py`), fixtures (`@pytest.fixture`), scope (`function`, `module`, `session`), assertions vs. `assert`.
* **Hands-on Task:** Inspect `backend/tests/conftest.py`. Trace how fixtures set up clean database sessions, create test users, and tear down data automatically after each test.
* **DSA / Logic Drill:** [LeetCode 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/).
* **Interview Drill:** *"Why is Pytest preferred over the built-in `unittest` module in modern Python automation?"*
  - *Answer:* Pytest eliminates boilerplate class inheritance, provides powerful and modular dependency injection via fixtures, supports concise plain `assert` statements with detailed introspection, and features an extensive plugin ecosystem.
* **Deliverable:** Write a custom Pytest fixture in a scratch file that generates random test payloads.

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

### Day 18: Security & BOLA/IDOR Automation Suite
* **Concepts:** Automated security verification, testing negative authorization matrixes.
* **Hands-on Task:** Study `backend/tests/test_security_isolation.py`. Build a comprehensive Pytest test file `test_bola_security.py`:
  - Seed `User_A` and `User_B`.
  - Execute read, update, and delete requests on `User_A` records using `User_B` credentials.
  - Assert that all 6 cross-tenant operations strictly return `404 Not Found` or `403 Forbidden`.
* **DSA / Logic Drill:** [LeetCode 543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/).
* **Interview Drill:** *"How do you test for SQL injection and XSS vulnerabilities in an automated API test suite?"*
  - *Answer:* Use parameterized tests (`@pytest.mark.parametrize`) passing standard attack payloads (e.g. `' OR '1'='1`, `<script>alert(1)</script>`) into query parameters and JSON bodies, asserting that inputs are escaped or rejected with 422 errors and never evaluated by the database or rendered unescaped.
* **Deliverable:** A passing 6-test BOLA security isolation suite.

---

### Day 19: Modern Web UI Automation with Playwright (Python)
* **Concepts:** Playwright vs Selenium, auto-waiting, browser contexts, selectors (Role, Text, CSS, XPath), headless vs headed execution.
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

### Day 21: Rich Reporting with Allure & Week 3 Review
* **Concepts:** Test metrics, test execution visualization, Allure Framework (`allure-pytest`).
* **Hands-on Task:**
  1. Install Allure: `pip install allure-pytest`.
  2. Run your combined API and UI tests: `pytest --alluredir=reports/allure_results`.
  3. Generate and view the interactive dashboard displaying pass/fail percentages, test duration, and step-by-step logs.
* **DSA / Logic Drill:** Review binary search and trees.
* **Interview Drill:** Spoken review of Pytest fixtures and Playwright POM architecture.
* **Deliverable:** Week 3 Learning Log complete; Allure dashboard generated.

---

# WEEK 4: Performance, CI/CD, Portfolio Packaging & Interview Launch

### Day 22: Performance & Load Testing with Locust
* **Concepts:** Non-functional testing, Load testing, Stress testing, Requests Per Second (RPS), Latency percentiles (P50, P90, P95, P99), Concurrency.
* **Hands-on Task:**
  1. Install Locust: `pip install locust`.
  2. Create a `locustfile.py` simulating 50 concurrent users querying JobPulse endpoints.
  3. Run Locust: `locust -f locustfile.py`. Open web UI (`http://localhost:8089`), simulate a load spike, and record response times and failure rates.
* **DSA / Logic Drill:** [LeetCode 200: Number of Islands](https://leetcode.com/problems/number-of-islands/).
* **Interview Drill:** *"What is the difference between Load Testing, Stress Testing, and Spike Testing?"*
  - *Answer:* Load testing evaluates system behavior under expected normal user traffic; Stress testing pushes the system beyond its capacity limit to identify breaking points and graceful degradation; Spike testing analyzes how the system recovers from sudden, massive traffic surges.
* **Deliverable:** A committed `locustfile.py` and a screenshot/summary of the load test performance curve.

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
  ├── performance/          # Locust load testing scripts
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
* **Deliverable:** A portfolio README that immediately proves 1-year equivalent hands-on competence to any tech lead.

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

### Day 29: Resume & LinkedIn Optimization (The 1-Year Experience Framing)
* **Hands-on Task:** Rewrite your resume experience section to showcase **verifiable hands-on automation achievements**:
  ```markdown
  ### Quality Assurance & Automation Engineer (SDET Project) — JobPulse Platform
  *Python, Pytest, Playwright, Postman, Newman, PostgreSQL, Docker, GitHub Actions*

  * Designed and executed a comprehensive automated test framework comprising 35+ API, UI, and security test suites with 100% pass rate in CI/CD pipelines.
  * Automated end-to-end API regression test collections in Postman and Newman, integrating pre-request tokens and JSON schema assertions.
  * Built a modular UI test automation suite using Python and Playwright utilizing the Page Object Model (POM) pattern, reducing regression cycle times.
  * Implemented automated security testing covering OWASP API #1 vulnerabilities (Broken Object-Level Authorization), verifying multi-tenant isolation.
  * Conducted load and stress testing using Locust, analyzing latency percentiles (P95/P99) and server throughput under 50 concurrent virtual users.
  * Authored formal STLC documentation including Test Plans, BVA/EP Test Matrices, and Jira-standard defect reports.
  ```
* **Deliverable:** Updated resume and LinkedIn profile reflecting an Automation QA / SDET profile.

---

### Day 30: Targeted Outreach Campaign & Interview Launch
* **Execution:** Send 5 targeted messages to SQA Leads, Engineering Managers, and Tech Recruiters at Pakistani software houses (Systems Limited, Arbisoft, 10Pearls, Devsinc, Emumba) and remote international startups:
  > *"Hi [Name], I noticed your team’s emphasis on automated software quality at [Company]. I recently engineered a full-stack QA automation framework for JobPulse—a multi-tenant recruitment platform. The suite includes 35+ automated integration tests in Pytest, Playwright UI tests using Page Object Model, Newman API pipelines in GitHub Actions, and Locust load benchmarks.  
  > Here is my GitHub repository with passing CI badges and test reports: [Link].  
  > I’d welcome 3 minutes of your candid feedback on my test architecture and assertion strategy. Are you open to sharing your perspective?"*
* **Final Deliverable:** 5 targeted messages sent; complete 30-Day QA/SDET Sprint finished!
