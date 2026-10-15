# Protocol 03: Active Recall & Mutation Drills

This protocol operationalizes the **Testing Effect** (Roediger & Karpicke, 2006) and **Deliberate Practice** (Ericsson, 1993) to destroy the illusion of competence and burn architectural patterns into permanent neural memory.

---

## 1. Objective

To prove that you actually own the code you have built by deliberately deleting core components and reconstructing them from a blank file from memory, followed by diagnosing intentional bugs injected into your codebase.

---

## 2. Theoretical Grounding

* **The Testing Effect (Roediger & Karpicke):** Active retrieval creates synaptic pathways that passive review cannot duplicate. Reconstructing an architecture from scratch yields up to 400% higher retention than re-reading the code.
* **Overcoming the "Illusion of Explanatory Depth" (Keil, 2003):** You only discover what you do not understand when forced to produce the solution without visual cues.

---

## 3. The 3-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                         PROTOCOL 3: ACTIVE RECALL & MUTATION DRILL                      |
+-----------------------------+-----------------------------+-----------------------------+
| Drill 1: The Blind Rebuild  | Drill 2: Mutation Testing   | Drill 3: Spaced Retrieval   |
+-----------------------------+-----------------------------+-----------------------------+
| • Delete a core module      | • AI injects 3 subtle bugs  | • Re-test the module after  |
| • Reconstruct from blank    | • Run PyTest (tests fail)   |   48 hours & 7 days         |
| • Only L1 conceptual hints  | • Diagnose root cause via   | • Verify retention curve    |
|   allowed if stuck          |   traceback & logs          |                             |
+-----------------------------+-----------------------------+-----------------------------+
```

### Drill 1: The Blind Rebuild (Weekly)
1. Pick one critical module in your backend (e.g., `backend/app/core/security.py` containing password hashing and JWT token creation, or `backend/app/crud/applications.py`).
2. **Delete the entire contents of the file** (or create a new blank file `security_rebuild.py`).
3. Set a timer for 15 minutes.
4. From memory, write the imports, the cryptographic helper functions, error handling, and type annotations from scratch.
5. Run your test suite:
   ```powershell
   pytest tests/test_auth.py
   ```
6. **Constraint:** If you get stuck on syntax, you may look at the official documentation (e.g., PyJWT or Passlib/Bcrypt docs), but you are **strictly forbidden from asking an AI to write the code**.

### Drill 2: AI Mutation Testing (The Bug Hunt)
1. Copy a 50-line module and paste it into your AI assistant.
2. Prompt the AI:
   > *"I am practicing mutation testing. Take this code and inject 3 subtle, realistic bugs into it (e.g., an incorrect HTTP status code, an off-by-one pagination error, an async race condition, or a missing `await` on a database commit). Return the mutated code block to me WITHOUT telling me where the bugs are. I will run my PyTest suite against it to see if my tests catch your mutations."*
3. Replace your module with the mutated code.
4. Run `pytest`.
   * **If your tests fail:** Excellent! Your test suite caught the mutation. Now inspect the error trace, identify the injected bug, and patch it.
   * **If your tests pass:** Warning! Your test suite has a coverage gap (it passed even though the code is broken). Identify the bug manually and write a new test case that catches it.

### Drill 3: Spaced Interval Retrieval
Schedule the rebuild drill across spaced intervals:
* **Day 1:** Build the feature with Socratic guidance.
* **Day 3 (48 Hours Later):** Rebuild the core dependency from scratch in 10 minutes.
* **Day 7 (1 Week Later):** Rebuild the database schema and query from scratch.

---

## 4. Verification Checkpoint

You have mastered a backend concept when you can:
1. Reconstruct its primary module from a blank editor in under 15 minutes with all unit tests passing.
2. Detect and fix 3 AI-injected mutations using only automated test failures and log tracebacks.
