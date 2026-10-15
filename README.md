# The Shifting Landscape of Entry-Level Software Engineering: An Empirical Market Analysis and Strategic Guide for Pakistani Graduates

**Author:** Muhammad Bilal Farid  
*BS Software Engineering Graduate & Independent Technology Analyst*  
*Lahore, Pakistan*  

---

## Overview

This repository provides an empirical market analysis and practical career playbook evaluating how generative AI, post-pandemic macroeconomic normalization, and offshore industry dynamics are transforming the software engineering labor market—with a specific focus on fresh graduates in Pakistan.

---

## Repository Structure

```
whattochoose/
│
├── README.md                           # This document
├── requirements.txt                    # Python runtime dependencies (pandas, matplotlib, numpy, scipy)
│
├── data/                               # Harmonized empirical datasets
│   ├── SOURCES.md                      # Data provenance & source audit (official URLs, report sections)
│   ├── README.md                       # Data directory summary
│   ├── raw/
│   │   └── longitudinal_se_data.json   # Multi-year metrics (SBP, Pakistan Economic Survey, P@SHA, Stack Overflow, BLS)
│   └── processed/
│       ├── time_series_metrics_2020_2026.csv
│       └── skills_lifecycle_metrics.csv
│
├── src/                                # Reproducible Python analytical pipeline
│   └── analyze_market_dynamics.py      # Statistical modeling and figure generation
│
├── tests/                              # Automated data integrity & arithmetic tests
│   └── test_data_integrity.py          # Verifies schema, CAGR arithmetic, and source metadata
│
├── paper/                              # Market Analysis Manuscript & Visuals
│   ├── main_manuscript.md              # Complete research whitepaper & market brief
│   ├── references.bib                  # Academic BibTeX reference library
│   └── figures/                        # High-resolution figures (300 DPI)
│       ├── fig1_junior_squeeze.png     # U.S. software postings vs AI benchmark progression
│       ├── fig2_skills_lifecycle.png   # Author-assigned qualitative competency valuation
│       ├── fig3_pakistan_paradox.png   # Pakistan ICT export revenue vs member company demand
│       └── fig4_predictive_2030_forecast.png # Author-defined scenario of developer task allocation
│
└── roadmap/                            # Practical Graduate Deliverables
    ├── 2026_graduate_readiness_matrix.md # Skills triage: low-leverage vs AI-augmented vs high-leverage core
    └── pakistani_fresh_grad_playbook.md  # 90-day step-by-step execution protocol for Pakistani graduates
```

---

## Core Findings Summary

1. **Pakistan ICT Export Growth vs. Experience Bias:**  
   Pakistan's ICT export remittances have sustained rapid expansion, growing from $\$1.440\text{B}$ (FY20) to an official straight-line annualized pace of **$\sim \$4.52\text{B}$** in FY26 (**$+21.0\%$ 6-year CAGR** per SBP & Finance Division reports). However, according to the P@SHA Skills Survey 2025, approximately **$71.8\%$** of industry hiring demand across surveyed member firms is concentrated in experienced roles, creating an intense qualification filter for fresh graduates.
2. **The Verification Bottleneck:**  
   While AI models commoditize routine syntax and boilerplate code generation, the primary engineering constraint has shifted to **Specification Formalization**, **Relational Data Architecture**, and **Automated Verification / Integration Testing**.
3. **The Importance of Technical Depth (Reasoned Strategic Choice):**  
   In a competitive entry-level market, surface-level familiarity across multiple stacks offers minimal hiring signal. Committing deeply to a robust backend stack (**Python / FastAPI + PostgreSQL + PyTest**) and shipping a verifiable, deployed project provides a disciplined, high-leverage foundation to secure entry-level employment.

---

## Reproducing the Analysis Pipeline

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Execute analysis pipeline
python src/analyze_market_dynamics.py
```

All charts are generated and exported to `paper/figures/` at 300 DPI.

---

## Suggested Citation

```bibtex
@techreport{farid2026se_market,
  title = {The Shifting Landscape of Entry-Level Software Engineering: An Empirical Market Analysis and Strategic Guide for Pakistani Graduates},
  author = {Farid, Muhammad Bilal},
  institution = {Independent Technology Analysis},
  year = {2026},
  url = {https://github.com/bilalfarid-1/whattochoose}
}
```
