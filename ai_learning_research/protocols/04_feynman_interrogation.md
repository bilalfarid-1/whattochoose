# Protocol 04: The Feynman AI Interrogation

This protocol operationalizes the **Self-Explanation Effect** (Chi et al., 1989) and the **Feynman Technique** by utilizing the AI as an inquisitor that interrogates your architectural choices and demands verbal justification of technical trade-offs.

---

## 1. Objective

To prepare for high-stakes technical job interviews by verbally articulating the *"Why"* behind your code, defending your design decisions against aggressive counter-arguments, and exposing gaps in your conceptual understanding.

---

## 2. Theoretical Grounding

* **The Self-Explanation Effect (Chi et al., 1989):** High-performing engineers continuously generate internal explanations that connect procedural actions to first-principle engineering laws.
* **Dual-Coding Theory & Verbalization:** Converting spatial and procedural code into clear, articulate spoken language engages distinct neural networks, consolidating mental models and eliminating interview anxiety.

---

## 3. The 3-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                        PROTOCOL 4: FEYNMAN INTERROGATION WORKFLOW                       |
+-----------------------------+-----------------------------+-----------------------------+
| Step 1: Record Rationale    | Step 2: Adversarial Critique| Step 3: Synthesis & Rebuttal|
+-----------------------------+-----------------------------+-----------------------------+
| • Pick an architectural     | • AI attacks the rationale  | • Respond to the critique   |
|   trade-off in your project | • Proposes alternative stack| • Formulate production      |
| • Speak/type your defense   | • Asks for failure modes    |   trade-off summary         |
+-----------------------------+-----------------------------+-----------------------------+
```

### Step 1: Formulate Your Technical Defense
Pick an architectural decision you made in your codebase. For example:
* *"Why did you use FastAPI with asynchronous SQLAlchemy instead of Django or Flask?"*
* *"Why did you use PostgreSQL relational modeling with foreign keys instead of MongoDB?"*
* *"Why did you implement JWT tokens rather than stateful server-side sessions stored in Redis?"*
* *"What is the indexing strategy on your `job_applications` table, and why did you choose a B-Tree index over a Hash index?"*

Feed your AI assistant the **Architecture Challenger System Prompt** (located at `ai_learning_research/prompts/architecture_challenger.prompt.md`).

Submit your explanation:
> *"Here is my defense for choosing PostgreSQL over MongoDB for the JobPulse application tracking backend: [Type or speak your 3-minute explanation]. Challenge my explanation. Point out any flawed assumptions, benchmark trade-offs, or scaling bottlenecks I ignored."*

### Step 2: The Inquisitor's Cross-Examination
The AI will cross-examine your logic, pressing you with real-world industry counter-scenarios:
* *"You claimed PostgreSQL is better because of ACID transactions. But doesn't MongoDB support multi-document ACID transactions since version 4.0? Why couldn't you use MongoDB's flexible schema to store interview notes as embedded sub-documents instead of creating a separate relational table with a foreign key join?"*
* *"You mentioned asynchronous FastAPI handles higher concurrency. But what happens if your endpoint performs a CPU-bound bcrypt password hash on the main event loop? Won't that block all incoming requests despite using async/await?"*

### Step 3: The Refined Synthesis (The Interview Answer)
You must formulate an evidence-based rebuttal that acknowledges trade-offs:
1. **Acknowledge the Counter-Scenario:** *"Yes, MongoDB supports multi-document transactions, and embedding notes eliminates joins for single-record reads."*
2. **Defend with Invariants:** *"However, in our domain model, notes and interview stages require relational integrity, cascade deletions on application deletion, and independent filtering across companies. PostgreSQL relational foreign keys enforce this at the database level rather than relying on application code."*
3. **Address the CPU-bound Bottleneck:** *"Regarding bcrypt on the async loop, that is a real hazard. In production, password hashing must be offloaded to an asynchronous threadpool via `asyncio.to_thread` or Celery workers so it does not block the async event loop."*

---

## 4. Verification Checkpoint

You are ready for senior technical interviews when:
* You can answer *"Why X instead of Y?"* for every dependency in your `requirements.txt` without hesitating.
* You can explain the primary bottleneck of your architecture and exactly how you would monitor and scale it under 100x traffic.
