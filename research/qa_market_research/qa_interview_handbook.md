# QA / SDET Technical Interview Handbook: Top Questions & Answers (1-Year Experience Level)

**Target Role:** Junior QA Engineer / Associate SQA / SDET (0–12 Months Experience)  
**Context:** Curated from interview evaluations across tier-1 Pakistani software houses (**Systems Limited, Arbisoft, 10Pearls, Devsinc, Emumba**) and global remote tech employers.

---

## Section 1: Core STLC, Agile & Defect Management

### Q1: What is the exact difference between Verification and Validation?
* **Model Answer:**  
  * **Verification** is static testing performed without executing code to confirm whether work products meet specified requirements: *"Are we building the product right?"* (Examples: code reviews, static code analysis, inspecting requirement documents).
  * **Validation** is dynamic testing performed by executing software to ensure it satisfies user needs and business operational requirements: *"Are we building the right product?"* (Examples: functional testing, integration testing, user acceptance testing).

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

## Section 3: API Testing & Postman / Newman Automation

### Q8: What makes an HTTP method "Idempotent"? Which methods are idempotent?
* **Model Answer:**  
  An HTTP method is **idempotent** if making multiple identical requests has the exact same effect on the server state as making a single request.
  * **Idempotent Methods:** `GET`, `HEAD`, `PUT` (replacing state), `DELETE` (deleting resource once or multiple times leaves it deleted).
  * **Non-Idempotent Methods:** `POST` (submitting 5 times creates 5 separate records), `PATCH` (incremental modifications like `counter += 1` alter state on each call).

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

### Q19: How do you configure an automated regression test suite to run on every GitHub Pull Request?
* **Model Answer:**  
  By creating a GitHub Actions workflow file (`.github/workflows/ci.yml`):
  1. Define the trigger on `pull_request` to the `main` branch.
  2. Set up service containers (e.g. PostgreSQL, Redis).
  3. Check out the code, install dependencies (`pip install -r requirements.txt`).
  4. Run the test command: `pytest --alluredir=allure-results`.
  5. Publish test artifacts. If any test fails, GitHub automatically blocks merging the PR.
