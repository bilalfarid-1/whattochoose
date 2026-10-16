# Protocol 03: Active Recall & Mutation Drills

This protocol operationalizes the **Testing Effect** (Roediger & Karpicke, 2006) and **Deliberate Practice** (Ericsson & Pool, 2016) to verify that you genuinely understand your codebase and can reconstruct its key components independently.

---

## 1. Objective

To demonstrate independent competence by reconstructing core modules from memory without reference notes, and discovering subtle defects injected into code through automated test suites.

---

## 2. Theoretical Grounding

* **The Testing Effect (Roediger & Karpicke, 2006):** Actively retrieving information from memory produces substantially higher delayed retention than passive re-reading or review alone.
* **Overcoming Misconceptions (Prather et al., 2024):** Learners frequently overestimate their mastery when reading code they generated with AI. Closed-book reconstruction reveals gaps between recognition and production.

---

## 3. The 3-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                         PROTOCOL 3: ACTIVE RECALL & MUTATION DRILL                      |
+-----------------------------+-----------------------------+-----------------------------+
| Drill 1: Closed-Book Recall | Drill 2: Mutation Testing   | Drill 3: Spaced Retrieval   |
+-----------------------------+-----------------------------+-----------------------------+
| • Rebuild a core component  | • AI injects subtle bugs    | • Re-test the module after  |
|   from a blank file         | • Run PyTest to see if      |   48 hours & 7 days         |
| • Check documentation only  |   tests catch the defect    | • Verify retention curve    |
|   after an honest attempt   | • Patch and verify fix      |                             |
+-----------------------------+-----------------------------+-----------------------------+
```

### Drill 1: Closed-Book Reconstruction
1. Select one core component in your JobPulse application (e.g., `app/core/security.py` containing password hashing and JWT token generation, or a database CRUD service).
2. Create a temporary scratch file (e.g., `scratch_rebuild.py`).
3. Set a timer for 15–20 minutes.
4. From memory, write the function signatures, Pydantic schemas, or database queries.
5. Compare your implementation against the original:
   - What did you remember correctly?
   - What did you forget or misconfigure?
   - Record the gap in your learning log and review the specific concept.

### Drill 2: AI Mutation Testing (The Bug Hunt)
1. Share a completed module (e.g., your application status update route) with your AI assistant using the **Adversarial Tester Prompt** (`prompts/adversarial_tester.prompt.md`).
2. Prompt the AI:
   > *"Inject 2 subtle, realistic defects into this code (e.g., an incorrect status code, an off-by-one boundary, or a missing transaction rollback). Return only the modified code without explaining what was changed. I will run my PyTest suite to see if my existing tests catch the defects."*
3. Replace the module with the mutated version and run your test suite:
   ```powershell
   pytest tests/
   ```
   - **If the tests fail:** Your test suite successfully caught the regression. Identify the defect from the traceback and patch it.
   - **If the tests pass:** Your test suite has a coverage blind spot. Identify what broke and add a new test case to prevent the regression.

### Drill 3: Spaced Retrieval Sessions
Schedule review sessions at spaced intervals:
* **Day 1:** Build and test the feature.
* **Day 3 (48 Hours Later):** Re-implement the key function or query from scratch in 10 minutes.
* **Day 7 (1 Week Later):** Explain the architecture and edge cases to another person or an AI interviewer.

---

## 4. Verification Checkpoint

A concept is well-understood when you can:
1. Reconstruct its primary interfaces and database queries from a blank file with minimal documentation lookups.
2. Formulate test assertions that detect regressions and boundary errors.
