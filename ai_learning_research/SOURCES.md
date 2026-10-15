# Academic Bibliographic Audit: Learning Engineering in the Generative AI Era

This document establishes the scientific foundation for the AI-Augmented Engineering Mastery Framework. It audits seminal peer-reviewed research and meta-analyses across **Cognitive Science**, **Computing Education (ACM SIGCSE / ICER)**, and **Human-Computer Interaction (ACM CHI)**, detailing empirical findings, methodologies, and their practical application to software engineering skill acquisition.

---

## 1. Primary Empirical Literature Matrix

| Citation | Venue / Year | Publication Type | Empirical Cohort & Methodology | Key Findings Applied in Framework |
| :--- | :--- | :--- | :--- | :--- |
| **Prather, J., Reeves, B. N., Leinonen, J., MacNeil, S., et al.** | **ACM ICER 2024** | Peer-reviewed Conference Paper | Observational study of 21 novice programming sessions analyzing interaction logs, code submissions, and self-reported perceptions. | Although 20 of 21 students completed the assigned problem, interaction patterns diverged substantially: some used AI to accelerate code they understood, while others struggled with misconceptions and an exaggerated sense of competence. Demonstrates the need to evaluate independent comprehension rather than relying solely on AI-assisted completion. |
| **Maier, P., et al.** | **arXiv (May 2026)** | Research Preprint (Meta-analysis) | Systematic meta-analysis of 23 studies in total (14 contributing productivity outcomes and 10 contributing learning outcomes, with one study appearing in both groups). | A meta-analysis of 23 studies, comprising 14 studies contributing productivity outcomes and 10 contributing learning outcomes, found a moderate positive effect on productivity ($g=0.33$) and no statistically significant pooled effect on learning outcomes ($g=0.14$, 95% CI $[-0.18, 0.47]$). Highlights the critical need to measure independent, unassisted competence separately from AI-assisted task completion speed. |
| **Kazemitabaar, M., et al. (CodeAid)** | **ACM CHI 2024** | Peer-reviewed Conference Paper | Deployment study of an AI programming assistant with ~700 undergraduate students across a 12-week CS course. | CodeAid provided conceptual explanations, pseudocode, and targeted annotations instead of direct completed code. Demonstrates that structured, scaffolded AI help can support novice problem-solving, though graduated worked examples remain valuable when facing novel knowledge gaps. |
| **Kazemitabaar, M., Hou, X., Henley, A., Ericson, B., et al.** | **ACM Koli Calling 2023** | Peer-reviewed Conference Paper | Controlled laboratory evaluation in the *Coding Steps* environment studying Python learning with Codex. | Access to AI code generators boosted immediate task completion. However, students who relied on single-prompt generation struggled on subsequent code modification tasks, pointing to the risk of over-reliance without self-regulation. |
| **Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E.** | **ACM CHI 2024** | Peer-reviewed Conference Paper | User study analyzing programmers with Copilot via retrospective video analysis and the CUPS taxonomy (12 interaction states). | AI assistance shifts developer effort toward reading, reviewing, and validating generated suggestions. When developers lack domain grasp, verifying suggestions becomes a cognitive friction point, underscoring the importance of deliberate verification practice. |
| **Denny, P., Prather, J., Becker, B. A., et al.** | **Communications of the ACM (2024)** | Peer-reviewed Journal Article | Synthesis of empirical studies in computing education post-LLM launch. | Cautions against the *illusion of competence*. Recommends shifting instruction toward problem decomposition, prompt formulation, and critical evaluation of code artifacts. |
| **Margulieux, L. E., & Catrambone, R.** | **Journal of Educational Psychology (2016)** | Peer-reviewed Journal Article | Experimental studies comparing traditional vs. subgoal-labeled worked examples in programming. | Structuring procedural programming procedures into meaningful functional subgoals reduces cognitive load and significantly enhances transfer to novel tasks. |
| **Roediger, H. L., & Karpicke, J. D.** | **Perspectives on Psychological Science (2006)** | Peer-reviewed Review Article | Review of empirical laboratory and classroom studies on the Testing Effect. | Actively retrieving information from memory produces stronger delayed retention than repeated passive study alone, depending on retrieval success, spacing, and feedback conditions. |
| **Cowan, N.** | **Behavioral and Brain Sciences (2001)** | Peer-reviewed Journal Article | Comprehensive empirical review of working-memory capacity. | Identifies an approximate working-memory capacity limit of $4 \pm 1$ discrete information chunks for novel, unchunked stimuli in young adults, cautioning against cognitive overload in multi-step problem solving. |
| **Sweller, J.** | **Cognitive Science (1988) / Springer (2011)** | Foundational Theory / Book Chapter | Decades of experimental problem-solving studies. | Working memory is strictly limited. Instructional design must minimize extraneous load (irrelevant friction) and support germane processing (schema construction). |
| **Bjork, E. L., & Bjork, R. A.** | **Book Chapter (2011)** | Scholarly Book Chapter | Synthesis of research on memory retrieval, spacing, and interleaving. | Easy, fluent learning conditions often foster an illusion of mastery. Introducing *desirable difficulties* (e.g., generation, spacing, interleaving) enhances long-term retention and flexible transfer. |
| **Ericsson, K. A., & Pool, R.** | **Book (2016)** | Scholarly Book | Longitudinal research on expert performance across multiple domains. | Repetition alone does not create expertise. Skill development requires deliberate practice: clearly defined stretch goals just beyond current comfort, rapid feedback, and construction of internal mental representations. |
| **Chi, M. T. H., Bassok, M., Lewis, M. W., et al.** | **Cognitive Science (1989)** | Peer-reviewed Journal Article | Laboratory study of verbal think-aloud protocols during STEM problem solving. | High-performing students spontaneously generate self-explanations that link specific procedural steps to general principles; low-performing students passively accept worked solutions. |
| **Mollick, E. R., & Mollick, L.** | **SSRN Working Paper (2023)** | Scholarly Working Paper | Pedagogical design framework testing structured LLM system prompts in education. | Demonstrates that structuring AI prompts into pedagogical roles (e.g., Socratic tutor, coach) fosters active student reflection compared to direct question-and-answer interactions. |
| **Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M.** | **arXiv (2023)** | Research Preprint | Controlled trial with 95 developers using GitHub Copilot vs. unassisted control. | Developers using AI completed tasks 55.8% faster. Highlights that productivity gains in software authoring depend on the developer's ability to evaluate and debug the generated code. |

---

## 2. In-Depth Methodological Annotations

### 1. Prather et al. (ACM ICER 2024) — *The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers*
* **Publication Venue:** Proceedings of the 2024 ACM Conference on International Computing Education Research (ICER '24).
* **DOI:** [https://doi.org/10.1145/3632620.3671116](https://doi.org/10.1145/3632620.3671116)
* **Official Listing:** [ICER 2024 Papers Listing](https://icer2024.acm.org/details/icer-2024-papers/26/The-Widening-Gap-The-Benefits-and-Harms-of-Generative-AI-for-Novice-Programmers)
* **Methodology & Scope:**
  - Observed 21 introductory programming students completing code-authoring tasks with generative AI assistance.
  - Analyzed prompt logs, interaction histories, screen recordings, and student self-assessments.
* **Core Empirical Findings:**
  - 20 of 21 participants completed the assigned task. However, their interaction strategies diverged into distinct approaches.
  - Some learners used AI to accelerate tasks whose underlying concepts they already understood.
  - Other learners encountered persistent misconceptions, accepting AI suggestions uncritically and developing an inflated sense of competence despite struggling to explain the code.
* **Framework Translation:**
  - The study is observational and small-sample ($N=21$); it does not prove that all AI-generated code inherently damages learning.
  - Rather, it establishes that task completion with AI cannot be used as evidence of understanding. Learners must independently verify, explain, and reproduce key logic unassisted.

### 2. Maier et al. (arXiv, May 2026) — *A Meta-analysis of the Effect of Generative AI on Productivity and Learning in Programming*
* **Publication Venue:** arXiv preprint (May 2026).
* **Resource:** [https://arxiv.org/abs/2605.04779](https://arxiv.org/abs/2605.04779)
* **Methodology & Scope:**
  - Systematic meta-analysis of 23 studies in total, comprising 14 studies contributing productivity outcomes and 10 contributing learning outcomes (13 examined productivity only, 9 examined learning only, and 1 examined both).
* **Core Empirical Findings:**
  - A meta-analysis of 23 studies, comprising 14 studies contributing productivity outcomes and 10 contributing learning outcomes, found a moderate positive effect on productivity ($g=0.33$) and no statistically significant pooled effect on learning outcomes ($g=0.14$, 95% CI $[-0.18, 0.47]$).
  - Outturn varied significantly depending on whether AI assistance was permitted during post-test evaluations.
* **Framework Translation:**
  - Confirms the necessity of separating *productivity metrics* (how fast you ship JobPulse features with AI) from *learning metrics* (how well you can reproduce, explain, and debug the code without AI).

### 3. Kazemitabaar et al. (ACM CHI 2024) — *CodeAid: Evaluating a Classroom Deployment of an LLM-Based Programming Assistant*
* **Publication Venue:** Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems.
* **DOI:** [https://doi.org/10.1145/3613904.3642773](https://doi.org/10.1145/3613904.3642773)
* **Methodology & Scope:**
  - Deployed CodeAid across a cohort of approximately 700 undergraduate programming students over a 12-week course.
  - Configured the tool to provide conceptual explanations, pseudocode, and targeted annotations while withholding direct code solutions for homework assignments.
* **Core Empirical Findings:**
  - Students actively engaged with conceptual explanations and pseudocode, utilizing the tool for debugging guidance and conceptual clarification.
  - Proved that scaffolded, explanation-first AI assistance is practical and well-received in large-scale educational settings.
* **Framework Translation:**
  - Informs our *Graduated Assistance Model*: rather than enforcing a dogmatic, permanent ban on all code examples, learners should request conceptual hints first, subgoal pseudocode second, partial snippets third, and complete worked examples only when resolving genuinely novel knowledge gaps.

### 4. Mozannar et al. (ACM CHI 2024) — *Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming*
* **Publication Venue:** Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems.
* **DOI:** [https://doi.org/10.1145/3613904.3641936](https://doi.org/10.1145/3613904.3641936)
* **Methodology & Scope:**
  - User study evaluating programmers completing programming tasks using GitHub Copilot, tracked via retrospective video labeling and the 12-state CUPS taxonomy.
* **Core Empirical Findings:**
  - Programmers spend significant cognitive effort reading, inspecting, and validating suggestions rather than authoring code.
  - When suggestions introduce subtle defects or unfamiliar idioms, verification becomes a major friction point.
* **Framework Translation:**
  - Motivates our *Adversarial Verification Protocol*: developers must build deliberate test suites to verify AI suggestions rather than passively accepting green checkmarks.

### 5. Cowan (2001) / Sweller (1988, 2011) — *Working-Memory Capacity & Cognitive Load*
* **Cowan DOI:** [https://doi.org/10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922)
* **Core Scientific Principle:**
  - Nelson Cowan's review established that young adults can hold approximately $4 \pm 1$ discrete information chunks in central working memory when rehearsal and long-term memory chunking are constrained.
  - This is an empirical capacity estimate for novel, unchunked information, not a rigid mathematical limit on every software engineering task.
* **Framework Translation:**
  - When learning full-stack backend development (routes, schemas, queries, migrations, tests), learners face high intrinsic cognitive load. Structuring tasks into subgoals reduces cognitive overload by chunking complex sequences.

### 6. Roediger & Karpicke (2006) — *The Testing Effect & Retrieval Practice*
* **DOI:** [https://doi.org/10.1111/j.1745-6916.2006.00012.x](https://doi.org/10.1111/j.1745-6916.2006.00012.x)
* **Core Scientific Principle:**
  - Across multiple laboratory experiments, active retrieval (testing) produced significantly greater delayed memory retention compared with repeated study/rereading.
  - The magnitude of the testing effect varies with initial retrieval success, the presence of feedback, and the delay between study and test.
* **Framework Translation:**
  - Supports closed-book recall and reconstruction sessions: re-implementing an authentication dependency or schema from memory after 24–48 hours builds substantially higher retention than re-reading the working code.

---

## 3. Bibliographic References (Categorized Scholarly Works)

### Peer-Reviewed Journal Articles
1. Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114. https://doi.org/10.1017/S0140525X01003922
2. Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13(2), 145–182. https://doi.org/10.1207/s15516709cog1302_1
3. Denny, P., Prather, J., Becker, B. A., Leinonen, J., & Luxton-Reilly, A. (2024). Computing education in the era of generative AI. *Communications of the ACM*, 67(2), 34–37. https://doi.org/10.1145/3624720
4. Margulieux, L. E., & Catrambone, R. (2016). Improving transfer in programming through subgoal learning and cognitive load mitigation. *Journal of Educational Psychology*, 108(7), 980–1001. https://doi.org/10.1037/edu0000108
5. Roediger, H. L., & Karpicke, J. D. (2006). The power of testing memory: Basic research and implications for educational practice. *Perspectives on Psychological Science*, 1(3), 181–210. https://doi.org/10.1111/j.1745-6916.2006.00012.x
6. Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285. https://doi.org/10.1207/s15516709cog1202_4

### Peer-Reviewed Conference Proceedings
7. Kazemitabaar, M., Hou, X., Henley, A., Ericson, B. J., Weintrop, D., & Grossman, T. (2023). How novices use LLM-based code generators to solve CS1 coding tasks in a self-paced learning environment. *Proceedings of the 23rd Koli Calling International Conference on Computing Education Research*, 1–12. https://doi.org/10.1145/3631802.3631835
8. Kazemitabaar, M., Ye, R. Z., Wang, X., Ericson, B. J., Henley, A., & Grossman, T. (2024). CodeAid: Evaluating a classroom deployment of an LLM-based programming assistant. *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, 1–19. https://doi.org/10.1145/3613904.3642773
9. Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, 1–18. https://doi.org/10.1145/3613904.3641936
10. Prather, J., Reeves, B. N., Leinonen, J., MacNeil, S., Becker, B. A., & Denny, P. (2024). The widening gap: The benefits and harms of generative AI for novice programmers. *Proceedings of the 2024 ACM Conference on International Computing Education Research (ICER '24)*, 1–15. https://doi.org/10.1145/3632620.3671116

### Scholarly Books & Book Chapters
11. Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World: Essays Illustrating Fundamental Contributions to Society* (pp. 56–64). Worth Publishers.
12. Ericsson, K. A., & Pool, R. (2016). *Peak: Secrets from the new science of expertise*. Houghton Mifflin Harcourt.
13. Sweller, J. (2011). Cognitive load theory. In J. P. Mestre & B. H. Ross (Eds.), *The Psychology of Learning and Motivation: Cognition in Education* (Vol. 55, pp. 37–76). Academic Press. https://doi.org/10.1016/B978-0-12-387693-5.00002-8

### Working Papers & Preprints
14. Maier, P., et al. (2026). A meta-analysis of the effect of generative AI on productivity and learning in programming. *arXiv preprint arXiv:2605.04779*. https://arxiv.org/abs/2605.04779
15. Mollick, E. R., & Mollick, L. (2023). Using AI to implement effective teaching strategies in classrooms: Five strategies, including prompts. *Wharton School Research Paper*, SSRN. https://ssrn.com/abstract=4391243
16. Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. *arXiv preprint arXiv:2302.06590*. https://arxiv.org/abs/2302.06590
