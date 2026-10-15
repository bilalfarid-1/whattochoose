# Data Provenance & Primary Source Audit

This document provides transparent, verifiable provenance for all quantitative metrics, institutional publications, and analytical frameworks utilized in this repository.

---

## 1. Official Pakistani Economic & Industry Data

### 1.1 ICT Export Remittances (FY2020 – FY2026)
* **Primary Source 1:** State Bank of Pakistan (SBP), External Sector Statistics / Balance of Payments Division.
* **Primary Source 2:** Finance Division, Government of Pakistan, *Pakistan Economic Survey 2025–26*, Chapter 15: "Information Technology and Telecommunication".
* **Official Portals & Direct Links:**
  - SBP Data Services: [https://www.sbp.org.pk/ecodata/index2.asp](https://www.sbp.org.pk/ecodata/index2.asp)
  - Pakistan Economic Survey 2025–26 (ICT Chapter PDF): [https://finance.gov.pk/survey/chapter_26/15_Information_Technology.pdf](https://finance.gov.pk/survey/chapter_26/15_Information_Technology.pdf)

**Reported & Reconciled Figures:**
* **FY20 (2019-2020):** US$ 1.440 Billion (Official SBP baseline, as of 2020-12-31)
* **FY21 (2020-2021):** US$ 2.110 Billion (+46.5% pandemic remote surge, as of 2021-12-31)
* **FY22 (2021-2022):** US$ 2.620 Billion (+24.1%, as of 2022-12-31)
* **FY23 (2022-2023):** US$ 2.600 Billion (Macroeconomic adjustment & exchange rate volatility, as of 2023-12-31)
* **FY24 (2023-2024):** US$ 3.220 Billion (+23.8%, as of 2024-12-31)
* **FY25 (2024-2025):** US$ 3.812 Billion (Official full-year reported figure in Economic Survey, as of 2025-12-31)
* **FY26 (2025-2026):** **US$ 4.517 Billion (~US$ 4.52B) — Straight-Line Annualized Projection**  
  *Methodology & Arithmetic Derivation:*  
  The official Economic Survey (Table 15.1) records July–March FY2026 ICT remittances at **US$ 3.388 Billion** (a +19.7% YoY increase over the corresponding 9-month period of FY25).  
  Straight-line annualization across the full 12-month period is calculated as:
  $$\text{FY26 Projected Remittances} = 3.388 \times \frac{12}{9} \approx 4.5173\text{ Billion USD} \approx \$4.52\text{B}$$
  This is explicitly labeled as an annualized straight-line projection based on 9 months of audited data, not a finalized census figure.
* **Compound Annual Growth Rate (CAGR) Derivation:**  
  $$\text{CAGR} = \left(\frac{4.5173}{1.440}\right)^{\frac{1}{6}} - 1 = (3.1370)^{0.16667} - 1 \approx 20.98\% \approx 21.0\% \text{ per annum}$$

---

### 1.2 Pakistan IT Industry Employment & Graduate Supply
* **Primary Source:** Pakistan Software Houses Association (P@SHA), *P@SHA Skills Survey 2025*, P@SHA Research & Talent Committee.
* **Official Portal:** [https://pasha.org.pk/](https://pasha.org.pk/)

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
* **Aggregation Method:**
  - 2020: 100.0 (Index baseline, normalized to Feb 1, 2020)
  - 2021: 138.4 (Annual mean of monthly index observations)
  - 2022: 126.1 (Annual mean)
  - 2023: 76.8 (Annual mean following post-ZIRP tightening)
  - 2024: 68.4 (Annual mean)
  - 2025: 71.5 (Annual mean)
  - 2026: 72.5 (Observed year-to-date mean through mid-2026)

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

## 3. Computational Coding Benchmarks

* **Primary Source 1:** Stanford Institute for Human-Centered Artificial Intelligence (HAI), *The AI Index Annual Reports* (2022–2025). [https://aiindex.stanford.edu/report/](https://aiindex.stanford.edu/report/)
* **Primary Source 2:** Jimenez, C. E., et al. (ICLR 2024), *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* [https://www.swebench.com/](https://www.swebench.com/)
* **Primary Source 3:** Chen, M., et al. (2021), *Evaluating Large Language Models Trained on Code* (OpenAI Codex release).

**Benchmark Trajectory & Snapshots:**
* **2021:** HumanEval Pass@1 at 28.8% (Codex, July 2021).
* **2023:** HumanEval Pass@1 at 67.0% (GPT-4 launch). SWE-bench introduced (~4.2% resolution).
* **2024:** HumanEval Pass@1 reached 91.5% (approaching saturation). SWE-bench Verified launched (top agentic systems resolving 38.8% to 50%+).
* **2025–2026:** Autonomous multi-turn reasoning agents reaching 58.2% (mid-2025 snapshot) and 72.4% (mid-2026 snapshot on SWE-bench Verified leaderboard).

---

## 4. Academic Literature & U.S. Labor Economics

* **Tucker, Lee C. (April 2026):** *You're (not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators*. Working Paper CES-26-27, Center for Economic Studies, U.S. Census Bureau. [https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html)  
  *Key Finding:* Documents a statistically robust decline in early-career hiring in AI-exposed technical industries within the United States. Cited as macro empirical context for technological task exposure; does not directly measure Pakistan's labor market.
* **Autor, David (2024):** *Applying AI to Rebuild Middle-Class Jobs*, NBER Working Paper 32140. Analyzes task-biased cognitive automation and task boundaries.
* **Brynjolfsson, E., Li, D., & Raymond, L. R. (2023):** *Generative AI at Work*, Quarterly Journal of Economics (NBER WP 31161). Explores productivity compression across seniority levels.
* **Peng, S., et al. (2023):** *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, arXiv:2302.06590. Documents completion speed gains on routine programming tasks.
* **Layoffs.fyi Tracker (Roger Lee):** Historical tech layoff counts: 2020 (80k), 2021 (15k), 2022 (165k), 2023 (263k peak), 2024 (152k), 2025 (98k), 2026 (~75k observed year-to-date through Q3 2026).

---

## 5. Author Qualitative Scoring Rubric (Figure 2)

Figure 2 assigns qualitative ratings (0–100 scale) to evaluate software engineering competencies between the pre-2022 baseline and 2026. These scores are **author-assigned qualitative evaluations**, not census measurements.

### Scoring Criteria:
1. **Automation Exposure (Weight: 35%):** The degree to which frontier LLMs and agentic workflows can autonomously generate, refactor, or complete the task without human logic supervision. (Higher automation exposure = Lower human market premium).
2. **Verification Bottleneck Necessity (Weight: 40%):** The requirement for human architectural reasoning, schema formalization, security validation, and debugging of runtime edge cases. (Higher verification necessity = Higher human market premium).
3. **Technical Interview Screening Frequency (Weight: 25%):** The prevalence and strictness with which engineering leads and hiring committees test this competency during technical screening rounds.

### Rubric Breakdown:
* **Routine CRUD & Boilerplate (Pre-2022: 90 $\to$ 2026: 20):** High automation exposure; low verification complexity; low interview differentiation.
* **Manual Black-Box QA (Pre-2022: 80 $\to$ 2026: 25):** High automation exposure via synthetic test harnesses; lower entry-level compensation.
* **Backend Systems Architecture (Pre-2022: 75 $\to$ 2026: 92):** Low automation exposure for domain-specific schemas; high verification demand for ACID transactions and indexing; mandatory screening requirement.
* **Automated Testing & Systems Verification (Pre-2022: 55 $\to$ 2026: 95):** The primary bottleneck for AI-generated code; high verification demand; core differentiator for candidates.
* **Core CS Fundamentals / DSA (Pre-2022: 90 $\to$ 2026: 95):** Critical for algorithmic complexity evaluation and runtime performance; standard screening filter across top employers.
