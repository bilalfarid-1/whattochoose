# 30-Day Job-Ready QA Roadmap

- **Version:** Proposed final learner-facing plan
- **Target:** QA Intern, QA Trainee, Associate QA Engineer, Junior SQA Engineer, Software Tester, Junior QA Automation
- **Region:** Rawalpindi–Islamabad first; suitable Pakistan-wide and remote openings
- **Daily time:** Approximately 4 focused hours
- **Primary portfolio project:** JobPulse (local/authorized test environment)
- **UI practice fallback:** SauceDemo if JobPulse has no stable user-facing workflow

> **What “job-ready” means here:** At the end of this plan, you should be prepared to apply for entry-level QA roles and demonstrate the fundamentals listed below through a small reproducible portfolio. This is a target, not a hiring guarantee, and 30 days of preparation does not equal 30 days or one year of professional experience. Continue applying and improving after Day 30.

---

## 1. The scope: what you will learn first

### Core skills for Days 1–30

1. Manual testing fundamentals, STLC, risk-based test design, exploratory testing and clear bug reports.
2. HTTP/REST basics and practical API testing with Postman.
3. Python fundamentals required for testing, pytest, fixtures, parameterization and meaningful assertions.
4. Practical SQL for reading data and verifying selected data-integrity behavior.
5. Basic authorization testing, including controlled two-user object access checks on JobPulse.
6. A small Playwright Python UI suite using stable locators and web-first assertions.
7. Git/GitHub, a basic GitHub Actions pipeline, report/artifact handling and reproducible documentation.
8. CV, interview practice and a weekly application routine.

### What this plan intentionally does not require

Do not make advanced Locust, Docker, Allure, Selenium, Appium, LLM/AI evaluation, async test architecture or advanced DSA prerequisites for entry-level applications. These can be explored in the Days 31–60 extension or later, based on actual job listings and your progress.

### Use one consistent project structure

Keep the JobPulse application repo separate from the test portfolio, or place the tests in a clearly separated top-level folder if that is simpler. Do not confuse JobPulse's existing in-process backend tests with your new external QA suite that calls a running application over HTTP.

Suggested QA repository:

```text
jobpulse-qa-automation/
├── docs/
│   ├── test-strategy.md
│   ├── test-cases.md
│   ├── test-summary.md
│   └── bugs/
├── postman/
│   ├── jobpulse-collection.json
│   └── environment.example.json
├── tests_api/
├── tests_ui/
├── sql/
├── reports/                 # generated outputs; do not commit sensitive data
├── .github/workflows/
│   └── qa.yml
├── requirements.txt
├── .gitignore
└── README.md
```

This is a suggested structure, not a mandatory design pattern. A smaller structure is acceptable if the README makes it clear and everything can be run.

---

## 2. Four-hour daily routine

Use this structure on full study days:

| Block | Time | Activity |
|---|---:|---|
| Learn | 45 min | Read the named documentation/topic and take brief notes in your own words. |
| Guided practice | 45 min | Try a small exercise before looking at a full solution. |
| Build | 105 min | Work on your own test artifacts or automation project. |
| Explain | 30 min | Explain one testing concept or code decision aloud; practise interview answers. |
| Commit/log | 15 min | Commit work, update the learning log and note the next blocker. |
| **Total** | **240 min** | **4 hours** |

Days 7, 14, 21 and 28 are dedicated consolidation and catch-up days (1–2 focused hours). Use them to address the single highest-impact gap, rerun test suites, and take the remainder of the day off to rest and consolidate concepts, preventing small delays from breaking the monthly schedule. Aim for approximately 108–112 focused hours across the 30-calendar-day period (26 four-hour study days plus four 1–2 hour consolidation days), depending on your pace.

### Working rules

- Write a test idea or first attempt yourself before asking AI for help. Use AI to review reasoning, explain errors and find missing cases; verify every suggested assertion.
- Do not invent bugs to reach a quota. Report genuine defects when found and document unexpected observations separately from known/intended demo behavior.
- Only test systems you own or have explicit permission to test. Run destructive/security experiments against local disposable data, not production.
- Never commit API tokens, `.env` files, real customer data, passwords or private client screenshots.
- If you miss a deliverable, first finish the core milestone. Do not stack every missed optional item onto the following day.
- A test count is a planning target, not evidence of quality by itself.

---

## 3. Week 1 — Fundamentals, test design and baseline (Days 1–7)

### Day 1 — Establish the baseline

**Objective:** Understand what the project currently does and make the environment reproducible.

**Learn:** What testing is; testing vs. debugging; verification vs. validation; defects vs. failures. Begin the ISTQB CTFL syllabus sections on testing fundamentals.

**Build/practice:**
1. Clone/pull the current JobPulse repository.
2. Follow its README to run the application in a local development environment.
3. Run its existing backend tests and record the actual result, including setup failures. Do not simply copy the test count from the README.
4. Inspect the current OpenAPI documentation and frontend. Inventory the actual routes/features that exist today.
5. Create a separate QA repository or clearly separated QA folder and a learning log.

**Deliverable:** `docs/project-baseline.md` with setup steps, application version/commit inspected, test command/results, route/feature inventory, environment issues and SUT decision.

**Done when:** You can run—or clearly document why you cannot yet run—the app and existing tests, and can explain what the current test suite does and does not cover.

**Fallback:** If PostgreSQL or the frontend cannot be started, record the error and first troubleshoot the documented setup. Use a clearly labeled practice site for exercises until the local environment works; do not pretend you tested JobPulse if you did not.

### Day 2 — STLC, test levels, types and risk

**Objective:** Understand a test process and define what is in scope.

**Learn:** STLC, test levels/types, confirmation vs. regression testing, test planning, risk-based prioritization. Use the ISTQB CTFL syllabus as a terminology reference.

**Build/practice:** Write a feature inventory for the actual JobPulse workflows (for example authentication, application records, stage transitions, notes, dashboard/analytics, only where implemented). Define risks, scope in/out, test environment, test data, entry/exit criteria and what a “release recommendation” would be based on.

**Deliverable:** `docs/test-strategy.md` (about 1–2 pages).

**Done when:** You can explain smoke vs. regression, and name the highest-risk user flows in your chosen SUT.

### Day 3 — Equivalence partitioning and boundary values

**Objective:** Design meaningful test cases rather than listing random inputs.

**Learn:** Equivalence partitioning (EP), boundary value analysis (BVA), expected results and test data.

**Build/practice:** Select actual validation rules from the app/API (e.g. required fields, allowed status values, length limits, pagination values). For each rule, identify valid/invalid partitions and boundary values. Do not assume a limit exists until code/schema/docs confirm it.

**Deliverable:** `docs/test-design.md` plus 10–15 test cases with preconditions, steps/data and expected result.

**Done when:** Each case traces to a requirement, route or explicitly labeled assumption.

### Day 4 — Decision tables, state transitions and prioritization

**Objective:** Cover business rules and workflow transitions systematically.

**Learn:** Decision tables, state-transition testing, severity vs. priority and risk-based prioritization.

**Build/practice:** Create a decision table for one real validation/business rule and a state-transition table for an actual JobPulse application/interview status flow. Mark each rule or state transition as implemented, unsupported or awaiting confirmation. Prioritize tests by user/business impact and likelihood.

**Deliverable:** Add 10–15 more test cases to `docs/test-cases.md` or a spreadsheet, reaching a target of about 20–30 thoughtful cases.

**Done when:** You can explain why each high-priority test is important and which requirement/state it covers.

### Day 5 — Bug reports and evidence collection

**Objective:** Create concise, reproducible reports.

**Learn:** Bug lifecycle, severity vs. priority, environment details, exact repro steps, expected vs. actual behavior, evidence and regression tests.

**Build/practice:** Use browser DevTools or `curl` to inspect a request and response. Write a reusable bug-report template. Document any genuine reproducible defects or surprising behaviors found during this week's tests. If no product defect is confirmed, submit evidence-backed observations without mislabeling them as bugs.

**Deliverable:** `docs/bugs/bug-template.md` and at least two completed test-execution records; aim for one or more reproducible bug/observation reports if available.

**Done when:** Another person could follow the steps and understand the expected and actual behavior without asking you to clarify.

### Day 6 — Exploratory testing and SQL introduction

**Objective:** Combine structured test ideas with investigation.

**Learn:** Exploratory testing charters, timeboxing, note-taking; SQL `SELECT`, `WHERE`, sorting, basic joins and aggregates.

**Build/practice:** Run one 45-minute charter-driven session on a JobPulse feature (or SauceDemo if the app is not ready). Record actions, observations, questions and follow-up cases. Complete beginner SQL exercises from SQLBolt and use a small sample schema if the current database setup is unavailable.

**Deliverable:** `docs/exploratory-session-01.md` plus `sql/queries.sql` with explanations of your initial queries.

**Done when:** Your session notes distinguish what you observed from what you infer and propose concrete follow-up tests.

### Day 7 — Weekly review / catch-up

**Objective:** Consolidate Week 1 and repair gaps.

**Tasks:** Review the strategy, test cases and reports. Execute a small selection of the cases. Explain STLC, BVA, EP, severity vs. priority and exploratory testing aloud. Finish one high-impact missing artifact; do not begin new tools.

**Deliverable:** `docs/week-1-review.md` listing completed items, gaps, real findings and three topics to revisit.

**Done when:** Your artifacts are readable and committed, or remaining blockers are clearly recorded with a plan.

---

## 4. Week 2 — HTTP, Postman and API test design (Days 8–14)

### Day 8 — HTTP and API route inventory

**Objective:** Understand the application contract before testing endpoints.

**Learn:** Request/response anatomy, methods, headers, status-code families, JSON and REST basics.

**Build/practice:** Confirm actual JobPulse paths and schemas from its live local OpenAPI output/source. The JobPulse backend exposes **20 business API operations across 13 unique business path templates**, plus 1 auto-generated documentation schema route (`GET /api/v1/openapi.json`), totaling 21 routable endpoints under `/api/v1`:
- **Auth (4 ops):** `POST /api/v1/auth/register`, `POST /api/v1/auth/login`, `POST /api/v1/auth/login/oauth`, `GET /api/v1/auth/me`
- **Companies (3 ops):** `GET /api/v1/companies/`, `POST /api/v1/companies/`, `GET /api/v1/companies/{company_id}`
- **Applications (5 ops):** `GET /api/v1/applications/`, `POST /api/v1/applications/`, `GET /api/v1/applications/{application_id}`, `PATCH /api/v1/applications/{application_id}`, `DELETE /api/v1/applications/{application_id}`
- **Interviews (4 ops):** `GET /api/v1/applications/{application_id}/interviews`, `POST /api/v1/applications/{application_id}/interviews`, `PATCH /api/v1/interviews/{interview_id}`, `DELETE /api/v1/interviews/{interview_id}`
- **Notes (3 ops):** `GET /api/v1/applications/{application_id}/notes`, `POST /api/v1/applications/{application_id}/notes`, `DELETE /api/v1/notes/{note_id}`
- **Analytics (1 op):** `GET /api/v1/analytics/`

Note the crucial authentication contract difference: `POST /api/v1/auth/login` expects a JSON body (`UserLogin` model with `email`, `password`), whereas `POST /api/v1/auth/login/oauth` expects `application/x-www-form-urlencoded` form data (`username`, `password`) used by Swagger UI. Distinguish JobPulse as your primary HTTP API SUT from SauceDemo as the labeled UI fallback.

**Deliverable:** `docs/api-inventory.md`.

**Done when:** You can describe a request and response for the most important routes without guessing.

### Day 9 — Status codes, auth and idempotency

**Objective:** Design expectations for both successful and unsuccessful requests.

**Learn:** 2xx/3xx/4xx/5xx, `401` vs. `403` vs. `404`, bearer/JWT basics, and the meaning of idempotency under HTTP semantics.

**Build/practice:** Test read-only routes unauthenticated and authenticated. Record the actual API contract. Explain that idempotency concerns intended state effects; repeated requests need not return identical codes.

**Deliverable:** Add an expected/actual HTTP behavior table to `docs/api-inventory.md`.

**Done when:** Your expectations are supported by the API's policy/schema or explicitly marked as a proposed expectation.

### Day 10 — Postman collection and variables

**Objective:** Build a shareable API exploration artifact.

**Learn:** Requests, collections, environment variables, authorization settings and post-response assertions in Postman.

**Build/practice:** Create a collection for a small set of actual JobPulse endpoints. Use a local base URL and placeholders for credentials. Add meaningful assertions on status, response fields and expected values.

**Deliverable:** `postman/jobpulse-collection.json` plus `postman/environment.example.json` and a README explaining how to set local variables without exposing secrets.

**Done when:** Another person can import the collection and understand how to configure it safely.

### Day 11 — Positive API flows

**Objective:** Verify primary supported behavior through HTTP.

**Learn:** Setup/test-data flow, positive/negative testing, response contract and state verification.

**Build/practice:** Cover the main implemented workflow, such as authenticating, creating an application, reading/listing it and updating supported fields. Use unique test data and clean up where possible. Do not mutate real users' data.

**Deliverable:** A collection with a small end-to-end request flow and recorded execution evidence.

**Done when:** The flow is repeatable from a clean test setup or any non-repeatability is documented.

### Day 12 — Negative and validation testing

**Objective:** Verify controlled failure cases.

**Learn:** Missing/invalid fields, incorrect data types, malformed requests, absent/invalid credentials and expected error messages.

**Build/practice:** Add tests only for rules supported by the actual API/schema. Record unexpected behavior, including whether validation errors have stable status codes and useful messages. Do not declare an undocumented rule a defect without stating the assumption.

**Deliverable:** At least 8–12 meaningful API cases in the collection across positive and negative paths; more are fine if quality is maintained.

**Done when:** Each assertion has a reason and the expected outcome is explained in the README.

### Day 13 — Collection review and API report

**Objective:** Make the exploratory collection clear and useful to another tester.

**Learn:** Collection Runner, collection organization and test evidence.

**Build/practice:** Run the collection from a clean session, fix misleading assertions and remove credentials. Create a short report showing tested routes, true pass/fail/error counts, untested routes and limitations. Do not make Newman mandatory; its current maintenance/collection-format limitations are documented by Postman. Use pytest for the primary code-based automation later.

**Deliverable:** `postman/README.md` and `docs/api-test-report-v1.md`.

**Done when:** A reviewer can see exactly what was tested and what remains unknown.

### Day 14 — Review, applications and interview checkpoint

**Objective:** Test your own understanding and start the application funnel.

**Tasks:** Explain HTTP methods, 401 vs. 403, positive/negative testing, and one Postman assertion. Fix the three biggest gaps. Prepare a one-page CV draft and tracker. Submit 2–5 tailored applications if your CV and initial proof-of-work are honest and ready; don't wait until Day 30 to apply.

**Deliverable:** `docs/week-2-review.md`, CV draft and job-tracker sheet.

**Done when:** At least a small batch of genuinely relevant applications is tracked, or the exact blocker preventing applications is identified.

---

## 5. Week 3 — Python/pytest, SQL and authorization (Days 15–21)

### Day 15 — Python for API tests

**Objective:** Write understandable code for testing.

**Learn:** Virtual environments, modules, dictionaries/lists, functions, exceptions, JSON responses and `requests` basics.

**Build/practice:** Create the external automation test project and run one request against the local JobPulse API. Use a timeout, check the status and inspect JSON in a useful failure message.

**Deliverable:** `tests_api/test_smoke.py` and `requirements.txt`.

**Done when:** The environment setup and one test work from the documented command; record any external service/environment prerequisites.

### Day 16 — pytest fundamentals and assertions

**Objective:** Convert API expectations into executable tests.

**Learn:** Test discovery, assertion patterns, setup, failing tests and reading test output.

**Build/practice:** Write a small suite against read-only or low-risk routes. Add tests for valid authentication and one invalid case. Keep the tests clear instead of creating a framework abstraction too early.

**Deliverable:** About 4–6 initial API tests.

**Done when:** You can deliberately break one assertion, interpret the failure, restore it and explain why the test is useful.

### Day 17 — Fixtures and test data cleanup

**Objective:** Prevent tests from depending on execution order.

**Learn:** pytest fixtures, `yield` teardown where appropriate, function scope and fixture reuse in `conftest.py`.

**Build/practice:** Add fixtures for base URL, test authentication and any test data actually required. Prefer function-scoped mutable data. Create unique records and clean up safely. If the API lacks test reset/cleanup support, document the limitation and use a disposable test database.

**Deliverable:** `tests_api/conftest.py` plus a note describing isolation and cleanup.

**Done when:** A test can run alone and in the suite without relying on a previous test's side effects.

### Day 18 — Parameterization and reliable negative tests

**Objective:** Cover input variations without copy-pasting tests.

**Learn:** `pytest.mark.parametrize`, reusable test data, timeouts and clean error assertions.

**Build/practice:** Parameterize a set of valid/invalid payloads based on real schema constraints. Add clear IDs/labels for cases and ensure invalid input doesn't leak a traceback or inconsistent internal response.

**Deliverable:** A suite of roughly 8–12 API tests, including parameterized cases.

**Done when:** Each case reports which input failed and why; no arbitrary response-time threshold is used as a functional assertion.

### Day 19 — Practical SQL and database verification

**Objective:** Verify a few important persisted changes.

**Learn:** `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, aggregates, `NULL`, primary/foreign keys and uniqueness at an introductory level.

**Build/practice:** Use an isolated test database. Trigger an API operation and verify only the relevant persisted fact, preferably by a unique test identifier. Record the query and why the check provides value beyond the API response. Explain whether the API is a separate process and how cleanup is performed.

**Deliverable:** `sql/queries.sql` with 5–8 explained queries and 1–3 selective persistence checks if the environment permits.

**Done when:** You can explain what each query proves and why it cannot accidentally match an unrelated user's record.

### Day 20 — Multi-user authorization / BOLA fundamentals

**Objective:** Verify that one user cannot access another user's private resource.

**Learn:** Authentication vs. authorization; object-level authorization; object-property authorization; safe testing practices.

**Build/practice:** In a local/authorized test environment, create two test users (A and B) and distinct resources. Attempt to read, update and delete A's resource as B using the actual supported routes. Check ownership-sensitive fields if the models/schemas allow them. The current JobPulse policy may return `404` to conceal resource existence, but confirm its implementation/policy before asserting it. Never run these checks against a public third-party target.

**Deliverable:** `docs/security-test-cases.md` and `tests_api/test_authorization.py` with the supported cases.

**Done when:** The tests prove that cross-user access is denied for the tested operations or clearly document a reproduced defect.

### Day 21 — Consolidation and application checkpoint

**Objective:** Stabilize the API automation suite.

**Tasks:** Run tests in different orders; fix order dependence and vague assertions. Confirm test data cleanup, review SQL and authorization tests, update the README and report. Review applications and submit another small batch of suitable roles.

**Deliverable:** A reproducible API suite, true test report, updated CV and `docs/week-3-review.md`.

**Done when:** The API suite is runnable from the README and known failing/unsupported scenarios are documented honestly.

---

## 6. Week 4 & Final Assessment — Playwright, CI, Portfolio and Mock Interview (Days 22–30)

### Part A: Week 4 Core — UI Automation, CI & Security Audit (Days 22–28)

### Day 22 — Select a real UI target and install Playwright

**Objective:** Set up one browser automation framework.

**Learn:** Playwright Python installation, pytest plugin usage and the idea of a UI smoke test.

**Build/practice:** Inspect JobPulse's actual frontend and pick one meaningful, stable user flow. If no such flow is ready, use SauceDemo and label it accurately. Install `pytest-playwright`, install browser binaries and run the official example.

**Deliverable:** `tests_ui/README.md` and one passing smoke test.

**Done when:** You can run the test headed and headless and explain which application it tests.

### Day 23 — Locators and web-first assertions

**Objective:** Write UI tests that wait for observable conditions.

**Learn:** Role/text/test-id locators, assertions and built-in auto-waiting.

**Build/practice:** Replace fragile selectors or fixed sleeps in the initial test. Add one assertion for a visible, user-relevant outcome. Keep the test isolated from prior test state.

**Deliverable:** Two or three stable UI smoke tests.

**Done when:** The test waits for a condition rather than using `time.sleep` as its normal synchronization mechanism.

### Day 24 — A small critical-flow UI suite

**Objective:** Automate only a few valuable user workflows.

**Build/practice:** Choose implemented flows only—for example login/error state, viewing the authenticated dashboard and creating/listing a record if that feature exists. If using SauceDemo, cover login, inventory/cart and a checkout validation. Keep credentials/test data non-sensitive.

**Deliverable:** Target of 4–6 UI tests and a short statement of what is intentionally not automated.

**Done when:** Every test has a meaningful assertion and a clear purpose; the count is not increased using duplicate or trivial tests.

### Day 25 — Debugging and failure evidence

**Objective:** Make failures explainable.

**Learn:** Playwright traces, screenshots, locator debugging and flaky-test causes.

**Build/practice:** Capture a trace/screenshot on failure if straightforward. Break a locator intentionally in a local branch and read the failure output, then restore it. Run the suite repeatedly and investigate genuine intermittent failures; document environment failures separately.

**Deliverable:** `docs/ui-test-debugging.md` and retained-on-failure artifacts if configured.

**Done when:** You can demonstrate how to investigate a failed test and do not hide failures with blind retries.

### Day 26 — Basic GitHub Actions CI

**Objective:** Run a deterministic automated suite automatically.

**Learn:** Workflows, triggers, jobs/steps, dependencies, environment variables, secrets and artifacts.

**Build/practice:** Add a GitHub Actions workflow that runs the API smoke suite on push/pull request. Configure required dependencies and a test database or documented test configuration. Upload test results/logs if practical. Add UI tests to CI only after the API workflow is stable and browser setup is configured correctly.

**Deliverable:** `.github/workflows/qa.yml` plus instructions to run the same tests locally.

**Done when:** The workflow has actually run successfully on your repository and fails when a test fails. Do not add a fake or manually asserted green badge.

### Day 27 — Documentation, test report and secrets audit

**Objective:** Make the portfolio understandable in under a minute.

**Build/practice:** Polish README with purpose, application-under-test, setup, test commands, tools, tested routes/flows, what is covered/not covered, real findings and limitations. Check `.gitignore` and repository history for accidental secrets. Do not include private customer data.

**Deliverable:** Updated README, test summary and clean repository.

**Done when:** A reviewer can follow the setup steps and understand the evidence without personal explanation.

### Day 28 — Light review / catch-up day

**Objective:** Repair the highest-impact gap before final assessment.

**Tasks:** Use a closed-book quiz or mock exercise on testing fundamentals, API status codes, pytest fixtures, SQL joins, BOLA and flaky-test handling. Choose no more than three gaps to fix. If CI or the environment is broken, prioritize reproducibility over new features.

**Deliverable:** `docs/week-4-review.md` plus a written list of remaining limitations.

**Done when:** You can explain your core portfolio choices without relying on copied answers.

### Part B: Final Assessment & Application Launch (Days 29–30)

### Day 29 — CV, portfolio walkthrough and job applications

**Objective:** Present only verifiable evidence.

**Build/practice:** Create a one-page CV tailored to entry-level QA/SQA/automation roles. Include the project, tools and measurable results only when they have been run and confirmed. Prepare a 60–90 second project pitch and a 3-minute walkthrough of the framework. Review job advertisements and submit a small, tailored batch.

**Deliverable:** `CV_QA.pdf` or an editable CV source, job tracker, and `docs/project-walkthrough.md`.

**Done when:** Every technical claim can be backed by a repository artifact or a clear explanation.

### Day 30 — Final audit and mock interview

**Objective:** Check whether you're ready to apply and identify the next steps.

**Mock topics:**
- STLC, test levels, smoke vs. regression, BVA/EP and risk-based prioritization.
- Severity vs. priority and how to write a reproducible bug.
- HTTP methods, `401` vs. `403` vs. `404`, request assertions and idempotency.
- pytest fixtures, parameterization, test cleanup and flaky tests.
- SQL `JOIN`/aggregates and how one database check was designed.
- BOLA using two users; scope and limitations of the security checks.
- Playwright locators, web-first assertions and interpreting a failed CI run.
- What is automated, what remains manual and why.

**Deliverable:** `docs/day-30-readiness-review.md` with completed evidence, missing topics, honest results from one mock interview and a Days 31–60 priority list.

**Done when:** You can demo the portfolio from a clean setup, answer the core questions at a beginner level and describe your next gaps without overstating competence.

---

## 7. Portfolio targets by Day 30

These are approximate targets. Correct, reproducible tests matter more than hitting every number.

| Artifact | Minimum useful outcome | Stretch target |
|---|---|---|
| Test strategy and test design | One strategy, 20–30 meaningful cases | Traceability matrix, risk ratings and 30–40 cases |
| Bug/exploratory records | Repeatable test executions and evidence-backed findings | Several genuine defects, if found, with regression cases |
| Postman | Shareable collection with variables and assertions | Organized smoke/regression folders and report |
| pytest API suite | A small passing suite with assertions, fixture and cleanup | Roughly 15–25 useful tests including negative paths |
| SQL | 5–8 explained queries | Selective DB integrity checks with isolated data |
| Authorization | Two-user test plan and implemented supported tests | Read/update/delete plus property-level checks where routes allow |
| Playwright | 2–4 stable UI tests | Roughly 5–8 tests with failure trace/screenshot |
| CI | One actually passing API test workflow | API and UI workflows with reports/artifacts |
| Career work | One honest CV, tracker and mock interview | More tailored applications and peer feedback |

Do not report a goal as completed until the artifact exists and has been checked. Do not describe existing JobPulse tests as new QA tests unless the new suite actually exists.

---

## 8. Job-search system during the 30 days

- Start reviewing real listings immediately. Start applying during Week 2 when you have basic evidence, rather than waiting for Day 30.
- Target QA Intern, QA Trainee, Associate QA Engineer, Junior SQA Engineer, Software Tester and Junior QA Automation titles. Apply to SDET roles when their requirements fit your evidence.
- Aim for about 5–8 tailored, relevant applications per week once the basics are ready. Quality matters more than meeting an arbitrary application quota.
- Record company, title, location, posting URL/date, required experience, required skills, date applied, status and next action.
- Tailor the CV honestly to each listing. Do not copy a job's keyword into your skills section unless you can discuss it.
- Never claim a fixed number of passing tests, discovered bugs, performance improvement or CI success unless you measured it.

### Suggested search terms

`QA Intern`, `QA Trainee`, `SQA Trainee`, `Associate QA Engineer`, `Junior SQA Engineer`, `Software Tester`, `Junior QA Automation`, `QA Engineer Python`, `QA Engineer API Testing`.

Review postings on LinkedIn, Rozee.pk, Indeed Pakistan, company career pages and the PSEB Tech Destination apprenticeship portal. Confirm current eligibility, requirements and deadlines directly on the relevant official listing.

---

## 9. Recommended resources

Use these to answer the task you're doing, not to binge-watch entire courses.

- **ISTQB CTFL v4.0.1 syllabus:** <https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf> — testing fundamentals, test techniques, risk and defect management.
- **ISTQB CTFL overview:** <https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/>.
- **HTTP Semantics (RFC 9110):** <https://www.rfc-editor.org/rfc/rfc9110.html> — method semantics and idempotency.
- **Postman Quick Start:** <https://learning.postman.com/docs/getting-started/quick-start> — requests, collections and variables.
- **Postman CLI:** <https://learning.postman.com/docs/postman-cli/postman-cli-installation> — optional current CLI workflow. Postman's docs state Newman is no longer maintained and is incompatible with newer Collection v3 workflows: <https://learning.postman.com/latest-v-12/docs/reference/newman-cli/migrate-to-postman-cli>.
- **Python tutorial:** <https://docs.python.org/3/tutorial/> — use the sections needed for functions, data structures, exceptions, files and classes.
- **Requests quickstart:** <https://requests.readthedocs.io/en/latest/user/quickstart/>.
- **pytest getting started:** <https://docs.pytest.org/en/stable/getting-started.html>.
- **pytest fixtures:** <https://docs.pytest.org/en/stable/how-to/fixtures.html>.
- **pytest parameterization:** <https://docs.pytest.org/en/stable/how-to/parametrize.html>.
- **pytest flaky tests:** <https://docs.pytest.org/en/stable/explanation/flaky.html>.
- **SQLBolt:** <https://sqlbolt.com> — beginner SQL exercises.
- **OWASP API Security Top 10 (2023):** <https://api-security.owasp.org/editions/2023/en/0x11-t10/> — BOLA and object-property authorization concepts.
- **Playwright Python introduction:** <https://playwright.dev/python/docs/intro>.
- **Playwright locators:** <https://playwright.dev/python/docs/locators>.
- **Playwright assertions:** <https://playwright.dev/python/docs/test-assertions>.
- **Playwright auto-waiting/actionability:** <https://playwright.dev/python/docs/actionability>.
- **Playwright CI:** <https://playwright.dev/python/docs/ci-intro>.
- **GitHub Actions:** <https://docs.github.com/en/actions>.

---

## 10. Day-30 acceptance checklist

- [ ] I understand the testing process and can design cases using BVA/EP and at least one other technique.
- [ ] I can write and explain a reproducible bug report.
- [ ] I have explored the actual API routes and documented the tested scope.
- [ ] I can build and run a Postman collection with meaningful assertions.
- [ ] I can write pytest API tests with fixtures, assertions, parameters and safe data cleanup.
- [ ] I understand practical SQL joins and can explain at least one database check.
- [ ] I have tested authorization with two separate users against a local/authorized system.
- [ ] I have a small UI automation suite using stable locators and meaningful assertions.
- [ ] I have one working CI workflow that actually runs my tests.
- [ ] My repository is reproducible and contains no real secrets or unauthorized data.
- [ ] My CV only claims work I actually completed and can explain.
- [ ] I have applied to relevant entry-level roles and tracked outcomes.
- [ ] I have completed a mock interview and identified my next three gaps.

If several core items are not complete, use the Days 31–60 period to finish them before advanced specialization. A roadmap is successful when it improves demonstrated competence, not when all boxes are ticked regardless of quality.
