# AI-Augmented Engineering Mastery Framework

A research-informed learning framework grounded in empirical studies, designed to master **Python Backend Systems Engineering** using Generative AI as a deliberate cognitive amplifier, while avoiding passive tutorial bingeing and superficial AI dependence.

---

## 1. Directory Structure

```
ai_learning_research/
├── README.md                               # Architecture overview & setup guide (this file)
├── SOURCES.md                              # Scholarly bibliographic audit (journals, conferences, books, preprints)
├── framework/
│   ├── cognitive_architecture.md           # Working memory, Deliberate Practice & the Verification Shift
│   └── anti_patterns.md                    # 6 learning anti-patterns & corrective disciplines
├── protocols/
│   ├── 01_socratic_subgoal_decomposition.md# Subgoal chunking with graduated assistance
│   ├── 02_adversarial_code_review.md       # AI stress-testing code across 5 threat vectors
│   ├── 03_active_recall_mutation_drills.md # Closed-book reconstruction & bug hunting
│   └── 04_feynman_interrogation.md         # Oral defense of architectural trade-offs
├── prompts/
│   ├── socratic_mentor.prompt.md           # Research-informed prompt: graduated hints & subgoals
│   ├── adversarial_tester.prompt.md        # Research-informed prompt: finds edge cases & bugs
│   ├── architecture_challenger.prompt.md   # Research-informed prompt: systems design interviewer
│   └── dsa_coach.prompt.md                 # Research-informed prompt: Socratic LeetCode coaching
├── roadmap/
│   └── 30_day_ai_backend_sprint.md         # 30-day active-learning sprint using JobPulse as training ground
└── tests/
    └── test_protocols_and_sources.py       # Automated consistency test suite (6 passing tests)
```

---

## 2. Core Scientific Foundations

This framework synthesizes 16 categorized scholarly references across Cognitive Science, Computing Education (ACM SIGCSE / ICER), and Human-Computer Interaction (ACM CHI):

1. **Separating Productivity from Learning (Maier et al., 2026 Meta-analysis):**  
   A meta-analysis of 23 studies, comprising 14 studies contributing productivity outcomes and 10 contributing learning outcomes, found a moderate positive effect on productivity ($g=0.33$) and no statistically significant pooled effect on learning outcomes ($g=0.14$, 95% CI $[-0.18, 0.47]$). We optimize for building software efficiently with AI while measuring independent unassisted competence separately.
2. **Avoiding the Illusion of Competence (Prather et al., ACM ICER 2024):**  
   Novices relying on uncritical AI code generation often suffer from misconceptions and inflated confidence. Our framework emphasizes independent reproduction and explanation rather than treating assisted completion as proof of learning.
3. **The Verification Shift (Mozannar et al., ACM CHI 2024):**  
   Developers using AI spend substantial cognitive effort reading, reviewing, and validating suggestions. We train developers to write automated test suites (PyTest) to independently verify AI suggestions.
4. **Subgoal Learning & Working-Memory Chunking (Margulieux & Catrambone, 2016; Cowan, 2001; Sweller, 1988, 2011):**  
   Structuring procedural programming into distinct functional subgoals (Data Layer $\to$ Validation $\to$ Business Logic $\to$ Tests) reduces cognitive overload.
5. **The Testing Effect & Retrieval Practice (Roediger & Karpicke, 2006; Ericsson & Pool, 2016):**  
   Actively retrieving information from memory through closed-book reconstruction builds significantly more durable delayed retention than re-reading notes or re-watching tutorials.

---

## 3. How to Execute This Framework

### Step 1: Initialize Your AI Assistant with Guardrails
Select your preferred AI assistant (ChatGPT, Claude, or Gemini). Copy the research-informed system prompt from [`prompts/socratic_mentor.prompt.md`](prompts/socratic_mentor.prompt.md) and paste it into your chat session.

### Step 2: Use JobPulse as Your Primary Training Ground
Rather than building throwaway tutorial projects, open [`roadmap/30_day_ai_backend_sprint.md`](roadmap/30_day_ai_backend_sprint.md) and use the existing production backend in `backend/app` to trace routes, strengthen tests, and add vertical features.

### Step 3: Track the 4-Metric Learning Scorecard
Evaluate your progress across:
* **Independent Completion:** Can you implement a small related feature without AI?
* **Debugging Ability:** Can you reproduce a bug, create a failing regression test, and fix it?
* **Technical Explanation:** Can you explain your schema and API trade-offs clearly?
* **Conceptual Transfer:** Can you apply the pattern to a novel problem?

### Step 4: Run Automated Consistency Tests
Check citation identifiers, prompt guardrails, and protocol structure:
```bash
python -m pytest -v ai_learning_research/tests/test_protocols_and_sources.py
```
*(Note: The test suite verifies citation identifiers, system prompt rules, and document consistency; it does not automatically resolve live external DOIs or replace critical manual source analysis).*
