# Protocol 01: Socratic Subgoal Decomposition

This protocol operationalizes **Subgoal Learning** (Margulieux & Catrambone, 2016) and **Graduated Assistance** (Kazemitabaar et al., 2024; Mollick & Mollick, 2023) to manage cognitive load and build durable mental models when implementing backend features.

---

## 1. Objective

To take a backend requirement (such as implementing authentication, pagination, or database relationships in JobPulse) and decompose it into distinct functional subgoals, using graduated AI assistance to support independent problem solving.

---

## 2. Theoretical Grounding

* **Subgoal Learning (Margulieux & Catrambone, 2016):** Chunking multi-step procedures into labeled functional subgoals reduces cognitive overload and improves transfer to novel programming tasks.
* **Graduated Assistance (Kazemitabaar et al., 2024):** Beginning with conceptual hints and pseudocode before offering code snippets helps learners engage their own reasoning rather than defaulting to passive copying.

---

## 3. The 4-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                         PROTOCOL 1: SUBGOAL DECOMPOSITION WORKFLOW                      |
+-----------------------------+-----------------------------+-----------------------------+
| Step 1: Independent Attempt | Step 2: Socratic Subgoals   | Step 3: Graduated Support   |
+-----------------------------+-----------------------------+-----------------------------+
| • State feature requirement | • Identify 3-4 functional   | • Request conceptual hint   |
| • Sketch data model & flow  |   subgoals with AI          | • If stuck, request subgoal |
| • Attempt initial design    | • Agree on invariants       | • Use minimal snippet only  |
|   before consulting AI      |   before implementation     |   when facing novel syntax  |
+-----------------------------+-----------------------------+-----------------------------+
```

### Step 1: Independent Attempt & Intent Declaration
Before querying an AI assistant, write down:
1. The goal of the feature (e.g., *"Add filtering and pagination to the JobPulse application endpoint"*).
2. The expected inputs (query parameters: `status`, `page`, `page_size`) and outputs (list of applications, total count).
3. Your proposed database query and validation logic.

### Step 2: Establish the Functional Subgoals
Consult your AI assistant using the **Socratic Mentor Prompt** (`prompts/socratic_mentor.prompt.md`):
> *"I am adding pagination and status filtering to my JobPulse applications endpoint in FastAPI and SQLAlchemy. Here is my initial plan: [paste your notes]. Help me review the functional subgoals and identify any constraints I overlooked."*

Agree on the canonical subgoals:
* **Subgoal 1 (Data Layer):** Efficient database query using `limit` and `offset` with an indexed `status` filter.
* **Subgoal 2 (Schema Layer):** Pydantic response envelope containing `items`, `total_count`, `page`, and `page_size`.
* **Subgoal 3 (Route Implementation):** Dependency injection of the database session and parameter parsing.
* **Subgoal 4 (Defensive Testing):** PyTest cases verifying pagination boundaries (`page=1`, empty pages, invalid negative parameters).

### Step 3: Implement with Graduated Assistance
Implement each subgoal independently:
1. **Tier 1 (Conceptual Hint):** If stuck, ask: *"What SQL clause or SQLAlchemy method manages query limits without loading all rows into memory?"*
2. **Tier 2 (Subgoal / Pseudocode):** Ask for structural pseudocode showing how the query and count should be structured.
3. **Tier 3 (Partial Snippet):** If unfamiliar with specific SQLAlchemy 2.0 syntax, request a 2-line snippet for the unfamiliar construct.
4. **Tier 4 (Worked Example, when needed):** If facing a completely novel concept (e.g., configuring a transactional session fixture in PyTest), study a worked example, close the reference, and reconstruct the logic independently in your codebase.

---

## 4. Verification Checkpoint

Before marking the task complete:
1. Trace the data flow from the FastAPI route through SQLAlchemy to the PostgreSQL query without looking at notes.
2. Run your automated test suite to verify that both happy-path and boundary queries pass.
