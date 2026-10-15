# Protocol 02: Adversarial Code Review & Invariant Verification

This protocol operationalizes the **Verification Shift** (Mozannar et al., CHI 2024; SWE-bench verification findings) by turning the AI into a hostile, adversarial reviewer that stress-tests your code rather than helping you write it.

---

## 1. Objective

To transform clean-looking happy-path code into resilient, production-grade software by having an AI generate **hostile test payloads, concurrency edge cases, and architectural failure vectors** that you must defend against using automated tests.

---

## 2. Theoretical Grounding

* **The Verification Bottleneck (Mozannar et al., 2024):** Developers using AI coding assistants must evaluate suggestions, inspect generated code, and manage the costs of interacting with these systems. Our verification protocol translates this observation into a practical learning exercise: design tests that reveal whether the implementation satisfies its requirements.
* **Desirable Difficulties (Bjork & Bjork, 2011):** Forcing learners to anticipate and patch non-obvious failure modes encodes deep systems schemas that happy-path coding completely misses.

---

## 3. The 4-Step Operational Workflow

```
+-----------------------------------------------------------------------------------------+
|                        PROTOCOL 2: ADVERSARIAL VERIFICATION WORKFLOW                    |
+-----------------------------+-----------------------------+-----------------------------+
| Step 1: Code Submission     | Step 2: Adversarial Attack  | Step 3: PyTest Defense      |
+-----------------------------+-----------------------------+-----------------------------+
| • Paste your completed code | • AI generates 5 hostile    | • Write tests that reproduce|
| • State expected invariants |   payloads / edge cases     |   the vulnerability         |
| • Prompt hostile persona    | • AI does NOT provide fixes | • Patch the code & pass test|
+-----------------------------+-----------------------------+-----------------------------+
```

### Step 1: Submit Code to the Adversarial Tester
Feed your AI assistant the **Adversarial Tester System Prompt** (located at `ai_learning_research/prompts/adversarial_tester.prompt.md`).

Paste your completed code (e.g., your CRUD router, authentication dependency, or database query):
> *"Here is my completed endpoint in `backend/app/api/v1/endpoints/applications.py`. I have manually verified that it returns 200 OK for valid inputs. Act as a hostile Principal Security & QA Engineer. Attack this code. Find 5 non-obvious ways this will break in production under concurrency, malformed inputs, or database edge cases. Do not write the fix for me."*

### Step 2: Receive the 5 Attack Vectors
The AI will return 5 specific vulnerability or failure vectors, such as:
1. **Concurrency Race Condition:** What happens if two simultaneous requests update the same record at the exact same millisecond? (Lost update problem).
2. **Malformed Payload Injection:** What happens if a client passes a JSON body with an unexpected type (e.g., an array where a dictionary is expected)? Does it leak a 500 stack trace or return a clean 422?
3. **Database Connection Leak:** If an unhandled exception occurs inside the route before the database commit, is the async session explicitly rolled back and closed, or does it hang in the pool?
4. **Authorization Bypass:** Can User A access or update an application record belonging to User B by simply guessing the integer ID? (Broken Object-Level Authorization - BOLA).
5. **Memory Exhaustion via Pagination:** What happens if the client requests `limit=1000000`? Does the database attempt to serialize one million rows into memory?

### Step 3: The "Test-First" Defense
For each attack vector identified:
1. Do NOT immediately edit your production code.
2. First, **write a failing PyTest integration test** that simulates the attack vector. Run pytest to see it fail (`RED`).
3. Now, edit your production code to guard against the attack (e.g., adding user ownership filters, strict Pydantic range constraints `Query(default=20, le=100)`, or database transactions).
4. Re-run pytest until the test passes (`GREEN`).

---

## 4. Verification Checkpoint

Your feature is officially production-ready only when:
* You have added dedicated test cases for each of the identified edge cases in `tests/`.
* Running `pytest -v` executes all assertions cleanly with zero unhandled exceptions.
* You can explain the attack vector and the defense mechanism in simple terms.
