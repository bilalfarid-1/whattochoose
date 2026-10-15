# Data Provenance & Primary Source Audit

This document provides transparent, verifiable provenance for all quantitative metrics, institutional publications, and analytical frameworks utilized in this repository.

---

## 1. Official Pakistani Economic & Industry Data

### 1.1 ICT Export Remittances (FY2020 – FY2026)
* **Primary Source 1:** State Bank of Pakistan (SBP), External Sector Statistics / Balance of Payments Division.
* **Primary Source 2:** Finance Division, Government of Pakistan, *Pakistan Economic Survey 2025–26*.
* **Official Portals:**
  - SBP Data Services: [https://www.sbp.org.pk/ecodata/index2.asp](https://www.sbp.org.pk/ecodata/index2.asp)
  - Finance Division Economic Surveys: [https://www.finance.gov.pk/survey_economy.html](https://www.finance.gov.pk/survey_economy.html)

**Reported & Reconciled Figures:**
* **FY20 (2019-2020):** US$ 1.44 Billion
* **FY21 (2020-2021):** US$ 2.11 Billion (+46.5% pandemic surge)
* **FY22 (2021-2022):** US$ 2.62 Billion (+24.1%)
* **FY23 (2022-2023):** US$ 2.60 Billion (Macroeconomic adjustment & exchange rate volatility)
* **FY24 (2023-2024):** US$ 3.22 Billion (+23.8%)
* **FY25 (2024-2025):** US$ 3.812 Billion (Official full-year reported figure)
* **FY26 (2025-2026):** Pacing at record ~US$ 4.6 Billion (Based on official July–March FY26 receipts of US$ 3.388 Billion, up 19.7% YoY per the Pakistan Economic Survey 2025–26)
* **Compound Annual Growth Rate (CAGR):**
  $$\text{CAGR} = \left(\frac{4.60}{1.44}\right)^{\frac{1}{6}} - 1 \approx 21.36\% \text{ per annum}$$

---

### 1.2 Pakistan IT Industry Employment & Graduate Supply
* **Primary Source:** Pakistan Software Houses Association (P@SHA), *P@SHA Skills Survey 2025*.
* **Official Portal:** [https://pasha.org.pk/](https://pasha.org.pk/)

**Audited Benchmark Metrics:**
* **Annual CS/IT Graduates:** Estimated at approximately **72,952** graduates per year across Pakistani universities.
* **Hiring by P@SHA Member Companies (2024):** **47,393** total hires across surveyed firms.
* **Fresh Graduate Intake:** **13,350** of those hires were fresh graduates (~28.17% of total company hiring).
* **Experience Bias:** Approximately **71.83%** of measured hiring demand is for experienced professionals (mid-level and senior), creating an acute barrier to entry for candidates with unverified or routine skillsets.

---

## 2. Global Developer Tool Adoption & Market Sentiment

### 2.1 Stack Overflow Annual Developer Surveys (2023 & 2024)
* **Source:** Stack Overflow Research. Sample size: 65,000 to 90,000+ respondents per survey wave.
* **Official URLs:**
  - 2023 Survey: [https://survey.stackoverflow.co/2023/#section-ai-ai-tools](https://survey.stackoverflow.co/2023/#section-ai-ai-tools)
  - 2024 Survey: [https://survey.stackoverflow.co/2024/ai#ai-tools](https://survey.stackoverflow.co/2024/ai#ai-tools)

**Audited Observations:**
* **2023:** 44.0% of respondents reported actively using AI tools in their development process, with an additional 26.0% planning to do so soon (70.0% total interest/usage).
* **2024:** 62.0% reported actively using AI coding tools, with 14.0% planning to use them soon (76.0% total engagement).
* *Note on 2020–2022 Baseline:* Stack Overflow did not include a dedicated "AI Developer Tools" section prior to 2023. Figures for 2020–2022 in our dataset are analytical author baselines reflecting early IDE extension adoption.

---

## 3. Computational Coding Benchmarks

### 3.1 HumanEval & SWE-bench Verified
* **Primary Source 1:** Stanford Institute for Human-Centered Artificial Intelligence (HAI), *The AI Index Annual Reports* (2022–2025). [https://aiindex.stanford.edu/report/](https://aiindex.stanford.edu/report/)
* **Primary Source 2:** Jimenez, C. E., et al. (ICLR 2024), *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* [https://www.swebench.com/](https://www.swebench.com/)
* **Primary Source 3:** Chen, M., et al. (2021), *Evaluating Large Language Models Trained on Code* (OpenAI Codex release).

**Audited Benchmarks:**
* **2021:** HumanEval Pass@1 at 28.8% (Codex).
* **2023:** HumanEval Pass@1 at 67.0% (GPT-4 launch). SWE-bench introduced (~4.2% resolution).
* **2024:** HumanEval Pass@1 reached 91.5% (approaching saturation). SWE-bench Verified launched (top agentic systems resolving 38.8% to 50%+).
* **2025–2026:** Autonomous multi-turn reasoning agents reaching 58% to 72%+ on SWE-bench Verified.

---

## 4. Labor Economics, Macroeconomic Trends & Confounding Factors

To ensure intellectual rigor, this research accounts for major confounding variables:

1. **Macroeconomic Tightening & The End of ZIRP (2022–2024):**
   * The conclusion of the Zero Interest-Rate Policy (ZIRP) era substantially increased the cost of venture capital, prompting software firms globally to shift from speculative growth and over-hiring to operational profitability.
   * *Data Source:* [Layoffs.fyi](https://layoffs.fyi/) tracked over 165,000 tech layoffs in 2022 and 263,000 in 2023.
2. **Early-Career Hiring Dynamics in AI-Exposed Sectors:**
   * *US Census Bureau Working Paper (2025):* Investigates early-career hiring shifts in AI-exposed industries following ChatGPT's release, analyzing both technological displacement and post-pandemic macroeconomic normalization.
3. **Firm-Level Productivity & Hiring Associations:**
   * *Wiley / Academic Studies on Copilot Adoption (2026):* Found that firm adoption of GitHub Copilot was associated with higher monthly probability of hiring software engineers in certain adopting enterprises, demonstrating that AI does not simply destroy jobs universally, but restructures tasks and raises the competence baseline.

---

## 5. Methodological Classification

In `data/raw/longitudinal_se_data.json`:
* All audited institutional numbers are clearly tagged with their exact publication source.
* All qualitative skill-weight frameworks are explicitly labeled as **analytical models**, rather than misrepresented as census measurements.
