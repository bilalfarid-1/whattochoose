# Protocol 01: Socratic Subgoal Decomposition

This protocol operationalizes **Subgoal Learning** (Margulieux & Catrambone, 2016) and the **Socratic Tutoring Method** (Mollick & Mollick, 2023) to eliminate cognitive overload and build mental schemas when implementing new backend features.

---

## 1. Objective

To take a complex software requirement (e.g., *"Implement JWT authentication with refresh tokens and role-based access control"* or *"Implement optimistic concurrency locking on inventory updates"*) and break it down into clean, mentally digestible architectural subgoals **without receiving or copying a single line of raw code from an AI**.

---

## 2. Theoretical Grounding

* **Cognitive Load Theory:** Prevents working-memory exhaustion by chunking 100+ lines of procedural syntax into 3–4 logical milestones.
* **The Generation Effect:** Ensuring that the student, not the AI, generates the actual implementation logic. This leads to durable long-term retention.

---

## 3. The 4-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                         PROTOCOL 1: SUBGOAL DECOMPOSITION WORKFLOW                      |
+-----------------------------+-----------------------------+-----------------------------+
| Step 1: Intent Declaration  | Step 2: Socratic Querying   | Step 3: Subgoal Execution   |
+-----------------------------+-----------------------------+-----------------------------+
| • Provide system prompt     | • AI asks clarifying queries| • Implement Subgoal 1       |
| • State feature goal        | • Student defines constraints| • Verify Subgoal 1 with test|
| • BARS raw code output      | • Agree on 3-4 Subgoals     | • Proceed to Subgoal 2      |
+-----------------------------+-----------------------------+-----------------------------+
```

### Step 1: Initiate Session with Socratic Constraint
Feed your AI assistant the **Socratic Mentor System Prompt** (located at `ai_learning_research/prompts/socratic_mentor.prompt.md`).

Submit your problem statement:
> *"I need to build an asynchronous endpoint in FastAPI that accepts user registration, hashes passwords using bcrypt, stores the user in PostgreSQL via SQLAlchemy 2.0 async, and returns a JWT access token. Do not write the code for me. Act as a Staff Backend Engineer. Help me decompose this into functional subgoals and guide me through the architectural decisions."*

### Step 2: The Socratic Dialogue
The AI will respond with probing architectural questions rather than code:
* *Question 1:* What unique constraints should be applied at the database level versus the application level for email uniqueness?
* *Question 2:* What fields should belong in the Pydantic schema validation versus the SQLAlchemy database model?
* *Question 3:* What HTTP status code should be returned if the user already exists?
* *Question 4:* How will you manage the async database session lifecycle if password hashing fails?

**Action:** You must answer these questions in your own words before moving to Step 3.

### Step 3: Establish the Canonical 4 Subgoals
Together with the AI, formalize the task into 4 explicit subgoals:
* **Subgoal 1 (Data Layer):** Define the relational schema, column types, unique constraints, and indexes in `models/user.py`.
* **Subgoal 2 (Validation Layer):** Define Pydantic request models (`UserCreate`) and response models (`UserRead`, `Token`) in `schemas/user.py`.
* **Subgoal 3 (Business Logic Layer):** Implement the password hashing utility, database insert query, and token generator in `crud/user.py` and `core/security.py`.
* **Subgoal 4 (Interface & Verification Layer):** Implement the FastAPI router endpoint and write 3 PyTest cases covering success and duplicate email collisions.

### Step 4: Step-by-Step Implementation with Graduated Hints
Implement each subgoal in your IDE **one by one**:
* If you encounter a bug or error, do NOT ask the AI to fix it.
* Instead, provide the traceback and ask: *"What invariant did I violate here?"*
* If you are completely stuck, request a **Level 1 Hint** (conceptual clue), then a **Level 2 Hint** (pseudocode structure). Never ask for executable code.

---

## 4. Verification Checkpoint

Before marking the feature complete:
1. Explain the execution path from HTTP request to PostgreSQL row commit in under 60 seconds without looking at your screen.
2. Run `pytest` and verify that both happy path and failure path tests pass.
