# Data Provenance & Primary Source Audit

This document provides transparent, verifiable provenance for all quantitative metrics, institutional publications, and analytical frameworks utilized in this repository.

---

## 1. Official Pakistani Economic & Industry Data

### 1.1 ICT Export Remittances (FY2020 – FY2026)
* **Primary Source 1:** State Bank of Pakistan (SBP), External Sector Statistics / Balance of Payments Division. [https://www.sbp.org.pk/economic-data](https://www.sbp.org.pk/economic-data)
* **Primary Source 2:** Finance Division, Government of Pakistan, *Pakistan Economic Survey 2025–26*, Chapter 15: "Information Technology and Telecommunication". Direct PDF: [https://finance.gov.pk/survey/chapter_26/15_Information_Technology.pdf](https://finance.gov.pk/survey/chapter_26/15_Information_Technology.pdf)
* **Primary Source 3:** Associated Press of Pakistan (APP), *Pakistan's ICT Export Earnings Hit Record $4.6bn in FY2025-26* (July 2026 reported outturn). [https://www.app.com.pk/national/pakistans-ict-export-earnings-hit-record-4-6bn-in-fy2025-26/](https://www.app.com.pk/national/pakistans-ict-export-earnings-hit-record-4-6bn-in-fy2025-26/)

**Audited & Reconciled Historical Figures:**
* **FY20 (2019-2020):** US$ 1.440 Billion (Official SBP baseline, as of 2020-12-31)
* **FY21 (2020-2021):** US$ 2.110 Billion (+46.5% pandemic remote surge, as of 2021-12-31)
* **FY22 (2021-2022):** US$ 2.620 Billion (+24.1%, as of 2022-12-31)
* **FY23 (2022-2023):** US$ 2.600 Billion (Macroeconomic adjustment & exchange rate volatility, as of 2023-12-31)
* **FY24 (2023-2024):** US$ 3.220 Billion (+23.8%, as of 2024-12-31)
* **FY25 (2024-2025):** US$ 3.812 Billion (Official full-year audited figure in Economic Survey, as of 2025-12-31)
* **FY26 (2025-2026):** **US$ 4.600 Billion (Reported Full-Year Outturn)**  
  *Context:* Following the 9-month July–March receipt of US$ 3.388 Billion recorded in the Pakistan Economic Survey, full fiscal year FY2025–26 outturn was reported at approximately US$ 4.60 Billion in July 2026, representing a +20.6% year-over-year expansion.
* **Compound Annual Growth Rate (CAGR) Derivation:**  
  $$\text{CAGR} = \left(\frac{4.600}{1.440}\right)^{\frac{1}{6}} - 1 = (3.1944)^{0.16667} - 1 \approx 21.36\% \approx 21.4\% \text{ per annum}$$

---

### 1.2 Pakistan IT Industry Employment & Graduate Supply
* **Primary Source:** Pakistan Software Houses Association (P@SHA), *P@SHA Skills Survey 2025*, P@SHA Research & Talent Committee.
* **Direct Official Report PDF:** [https://www.pasha.org.pk/wp-content/uploads/Skills-Survey-2025.pdf](https://www.pasha.org.pk/wp-content/uploads/Skills-Survey-2025.pdf)

**Audited Benchmark Metrics & Population Scope:**
* **Survey Population Scope:** Data reflects surveyed, participating P@SHA member enterprises (representing formal software export houses and IT service agencies). It does not represent an exhaustive census of Pakistan's informal sector, domestic corporate IT departments, or independent freelancing.
* **Hiring by Surveyed Member Companies (2024):** **47,393** total hires across participating companies.
* **Fresh Graduate Intake by Surveyed Member Companies:** **13,350** hires (representing **28.17%** of member company hiring).
* **Experience Preference:** Approximately **71.83%** of measured hiring demand across member firms is targeted at experienced professionals (mid-level and senior).
* **National Graduate Supply (Separate Benchmark):** P@SHA estimates that approximately **72,952** CS/IT graduates are produced annually across Pakistani Higher Education Institutions (HEIs).
* **Scope Boundary Note:** Because the surveyed companies ($47,393$ hires) and the national graduate estimate ($\sim 72,952$) cover different populations, their ratio ($13,350 / 72,952$) must **not** be interpreted as a national graduate employment rate. Graduates also find employment in non-member IT agencies, domestic banking/telecoms, public institutions, or international freelancing platforms.

---

## 2. U.S. and Global Tech Labor Indicators

### 2.1 Software Development Job Postings (Indeed / FRED)
* **Primary Source:** Federal Reserve Bank of St. Louis (FRED) / Indeed Hiring Lab.
* **Series Identifier:** `IHLIDXUSTPSOFTDEVE` (*Software Development Job Postings on Indeed in the United States*).
* **Direct URL:** [https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE)
* **Geographic Scope:** **United States (Domestic Job Postings)**. It does not measure global or Pakistani job postings. We cite this as macro context reflecting capital expenditure and hiring sentiment within the world's largest software market.
* **Temporal Boundaries & Observation Periods:**
  - `data_retrieved_at`: **2026-10-15** (extraction date from FRED).
  - 2020: 100.0 (Index baseline, normalized to Feb 1, 2020; `observation_period_end: 2020-12-31`)
  - 2021: 138.4 (Annual mean; `observation_period_end: 2021-12-31`)
  - 2022: 126.1 (Annual mean; `observation_period_end: 2022-12-31`)
  - 2023: 76.8 (Annual mean following post-ZIRP tightening; `observation_period_end: 2023-12-31`)
  - 2024: 68.4 (Annual mean; `observation_period_end: 2024-12-31`)
  - 2025: 71.5 (Annual mean; `observation_period_end: 2025-12-31`)
  - 2026: **72.5** (Observed midyear mean snapshot; `observation_period_start: 2026-01-01`, `observation_period_end: 2026-06-30`, retrieved `2026-10-15`). Preserving the midyear snapshot avoids conflating the data retrieval date with the observation window.

### 2.2 Global Developer AI Tool Adoption (Stack Overflow)
* **Primary Source:** Stack Overflow Research Annual Developer Surveys.
* **Sample Size:** 65,000 to 90,000+ respondents per survey wave.
* **Metric Definition:** "Proportion of developers actively using or planning to use AI developer tools in their development process".
* **Direct URLs:**
  - [Stack Overflow 2023 Developer Survey - AI Section](https://survey.stackoverflow.co/2023/#section-ai-ai-tools)
  - [Stack Overflow 2024 Developer Survey - AI Tools](https://survey.stackoverflow.co/2024/ai#ai-tools)
  - [Stack Overflow 2025 AI Survey](https://survey.stackoverflow.co/2025/ai)
* **Audited Observations:**
  - **2023:** 44.0% actively using + 26.0% planning to use = **70.0%** broad engagement.
  - **2024:** 62.0% actively using + 14.0% planning to use = **76.0%** broad engagement.
  - **2025:** **84.0%** using or planning to use; **51.0%** of professional developers report daily AI tool usage.
  - **2020–2022:** Labeled explicitly as **author historical baselines** (2.0%, 5.0%, 8.5%), as Stack Overflow did not survey AI developer tools prior to 2023.
  - **2026:** Labeled explicitly as an **author analytical projection** (~88.0%).

---

## 3. Computational Coding Benchmarks & Benchmark Separation

* **Primary Source 1:** Stanford Institute for Human-Centered Artificial Intelligence (HAI), *The AI Index Annual Reports* (2022–2025). [https://aiindex.stanford.edu/report/](https://aiindex.stanford.edu/report/)
* **Primary Source 2:** Jimenez, C. E., et al. (ICLR 2024), *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* [https://www.swebench.com/](https://www.swebench.com/)
* **Primary Source 3:** OpenAI & Princeton University (August 13, 2024), *SWE-bench Verified: A Human-Validated Benchmark for AI Software Engineering*.
* **Primary Source 4:** Chen, M., et al. (2021), *Evaluating Large Language Models Trained on Code* (OpenAI Codex release).

### Methodological Distinction: Original SWE-bench vs. SWE-bench Verified
We explicitly separate the original SWE-bench from SWE-bench Verified:
1. **Original SWE-bench (2023):** Released in late 2023 (Jimenez et al., arXiv:2310.06770), comprising 2,294 full GitHub issue-resolving tasks. The top reported baseline was **4.2%** (Claude 2: 4.8%, GPT-4: 1.7%).
2. **SWE-bench Verified (2024–Present):** Released on **August 13, 2024** by OpenAI, Princeton, and the SWE-bench team, filtering to a rigorous, human-validated subset of 500 unit-tested issues. Because this benchmark did not exist prior to August 2024, observations for 2020–2023 are recorded as **`null`** (unobserved).

**Benchmark Trajectory, Models & Snapshot Dates:**
* **2020–2022:** SWE-bench Verified unobserved (`null`). (HumanEval: 2021 Codex Pass@1 = 28.8%; 2022 code-davinci-002 = 47.0%).
* **2023:** SWE-bench Verified unobserved (`null`). Original SWE-bench baseline = **4.2%** (Jimenez et al., Oct 2023; Claude 2 / GPT-4). HumanEval Pass@1 = 67.0% (GPT-4 launch).
* **2024:** SWE-bench Verified = **38.8%**. Model: **Claude 3.5 Sonnet (claude-3-5-sonnet-20240620)** with **SWE-agent scaffold** (OpenAI & Princeton SWE-bench Verified launch report, dated **2024-08-13**). Direct URL: [https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/). HumanEval reached 90.2% (approaching saturation).
* **2025:** SWE-bench Verified = **70.3%**. Model: **Claude 3.7 Sonnet (claude-3-7-sonnet-20250219)** with **Anthropic custom high-compute agent scaffold** (test-time compute with parallel thinking & planning tool, dated **2025-02-24**). Direct URL: [https://www.anthropic.com/news/claude-3-7-sonnet](https://www.anthropic.com/news/claude-3-7-sonnet).
* **2026:** SWE-bench Verified = **75.0%**. System: **SWE-bench Verified Leaderboard Top Entry** with frontier agentic scaffold with test-time verification & search (mid-2026 leaderboard snapshot, dated **2026-06-30**). Direct URL: [https://www.swebench.com/](https://www.swebench.com/). Note: HumanEval is saturated (>90%), making SWE-bench Verified the primary evaluation benchmark.

---

## 4. Academic Literature & U.S. Labor Economics

* **Tucker, Lee C. (April 2026):** *You're (not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators*. Working Paper CES-26-27, Center for Economic Studies, U.S. Census Bureau. [https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html)  
  *Key Finding:* Documents a statistically robust decline in early-career hiring in AI-exposed technical industries within the United States. Cited as macro empirical context for technological task exposure; does not directly measure Pakistan's labor market.
* **Autor, David (2024):** *Applying AI to Rebuild Middle-Class Jobs*, NBER Working Paper 32140. Analyzes task-biased cognitive automation and task boundaries.
* **Brynjolfsson, E., Li, D., & Raymond, L. R. (2023):** *Generative AI at Work*, Quarterly Journal of Economics (NBER WP 31161). Explores productivity compression across seniority levels.
* **Peng, S., et al. (2023):** *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, arXiv:2302.06590. Documents completion speed gains on routine programming tasks.
* **Layoffs.fyi Tracker (Roger Lee):** Historical tech layoff counts: 2020 (80k), 2021 (15k), 2022 (165k), 2023 (263k peak), 2024 (152k), 2025 (98k), 2026 (~75k observed year-to-date through Q3 2026).

---

## 5. Author Qualitative Scoring Rubric & Calculation (Figure 2)

Figure 2 assigns qualitative ratings (0–100 scale) to evaluate software engineering competencies between the pre-2022 baseline and 2026. These scores are **author-assigned qualitative evaluations**, not census measurements.

### Scoring Formula:
$$\text{Final Score} = \text{round}\Big((100 - \text{Automation Exposure}) \times 0.35 + \text{Verification Necessity} \times 0.40 + \text{Screening Rigor} \times 0.25\Big)$$

### Mathematical Breakdown Table:

| Competency Domain | Pre-2022 Score | Automation Exposure ($S_{\text{auto}}$) | Verification Necessity ($S_{\text{verif}}$) | Screening Rigor ($S_{\text{screen}}$) | Weighted Calculation | Final 2026 Score |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Routine CRUD & Boilerplate** | 90 | 95 | 25 | 33 | $(5 \times 0.35) + (25 \times 0.40) + (33 \times 0.25) = 20.00$ | **20** |
| **Manual Black-Box QA** | 80 | 90 | 35 | 30 | $(10 \times 0.35) + (35 \times 0.40) + (30 \times 0.25) = 25.00$ | **25** |
| **Backend Architecture (Python/FastAPI)** | 75 | 20 | 97 | 100 | $(80 \times 0.35) + (97 \times 0.40) + (100 \times 0.25) = 91.80$ | **92** |
| **Automated Testing & Verification** | 55 | 15 | 100 | 100 | $(85 \times 0.35) + (100 \times 0.40) + (100 \times 0.25) = 94.75$ | **95** |
| **AI Practical Orchestration (APIs/RAG)** | 10 | 25 | 92 | 100 | $(75 \times 0.35) + (92 \times 0.40) + (100 \times 0.25) = 88.05$ | **88** |
| **Core CS Fundamentals (DSA/Systems)** | 90 | 15 | 100 | 100 | $(85 \times 0.35) + (100 \times 0.40) + (100 \times 0.25) = 94.75$ | **95** |
