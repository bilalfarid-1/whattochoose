# 60-Day QA/SDET Engineering Master Sprint: Progress & Deliverables Tracker

Use this tracker to log your progress across the complete 60-day curriculum.
Primary interactive dashboard: [`30_Day_QA_Roadmap_Pro.html`](../30_Day_QA_Roadmap_Pro.html)

---

## Overall Sprint Status

* **Current Active Day:** Day 1
* **Core Days Completed (Days 1–30):** 0 / 30
* **Extension Days Completed (Days 31–60):** 0 / 30
* **Total Days Completed:** 0 / 60
* **Total Study Hours Target:** 220–230 focused hours (Core 108–112h + Extension 110–115h)
* **Target System Under Test (SUT):** JobPulse API (`backend/`)
* **Interactive Command Center:** [`30_Day_QA_Roadmap_Pro.html`](../30_Day_QA_Roadmap_Pro.html)

---

## WEEK 1: Fundamentals, Test Design & Baseline (Days 1–7)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **01** | Establish the Baseline & Environment Setup | `In Progress` | — | `docs/project-baseline.md (setup steps, version/commit, test results, route inventory, SUT decisions).` | [ ] |
| **02** | STLC, Test Levels, Types & Risk Prioritization | `Pending` | — | `docs/test-strategy.md (about 1–2 pages).` | [ ] |
| **03** | Equivalence Partitioning & Boundary Value Analysis | `Pending` | — | `docs/test-design.md + 10–15 test cases with preconditions, steps/data, and expected results.` | [ ] |
| **04** | Decision Tables, State Transitions & Prioritization | `Pending` | — | `docs/test-cases.md (add 10–15 cases, reaching 20–30 thoughtful cases total).` | [ ] |
| **05** | Bug Reports & Evidence Collection | `Pending` | — | `docs/bugs/bug-template.md + 2 completed execution records and reproducible bug reports.` | [ ] |
| **06** | Exploratory Testing Charters & Introductory SQL | `Pending` | — | `docs/exploratory-session-01.md + sql/queries.sql with explanations of initial database checks.` | [ ] |
| **07** | Weekly Review & Catch-up (Consolidation Day) | `Pending` | — | `docs/week-1-review.md listing completed items, gaps, findings, and 3 topics to revisit.` | [ ] |

---

## WEEK 2: HTTP, Postman & SQL Test Design (Days 8–14)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **08** | HTTP Protocol & 20-Route JobPulse API Inventory | `Pending` | — | `docs/api-inventory.md mapping the 20 operations with methods, bodies, and schemas.` | [ ] |
| **09** | Status Codes, Auth Semantics & Idempotency | `Pending` | — | `Expected/actual HTTP behavior table added to docs/api-inventory.md.` | [ ] |
| **10** | Postman Collection, Environments & Variables | `Pending` | — | `postman/jobpulse-collection.json + postman/environment.example.json + README.` | [ ] |
| **11** | Positive API Flows & Request Chaining | `Pending` | — | `Updated postman/jobpulse-collection.json with chained workflow folder.` | [ ] |
| **12** | Negative Testing & Boundary Exploration | `Pending` | — | `postman/jobpulse-negative-tests.json + docs/api-negative-findings.md.` | [ ] |
| **13** | SQL Relational Queries for Test Verification | `Pending` | — | `sql/api_verification_queries.sql with documented assertions for 5 core business operations.` | [ ] |
| **14** | Weekly Review & Postman Newman Run (Consolidation Day) | `Pending` | — | `docs/week-2-review.md + newman-report.html.` | [ ] |

---

## WEEK 3: Python/pytest, Custom Client & Authorization (Days 15–21)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **15** | Python Testing Ecosystem & Virtual Environments | `Pending` | — | `requirements-test.txt + tests_api/test_smoke.py verifying basic environment health.` | [ ] |
| **16** | pytest Basics, Assertions & Test Discovery | `Pending` | — | `tests_api/test_health_and_public.py with 100% passing pytest assertions.` | [ ] |
| **17** | Requests Library & Custom API Client | `Pending` | — | `tests_api/client.py + tests_api/test_client.py.` | [ ] |
| **18** | pytest Fixtures, Scopes & Teardown | `Pending` | — | `tests_api/conftest.py + tests_api/test_authenticated_flow.py.` | [ ] |
| **19** | Parametrization & Data-Driven Testing | `Pending` | — | `tests_api/test_parametrized_inputs.py with 15+ test cases executed via parameter tables.` | [ ] |
| **20** | Authorization & Multi-Tenant Boundary Tests | `Pending` | — | `tests_api/test_authorization.py covering 5 cross-user boundary scenarios.` | [ ] |
| **21** | Weekly Review & Fixture Refactoring (Consolidation Day) | `Pending` | — | `docs/week-3-review.md + fully passing `pytest tests_api/` suite.` | [ ] |

---

## WEEK 4: Playwright, CI/CD, Portfolio & Day-30 Gate (Days 22–30)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **22** | UI Testing Fundamentals & Web Locators | `Pending` | — | `docs/ui-locator-strategy.md mapping 10 key UI elements with role-based and CSS locators.` | [ ] |
| **23** | Playwright Setup & First Browser Tests | `Pending` | — | `tests_ui/test_auth_ui.py with passing Playwright browser test.` | [ ] |
| **24** | Auto-Waiting, Dynamic Content & Assertions | `Pending` | — | `tests_ui/test_dynamic_flows.py with zero explicit `time.sleep` calls.` | [ ] |
| **25** | GitHub Actions CI/CD Pipeline | `Pending` | — | `.github/workflows/qa.yml with verified green CI run on GitHub.` | [ ] |
| **26** | CI Test Selection, Smoke vs. Regression | `Pending` | — | `Updated .github/workflows/qa.yml with dual-tier smoke/regression jobs.` | [ ] |
| **27** | Capstone Portfolio Polish & Documentation | `Pending` | — | `README.md + docs/portfolio-summary.md with reproducible setup instructions.` | [ ] |
| **28** | Mock Interview Prep & Technical Defense | `Pending` | — | `docs/interview-prep-notes.md with scripted STAR stories and technical cheat-sheets.` | [ ] |
| **29** | Final Regression Run & Bug Audit | `Pending` | — | `docs/final-regression-audit.md with execution timestamps, test counts, and verified pass rates.` | [ ] |
| **30** | 30-Day Retrospective & Readiness Assessment (Consolidation Day) | `Pending` | — | `docs/day-30-retrospective.md + completed Readiness Scorecard.` | [ ] |

---

## WEEK 5: Robust API Automation, Contracts & Test Data Lifecycle (Days 31–37)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **31** | Audit and Refactor the API Suite | `Pending` | — | `docs/api-suite-review.md and a refactored, cleaner API test suite.` | [ ] |
| **32** | Environment Configuration and Safe Secrets | `Pending` | — | `config/settings.py + .env.example + updated .gitignore and README.` | [ ] |
| **33** | API Contract and Schema Validation | `Pending` | — | `tests_api/test_schemas.py + docs/contract-testing.md.` | [ ] |
| **34** | Negative Testing, State Transitions & Edge Paths | `Pending` | — | `tests_api/test_state_transitions_negative.py + docs/negative-edge-cases.md.` | [ ] |
| **35** | Test-Data Lifecycle & Stability Audit | `Pending` | — | `docs/test-data-strategy.md + clean test teardown verified across randomized runs.` | [ ] |
| **36** | Week 5 Review & Catch-up Day (Consolidation Day) | `Pending` | — | `docs/week-5-review.md with pass rate, execution speed metrics, and clean git commit.` | [ ] |
| **37** | Week 5 Cognitive Consolidation & Architecture Rest | `Pending` | — | `Updated study log noting mental readiness for Week 6.` | [ ] |

---

## WEEK 6: UI Reliability, Observability & Traces (Days 38–44)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **38** | Review Test Scope & Locator Quality | `Pending` | — | `docs/ui-automation-scope.md + refactored locators in tests_ui/.` | [ ] |
| **39** | Fixtures and UI State Isolation | `Pending` | — | `tests_ui/conftest.py with isolated browser context fixtures.` | [ ] |
| **40** | Expand End-to-End Critical UI Flow | `Pending` | — | `tests_ui/test_e2e_application_flow.py with passing end-to-end test.` | [ ] |
| **41** | Failure Diagnostics & Flaky-Test Investigation | `Pending` | — | `docs/flaky-test-investigation.md + trace configuration in pytest.ini/conftest.py.` | [ ] |
| **42** | Cross-Browser & Responsive Emulation Check | `Pending` | — | `docs/cross-browser-report.md + tests_ui/test_responsive_mobile.py.` | [ ] |
| **43** | Week 6 Review & Catch-up Day (Consolidation Day) | `Pending` | — | `docs/week-6-review.md with UI test stability log.` | [ ] |
| **44** | Week 6 Cognitive Consolidation & UI Rest | `Pending` | — | `Updated study notes reflecting on UI vs API testing balance.` | [ ] |

---

## WEEK 7: Security (BOLA), DB Constraints & CI Reliability (Days 45–51)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **45** | Expand Object-Level Authorization (BOLA) Cases | `Pending` | — | `tests_api/test_authorization_deep.py covering all mutation and read routes.` | [ ] |
| **46** | Object-Property Authorization and Mass Assignment | `Pending` | — | `tests_api/test_mass_assignment.py + docs/property-authorization.md.` | [ ] |
| **47** | Token Expiry and Authentication Edge Cases | `Pending` | — | `tests_api/test_auth_edge_cases.py covering 6 token validation scenarios.` | [ ] |
| **48** | Data Integrity and Database Constraints Verification | `Pending` | — | `tests_api/test_data_integrity.py + docs/data-integrity-tests.md.` | [ ] |
| **49** | CI Workflow Reproducibility & Artifact Retention | `Pending` | — | `Hardened .github/workflows/qa.yml + docs/ci-configuration.md.` | [ ] |
| **50** | Week 7 Review & Catch-up Day (Consolidation Day) | `Pending` | — | `docs/week-7-review.md with security matrix and clean git commit.` | [ ] |
| **51** | Week 7 Cognitive Consolidation & Security Rest | `Pending` | — | `Study notes reflecting on security testing insights.` | [ ] |

---

## WEEK 8: Specializations (AI/LLM, Mobile, Locust, TS) & Baselines (Days 52–58)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **52** | Market Review & Specialization Selection | `Pending` | — | `docs/specialization-decision.md detailing target job ads, skill counts, and rationale.` | [ ] |
| **53** | Specialization Track: Foundations & Dataset/Checklist | `Pending` | — | `Initial specialization artifact (dataset, checklist, locustfile skeleton, or tsconfig/test).` | [ ] |
| **54** | Specialization Track: Core Implementation & Execution | `Pending` | — | `Executed test runs, raw data logs, or passing TypeScript test suites.` | [ ] |
| **55** | Specialization Track: Evaluation, Reporting & Edge Cases | `Pending` | — | `Completed specialization report documenting methodology, findings, and honest limitations.` | [ ] |
| **56** | Controlled Local Performance Baseline or Reporting Hardening | `Pending` | — | `docs/performance-smoke-report.md or updated CI test reports.` | [ ] |
| **57** | Week 8 Review & Catch-up Day (Consolidation Day) | `Pending` | — | `docs/week-8-review.md with verified run commands and clean git commit.` | [ ] |
| **58** | Week 8 Rest & Cognitive Consolidation | `Pending` | — | `Reflective notes on personal growth from Day 1 to Day 58.` | [ ] |

---

## FINAL BLOCK: Clean-Clone Audit, Exit Interview & What Next (Days 59–60)

| Day | Topic | Status | Completed Date | Key Deliverable | Verified |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **59** | Full Clean-Clone Check, CV & Application Tracking | `Pending` | — | `docs/clean-clone-check.md + tailored CV + 60-second project pitch script.` | [ ] |
| **60** | Final Mock Technical Interview, Readiness Audit & Next 30-Day Decision | `Pending` | — | `docs/day-60-review.md with evidence, measured outcomes, and prioritized next-step action plan.` | [ ] |

---

## Beyond Day 60: Career Acceleration & Senior Roadmap

1. **High-Conversion Job Engine:** Target QA, Junior SDET, and API Automation roles with tailored CV and 60-second Loom project pitch.
2. **Technical Interview Mastery:** Whiteboard test architecture, live coding defense, and 4 STAR stories.
3. **Open-Source Contributions:** Add test suites to open source FastAPI/Playwright repositories.
4. **12-Month Senior SDET Roadmap:** Containerized test matrices, OpenTelemetry observability, and Chaos engineering.
