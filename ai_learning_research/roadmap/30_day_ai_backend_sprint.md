# The 30-Day Research-Informed Backend Sprint (JobPulse Training Ground)

A structured, deliberate-practice execution blueprint for computer science and software engineering graduates. Rather than building throwaway tutorial toys from scratch, this roadmap uses your existing production application—**JobPulse** (`backend/app`)—as your primary training ground to build, verify, and master backend engineering.

---

## 1. The Daily Operating Routine (Recommended 4-Hour Block)

Consistency outweighs marathon fatigue. If four hours is not sustainable on certain days, scale down the block proportionally rather than skipping days. The planned active study time is 220 minutes (3 hours and 40 minutes), with the remaining 20 minutes reserved for breaks, environment setup, and transition between blocks to complete a full 4-hour study session.

| Activity | Recommended Time | Focus & Cognitive Activity |
| :--- | :---: | :--- |
| **Build or Extend Backend** | **120 minutes** | Hands-on engineering on `backend/app`: tracing routes, data modeling, implementing vertical slices. |
| **DSA Fundamentals** | **45 minutes** | Solving 1 LeetCode problem using the Socratic DSA Coach (Arrays, Two Pointers, Hash Maps, Binary Search). |
| **Testing & Adversarial Review** | **35 minutes** | Writing PyTest cases covering invalid payloads, auth boundaries, and reviewing edge cases with AI. |
| **Closed-Book Recall & Learning Log** | **20 minutes** | Explaining logic without notes, logging what you learned, and tracking items to revisit in 1, 3, and 7 days. |

### The Daily Learning Log Template
At the conclusion of each study session, record:
1. **Feature Completed or Extended:** (e.g., Application notes endpoint with cascade deletion).
2. **Bug Found or Prevented:** (e.g., Fixed missing user ownership check allowing cross-user note access).
3. **What I Can Explain Without Help:** (e.g., Difference between `selectinload` and `joinedload` in async SQLAlchemy).
4. **Items to Revisit (Spaced Intervals):** (Review token expiry handling in 48 hours).

---

## 2. The 4-Metric Learning Scorecard

Evaluate whether AI is making you genuinely better—not merely faster at pasting code:

| Metric | Evaluation Question | Verification Standard |
| :--- | :--- | :--- |
| **1. Independent Completion** | Can you implement a related small feature without AI and without copying the original code? | Blank-file implementation with only official documentation reference. |
| **2. Debugging Ability** | Can you reproduce a defect, identify the root cause, write a regression test, and explain the fix? | Regression test fails before fix, passes after fix. |
| **3. Technical Explanation** | Can you explain why you chose your database schema, API contracts, status codes, and test strategies? | Verbal or written defense without buzzwords or hesitation. |
| **4. Conceptual Transfer** | Can you apply the same architectural pattern to a novel requirement rather than just repeating the demo? | Designing an interview stage model based on the application model pattern. |

*Rule:* If your completion speed increases but your independent completion or debugging scores stagnate, adjust your AI use: request smaller hints, make more unassisted attempts, and increase closed-book reconstruction time.

---

## 3. Four-Week Milestone Progression (JobPulse Focus)

### WEEK 1: Understand & Rebuild One Vertical Slice
* **Core Objective:** Select one existing JobPulse feature (e.g., creating and retrieving a job application). Trace the complete lifecycle of a request from the FastAPI route through Pydantic validation, SQLAlchemy queries, and PostgreSQL persistence.
* **Days 1–2 (Trace & Model):** Map out `app/models/application.py` and `app/schemas/application.py`. Document all foreign keys, unique constraints, and cascade delete rules.
* **Days 3–4 (Reconstruct):** In a scratch file or isolated branch, independently reconstruct the vertical slice: write the Pydantic schema, write the async SQLAlchemy query, and connect the route.
* **Day 5 (DSA & Verification):** LeetCode: Hash Maps & Two Pointers (Two Sum, Valid Anagram). Run existing tests: `pytest backend/tests/test_applications.py`.
* **Days 6–7 (Closed-Book Recall & Spaced Review):** Reconstruct the async database session dependency (`get_db`) from memory in 15 minutes. Explain why an async generator (`yield`) is used.

---

### WEEK 2: Master Verification by Finding Real Bugs
* **Core Objective:** Rather than assuming code works because it returns `200 OK`, actively stress-test JobPulse by discovering and patching edge cases.
* **Days 8–9 (Authentication & BOLA Boundaries):** Test missing authentication headers, invalid JWT signatures, expired tokens, and Broken Object-Level Authorization (attempting to access User A's application using User B's token).
* **Days 10–11 (Input Boundary & Validation Defects):** Pass extreme parameters to the analytics and application endpoints: `limit=-1`, `status="INVALID_STATUS"`, empty company names, excessively long strings.
* **Day 12 (DSA & Concurrency):** LeetCode: Two Pointers & Binary Search (Binary Search, Two Sum II). Review database connection pool behavior during unhandled exceptions.
* **Days 13–14 (AI Adversarial Review & Mutation):** Use the Adversarial Tester prompt to review your tests in `backend/tests/`. Ask the AI to identify 3 overlooked edge cases. Write tests to verify or refute those suggestions.

---

### WEEK 3: Improve One Production Concern
* **Core Objective:** Deepen your understanding of one critical production infrastructure concern in JobPulse rather than trying to overhaul everything simultaneously.
* **Days 15–16 (Database Migrations with Alembic):** Inspect the Alembic migration history. Create a new revision adding an index on `job_applications.applied_date`. Test `alembic upgrade head` and verify index creation in PostgreSQL with `EXPLAIN ANALYZE`.
* **Days 17–18 (Containerization & Environment Config):** Inspect `backend/Dockerfile` and `backend/docker-compose.yml`. Understand environment variable loading via Pydantic Settings (`app/core/config.py`). Run the multi-container stack locally.
* **Day 19 (DSA & Stacks):** LeetCode: Stack Patterns (Valid Parentheses, Min Stack).
* **Days 20–21 (Continuous Integration):** Set up or audit the GitHub Actions workflow (`.github/workflows/ci.yml`) to run `pytest backend/tests` automatically on every push.

---

### WEEK 4: Test Independent Competence & Launch
* **Core Objective:** Implement a complete, related feature extension in JobPulse with limited AI assistance, and prepare to articulate your engineering choices to interviewers.
* **Days 22–23 (Independent Feature Extension):** Add an interview debrief rating or salary negotiation milestone to JobPulse. Attempt the schema, route, and tests independently before requesting graduated hints.
* **Days 24–25 (Deliberate Mutation & Bug Fix):** Deliberately introduce a defect (e.g., invert a boolean check or omit a foreign key index). Write a regression test that fails on the defect, then fix it cleanly.
* **Days 26–27 (Technical Interview Defense):** Use the Architecture Challenger prompt to conduct a 45-minute mock interview defending JobPulse:
  - Why FastAPI async instead of Flask/Django?
  - Why PostgreSQL relational modeling instead of MongoDB?
  - What are the trade-offs of stateless JWTs vs stateful Redis sessions?
* **Days 28–30 (Deploy & Targeted Outreach):** Deploy your updated backend to Render or Railway connected to Neon/Supabase PostgreSQL. Send 5 targeted outreach messages to Engineering Leads at Pakistani software houses using the proven playbook template.
