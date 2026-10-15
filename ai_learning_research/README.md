# AI-Augmented Engineering Mastery Framework

An empirical, research-backed learning architecture and operational sprint designed to master **Python Backend Systems Engineering** using Generative AI as a deliberate cognitive amplifier while completely eliminating passive tutorials, courses, and the "illusion of competence" trap.

---

## 1. Directory Structure

```
ai_learning_research/
├── README.md                               # Executive summary & navigation guide (this file)
├── SOURCES.md                              # Rigorous academic bibliographic audit (APA 7th + DOIs)
├── framework/
│   ├── cognitive_architecture.md           # The science: Cognitive Load, Deliberate Practice, Human-AI interaction
│   └── anti_patterns.md                    # The 6 deadly traps (Oracular Crutch, Tutorial Hell 2.0, etc.)
├── protocols/
│   ├── 01_socratic_subgoal_decomposition.md# Protocol 1: Chunking architecture without code leakage
│   ├── 02_adversarial_code_review.md       # Protocol 2: LLM as senior engineer breaking your code
│   ├── 03_active_recall_mutation_drills.md # Protocol 3: Blind reproduction & bug hunting
│   └── 04_feynman_interrogation.md         # Protocol 4: Defending architectural trade-offs
├── prompts/
│   ├── socratic_mentor.prompt.md           # Battle-tested prompt: refuses answers, forces reasoning
│   ├── adversarial_tester.prompt.md        # Battle-tested prompt: generates malicious edge cases
│   ├── architecture_challenger.prompt.md   # Battle-tested prompt: challenges database & scaling choices
│   └── dsa_coach.prompt.md                 # Battle-tested prompt: guides LeetCode via hints only
├── roadmap/
│   └── 30_day_ai_backend_sprint.md         # Day-by-day active curriculum (zero video tutorials)
└── tests/
    └── test_protocols_and_sources.py       # Automated verification test suite
```

---

## 2. Core Scientific Principles

This framework directly translates findings from 12 seminal peer-reviewed research papers into software engineering practice:

1. **Eliminate the "Product-Understanding Gap" (Prather et al., ACM ICER 2024):** Novice developers who use AI as a code generator perform worst on unassisted programming tasks. We enforce the **Zero Code Leakage Rule** via system prompts that refuse to provide drop-in code.
2. **Master the Verification Shift (Mozannar et al., ACM CHI 2024):** Developers in the AI era spend over 50% of their time verifying and testing code rather than typing syntax. We train developers as adversarial reviewers who verify invariants with automated tests.
3. **Subgoal Chunking (Margulieux & Catrambone, 2016, 2021):** Learning procedural architectures is 2x more effective when broken down into functional subgoals (Data Modeling $\to$ Schemas $\to$ Business Logic $\to$ Verification).
4. **The Testing Effect & Active Recall (Roediger & Karpicke, 2006):** Active retrieval produces up to 400% higher long-term retention than passive reading or watching video tutorials.

---

## 3. How to Execute This Framework

### Step 1: Initialize Your AI Assistant with Guardrails
Select your preferred AI assistant (ChatGPT, Claude, or Gemini). Copy the system prompt from [`prompts/socratic_mentor.prompt.md`](file:///C:/Users/bilal/Gemeni_Cli/se_labor_market_research/ai_learning_research/prompts/socratic_mentor.prompt.md) and paste it into your chat session.

### Step 2: Follow the 30-Day Sprint Calendar
Open [`roadmap/30_day_ai_backend_sprint.md`](file:///C:/Users/bilal/Gemeni_Cli/se_labor_market_research/ai_learning_research/roadmap/30_day_ai_backend_sprint.md) and execute each day's 4-hour active block:
* **Block 1 (50%):** Hands-on architecture building & PyTest testing.
* **Block 2 (25%):** 1 LeetCode problem solved using the [`dsa_coach.prompt.md`](file:///C:/Users/bilal/Gemeni_Cli/se_labor_market_research/ai_learning_research/prompts/dsa_coach.prompt.md).
* **Block 3 (25%):** Adversarial verification & Feynman technical interrogation.

### Step 3: Run Automated Verification Tests
Run the automated verification suite to ensure all sources, links, and system prompt schemas are validated:
```powershell
python ai_learning_research/tests/test_protocols_and_sources.py
```
