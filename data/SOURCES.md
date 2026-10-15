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
* **FY20 (2019-2020):** US$ 1.44 Billion (Official SBP baseline)
* **FY21 (2020-2021):** US$ 2.11 Billion (+46.5% pandemic remote surge)
* **FY22 (2021-2022):** US$ 2.62 Billion (+24.1%)
* **FY23 (2022-2023):** US$ 2.60 Billion (Macroeconomic adjustment & exchange rate volatility)
* **FY24 (2023-2024):** US$ 3.22 Billion (+23.8%)
* **FY25 (2024-2025):** US$ 3.812 Billion (Official full-year reported figure in Economic Survey)
* **FY26 (2025-2026):** **US$ 4.60 Billion (Annualized Projection)**  
  *Methodology Note:* The official Economic Survey records July–March FY2026 ICT remittances at US$ 3.388 Billion (a +19.7% YoY increase over the corresponding period of FY25). Annualizing this 9-month run rate yields a projected full-year outturn of approximately US$ 4.6 Billion. This is clearly labeled as an annualized projection, not a finalized census figure.
* **Compound Annual Growth Rate (CAGR):**
  $$\text{CAGR} = \left(\frac{4.60}{1.44}\right)^{\frac{1}{6}} - 1 \approx 21.36\% \text{ per annum}$$

---

### 1.2 Pakistan IT Industry Employment & Graduate Supply
* **Primary Source:** Pakistan Software Houses Association (P@SHA), *P@SHA Skills Survey 2025*.
* **Official Portal:** [https://pasha.org.pk/](https://pasha.org.pk/)

**Audited Benchmark Metrics & Scope Boundaries:**
* **Survey Scope:** Data reflects surveyed P@SHA member enterprises, representing Pakistan's organized software export and IT services sector. It does not constitute a full census of informal, freelance, or non-member firms.
* **Annual CS/IT Graduates:** Estimated at approximately **72,952** graduates per year across all Pakistani universities.
* **Hiring by Surveyed Member Companies (2024):** **47,393** total hires across participating companies.
* **Fresh Graduate Intake:** **13,350** of those hires were fresh graduates (representing **28.17%** of member company hiring).
* **Experience Preference:** Approximately **71.83%** of measured hiring demand across member firms is targeted at experienced professionals (mid-level and senior).

---

## 2. Global Developer Tool Adoption & Market Sentiment

### 2.1 Stack Overflow Annual Developer Surveys (2023, 2024, 2025)
* **Source:** Stack Overflow Research. Sample sizes: 65,000 to 90,000+ respondents per survey wave.
* **Metric Definition:** "Using or planning to use AI tools in the software development process" (Broad engagement) vs. "Daily active professional use".
* **Official URLs:**
  - [Stack Overflow 2023 Developer Survey - AI Section](https://survey.stackoverflow.co/2023/#section-ai-ai-tools)
  - [Stack Overflow 2024 Developer Survey - AI Tools](https://survey.stackoverflow.co/2024/ai#ai-tools)
  - [Stack Overflow 2025 AI Survey](https://survey.stackoverflow.co/2025/ai)

**Audited Observations:**
* **2023 Survey:** 44.0% actively using + 26.0% planning to use = **70.0%** broad engagement.
* **2024 Survey:** 62.0% actively using + 14.0% planning to use = **76.0%** broad engagement.
* **2025 AI Survey:** **84.0%** using or planning to use AI tools; **51.0%** of professional developers report daily AI tool usage.
* **2020–2022 Baselines:** Labeled explicitly as **author historical baselines** (2.0%, 5.0%, 8.5%), as Stack Overflow did not include a dedicated AI tool survey module prior to 2023.
* **2026 Value:** Labeled explicitly as an **author analytical projection** (~88.0%).

---

## 3. Computational Coding Benchmarks

* **Primary Source 1:** Stanford Institute for Human-Centered Artificial Intelligence (HAI), *The AI Index Annual Reports* (2022–2025). [https://aiindex.stanford.edu/report/](https://aiindex.stanford.edu/report/)
* **Primary Source 2:** Jimenez, C. E., et al. (ICLR 2024), *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* [https://www.swebench.com/](https://www.swebench.com/)
* **Primary Source 3:** Chen, M., et al. (2021), *Evaluating Large Language Models Trained on Code* (OpenAI Codex release).

**Audited Benchmarks:**
* **2021:** HumanEval Pass@1 at 28.8% (Codex).
* **2023:** HumanEval Pass@1 at 67.0% (GPT-4 launch). SWE-bench introduced (~4.2% resolution).
* **2024:** HumanEval Pass@1 reached 91.5% (approaching saturation). SWE-bench Verified launched (top agentic systems resolving 38.8% to 50%+).
* **2025–2026:** Autonomous multi-turn reasoning agents reaching 58% to 72%+ on SWE-bench Verified.

---

## 4. Labor Economics & Macroeconomic Evidence

1. **U.S. Empirical Evidence on Early-Career Hiring:**
   * **Citation:** Tucker, Lee C. (April 2026). *You're (not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators*. Working Paper CES-26-27, Center for Economic Studies, U.S. Census Bureau.
   * **Official URL:** [https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html)
   * **Context & Scope:** This study provides rigorous empirical evidence showing an early-career hiring contraction in AI-exposed sectors within the United States. We cite this as macroeconomic context regarding technological exposure, noting explicitly that it does not measure Pakistan's domestic labor market directly.
2. **Firm-Level Adoption & Software Hiring:**
   * *Wiley / Academic Studies on Copilot Adoption (2026):* Found that firm-level adoption of GitHub Copilot was associated with a higher probability of hiring software engineers in certain adopting enterprises, illustrating that AI can expand software throughput while changing the nature of demanded skills.
3. **Macroeconomic Tightening & The End of ZIRP:**
   * [Layoffs.fyi](https://layoffs.fyi/) recorded over 165,000 tech layoffs in 2022 and 263,000 in 2023 following the conclusion of Zero Interest-Rate Policies, highlighting that entry-level tech hiring friction is heavily driven by capital costs and post-pandemic over-hiring corrections.

---

## 5. Classification of Entry-Level Hiring & 2030 Scenarios

* **Entry-Level Postings Share Series:** Classified explicitly as an **Author Illustrative Index** based on normalized job board observations (Indeed Hiring Lab, CompTIA reports), not an audited global census. Accordingly, we do not claim a verified statistical causal correlation between AI adoption and junior hiring.
* **Figure 4 (2020–2030 Horizon):** Classified explicitly as an **Author-Defined Conceptual Scenario** illustrating the structural shift from manual syntax drafting to systems verification and architecture.
