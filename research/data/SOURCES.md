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
* **Scope Boundary Note:** Because the surveyed companies ($47,393$ hires) and the national graduate estimate ($\sim 72,952$) cover different populations, their ratio ($13,350 / 72,952$) must **not** be interpreted as a national graduate employment rate. Graduates also find employment in non-member IT agencies, domestic banking/telecoms, public institutions, or international freelancing platforms. Furthermore, P@SHA's findings on tech demand (.NET, JavaScript full-stack, Python, relational DBs) reflect member enterprise portfolios and do not mathematically prove that Python is the single highest-probability stack for every graduate across all segments.

---

## 2. U.S. and Global Tech Labor Indicators

### 2.1 Software Development Job Postings (Indeed / FRED)
* **Primary Source:** Federal Reserve Bank of St. Louis (FRED) / Indeed Hiring Lab.
* **Series Identifier:** `IHLIDXUSTPSOFTDEVE` (*Software Development Job Postings on Indeed in the United States*).
* **Direct URL:** [https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE)
* **Single Snapshot File:** `research/data/raw/IHLIDXUSTPSOFTDEVE.csv` (retrieved 2026-10-16).
* **Geographic Scope:** **United States (Domestic Job Postings)**. It does not measure global or Pakistani job postings. We cite this as macroeconomic context reflecting capital expenditure and hiring sentiment within the world's largest software market.
* **Verifiable Annual Aggregates Computed from Raw Daily Snapshot (2,443 valid daily observations, 2020-02-01 to 2026-10-09):**
  - **2020 (Partial year, Feb 1 – Dec 31, 335 obs):** Mean = **78.91** (Min: 64.70, Max: 100.78). Note: 100.0 is the Feb 1, 2020 baseline value, not the annual mean.
  - **2021 (Full year, 365 obs):** Mean = **148.41** (Min: 90.54, Max: 217.96). Pandemic remote hiring acceleration.
  - **2022 (Full year, 365 obs):** Mean = **195.59** (Min: 130.51, Max: 233.83). All-time peak of post-ZIRP hiring expansion.
  - **2023 (Full year, 365 obs):** Mean = **90.40** (Min: 72.17, Max: 130.27). Post-ZIRP interest rate tightening and market correction.
  - **2024 (Full year, 366 obs):** Mean = **69.53** (Min: 66.53, Max: 72.58). Macroeconomic stabilization.
  - **2025 (Full year, 365 obs):** Mean = **65.05** (Min: 61.10, Max: 68.02). Post-bubble equilibrium.
  - **2026 (YTD snapshot through 2026-10-09, 282 obs):** Mean = **73.13** (Min: 66.92, Max: 78.34). Moderate normalization.
* **Offline Unit Test:** Verified in `research/tests/test_fred_aggregation.py`.

### 2.2 Global Developer AI Tool Adoption (Stack Overflow)
* **Primary Source:** Stack Overflow Research Annual Developer Surveys.
* **Sample Size:** 65,000 to 90,000+ respondents per survey wave.
* **Audited Survey Observations (Separated from Author Scenarios):**
  - **2023 Survey:** 44.0% actively using + 26.0% planning to use soon = **70.0%** broad engagement. Direct URL: [https://survey.stackoverflow.co/2023/#section-ai-ai-tools-in-development](https://survey.stackoverflow.co/2023/#section-ai-ai-tools-in-development)
  - **2024 Survey:** 62.0% actively using + 14.0% planning to use soon = **76.0%** broad engagement. Direct URL: [https://survey.stackoverflow.co/2024/technology#ai-tools-in-development](https://survey.stackoverflow.co/2024/technology#ai-tools-in-development)
  - **2025 Survey:** **51.0%** daily use among professional developers; ~84.0% using or planning to use. Direct URL: [https://survey.stackoverflow.co/2025/](https://survey.stackoverflow.co/2025/)
  - **2020–2022:** Unobserved via Stack Overflow developer surveys (pre-Copilot and pre-ChatGPT release). Removed from the empirical measurement series to avoid artificial jumps between ungrounded baseline estimates and survey instruments.
  - **2026:** Labeled explicitly as an **author analytical projection** (~88.0%) and not connected to empirical survey data in charts.

---

## 3. Computational Coding Benchmarks & Discrete Milestones Table

We present benchmark progress as discrete milestones with explicit models, scaffolds, task counts, denominators, and primary URLs, rather than an unbroken artificial trendline implying direct equivalence:

| Milestone ID | Benchmark Report Date | Model & Release Date | Source Revision Date | Agent Scaffold / Method | Benchmark Variant | Denominator | Observed Resolved Tasks / Expected Task Equivalents | Score (%) | Primary Source URL |
| :--- | :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `swe_full_2023_claude2` | 2023-10-10 | Claude 2 (2023-07-11) | 2023-10-10 | BM25 Retrieval + Prompt Baseline | SWE-bench Full | 2,294 | 45.0 | **1.96%** | [arXiv:2310.06770](https://arxiv.org/abs/2310.06770) |
| `swe_verified_2024_sonnet35`| 2024-08-13 | Claude 3.5 Sonnet (2024-06-20) | 2024-08-13 | SWE-agent scaffold (Yang et al.) | SWE-bench Verified | 500 | 168.0 | **33.6%** | [SWE-bench Leaderboard](https://www.swebench.com/) |
| `swe_verified_2024_gpt4o` | 2024-09-02 | GPT-4o (2024-05-13) | 2024-10-29 (v2) | Agentless scaffold (Xia et al.) | SWE-bench Verified | 500 | 194.0 | **38.8%** | [arXiv:2407.01489](https://arxiv.org/abs/2407.01489) |
| `swe_verified_2025_sonnet37_base` | 2025-02-24 | Claude 3.7 Sonnet (snapshot 2025-02-19, public launch 2025-02-24) | 2025-02-24 | Standard Unassisted Baseline | SWE-bench Verified (Evaluated) | 489 | 311.5 (Expected) | **63.7%** | [Anthropic Release](https://www.anthropic.com/news/claude-3-7-sonnet) |
| `swe_verified_2025_sonnet37_high` | 2025-02-24 | Claude 3.7 Sonnet (snapshot 2025-02-19, public launch 2025-02-24) | 2025-02-24 | Anthropic High-Compute Agent Scaffold | SWE-bench Verified (Evaluated) | 489 | 343.8 (Expected) | **70.3%** | [Anthropic Release](https://www.anthropic.com/news/claude-3-7-sonnet) |

### Benchmark Provenance Notes:
1. **Original SWE-bench 2023 Baseline:** The original benchmark release (Jimenez et al., ICLR 2024 / arXiv:2310.06770) evaluated 2,294 tasks across 12 repositories. Claude 2 resolved 45 tasks (1.96%), and GPT-4 resolved 40 tasks (1.74%). The previously cited 4.2% figure was an unverified secondary composite or Lite subset and is not comparable to full or verified evaluations.
2. **2024 Verified Launch & Agentless Comparative Evaluation (Source & Date Distinctions):**
   - **SWE-bench Verified Official Leaderboard Baseline (August 13, 2024):** The official SWE-bench Verified leaderboard (Princeton Language and Intelligence / PLI, [https://www.swebench.com/](https://www.swebench.com/)) evaluated launch scaffolds, recording 168/500 = 33.6% for Claude 3.5 Sonnet with SWE-agent (in comparison, OpenAI's launch post reported 33.2% for GPT-4o with an open scaffold).
   - **Agentless Evaluation vs. Paper Version Dates:** Xia et al. (*Agentless*, arXiv:2407.01489) evaluated Agentless with GPT-4o on SWE-bench Verified, achieving 194/500 = 38.8%. In our dataset, `evaluation_snapshot_date` records 2024-09-02 (the date of the evaluation run and leaderboard submission), distinguishing it from the initial arXiv release on 2024-07-01 (v1, which evaluated SWE-bench Lite) and the paper revision on 2024-10-29 (v2, documenting SWE-bench Verified results), while the underlying foundation model GPT-4o release date is preserved separately as 2024-05-13.
3. **Claude 3.7 Sonnet Evaluation, Model Snapshot & Expected Task Equivalents:**
   - **Date and Snapshot Clarification:** The underlying model snapshot identifier is `claude-3-7-sonnet-20250219` (internal build cutoff February 19, 2025), and Anthropic officially published the model and SWE-bench Verified evaluation report on February 24, 2025 (`2025-02-24`).
   - **Expected Task Equivalents:** Anthropic reported evaluations on 489 tasks due to 11 infrastructure-incompatible tasks in the environment (e.g., repository Docker container failures). The 70.3% score used test-time compute with parallel thinking and search tools, compared to 63.7% unassisted on that same 489-task subset. Fractional task values (343.8 and 311.5) represent expected task equivalents calculated from Pass@1 averages across repeated sampling trials over the 489 evaluated problems, not literal integer counts from a single run.
4. **2026 Benchmark Status:** Recorded as `null` / unobserved in our empirical time-series. While third-party agentic scaffolds continue to post experimental results to the public leaderboard, no single vetted foundation-model frontier milestone has been officially established as definitive for full calendar year 2026. To preserve empirical integrity, unverified point snapshots are omitted.
5. **Limits of Benchmark Evidence:** A rising benchmark score indicates progress on curated GitHub issue resolution within isolated Docker sandboxes. It does not prove that AI coding agents have replaced entry-level software engineers or caused market contraction.

---

## 4. Academic Literature & U.S. Labor Economics

* **Stanford Digital Economy Lab (Brynjolfsson, Chandar, & Chen, 2025; rev. 2026):**  
  *Citation:* Brynjolfsson, E., Chandar, B., & Chen, R. (2025; revised August 12, 2026). *Canaries in the Coal Mine: Six Facts About the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab. [https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)  
  *Finding:* Analyzes ADP payroll records covering millions of US private-sector employees. Employment among early-career workers (ages 22–25) in AI-exposed occupations was 19% below the trajectory it would have followed had it kept pace with less-exposed peers.  
  *Caveats:* This finding represents a descriptive relative employment shortfall among young workers in AI-exposed occupations rather than causal proof that AI caused a decline specifically in software-developer employment. Furthermore, the authors report no evidence of widespread, economy-wide job displacement. The study evaluates US domestic enterprise payrolls and does not measure Pakistani software export firm vacancy shares.
* **Tucker, Lee C. (April 2026):** *You're (not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators*. Working Paper CES-26-27, Center for Economic Studies, U.S. Census Bureau. [https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html)  
  *Finding:* Documents a statistically significant decline in early-career hiring in AI-exposed technical industries within the United States.
* **Autor, David (2024):** *Applying AI to Rebuild Middle-Class Jobs*, NBER Working Paper 32140. Analyzes task-biased cognitive automation and task boundaries.
* **Layoffs.fyi Tracker (Roger Lee):** Historical tech layoff counts: 2020 (80k), 2021 (15k), 2022 (165k), 2023 (263k peak), 2024 (152k), 2025 (98k), 2026 (~75k observed year-to-date through Q3 2026).

---

## 5. Author Qualitative Scoring Rubric & Calculation (Figure 2)

Figure 2 assigns qualitative ratings (0–100 scale) to evaluate software engineering competencies between the pre-2022 baseline and 2026. These scores are **author-assigned qualitative evaluations** representing a reasoned strategic stance, not census measurements or mathematical proofs of hiring probability.

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
