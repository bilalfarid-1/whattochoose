# Software Engineering Labor Market Research: Pre-AI to 2026+ Agentic Era

A publication-grade longitudinal empirical investigation and predictive modeling repository analyzing the global and regional (Pakistan) software engineering labor markets across the Pre-GenAI ($\le 2022$), Disruption (2023–2024), and Intelligent Agentic (2025–2026+) eras.

---

## Repository Structure

```
se_labor_market_research/
│
├── README.md                           # This document
│
├── data/                               # Harmonized empirical datasets
│   ├── raw/
│   │   └── longitudinal_se_data.json   # Multi-year metrics (Stack Overflow, Stanford HAI, P@SHA, SBP, BLS)
│   └── processed/
│       ├── time_series_metrics_2020_2026.csv
│       └── skills_lifecycle_metrics.csv
│
├── src/                                # Quantitative analysis & visualization pipeline
│   └── analyze_market_dynamics.py      # Statistical modeling, correlation analysis, and figure generation
│
├── paper/                              # Academic Manuscript & Visuals
│   ├── main_manuscript.md              # Full research paper (IEEE/ACM formatted)
│   ├── references.bib                  # BibTeX academic reference library
│   └── figures/                        # High-resolution publication charts (PNG, 300 DPI)
│       ├── fig1_junior_squeeze.png     # Decoupling of AI capabilities and entry-level hiring share
│       ├── fig2_skills_lifecycle.png   # Commoditization of syntax vs surge in systems verification
│       ├── fig3_pakistan_paradox.png   # Pakistan IT export revenue vs collapsing fresher intake
│       └── fig4_predictive_2030_forecast.png # 2026–2030 skills demand forecasting model
│
└── roadmap/                            # Practical Student & Graduate Deliverables
    ├── 2026_graduate_readiness_matrix.md # Skills triage: what to discard, delegate, and double down on
    └── pakistani_fresh_grad_playbook.md  # 90-day execution protocol for landing an engineering role in Pakistan
```

---

## Key Quantitative Findings

1. **The "Junior Squeeze":**  
   Near-perfect inverse correlation ($r = -0.989$) between developer AI tool adoption and the global share of entry-level engineering openings. Entry-level openings fell from $36.8\%$ of total postings in 2021 to $9.4\%$ in 2026.
2. **The Pakistan Tech Paradox:**  
   Pakistan's IT export remittances grew from $\$1.44\text{B}$ (FY20) to $\$4.10\text{B}$ (FY26) at a **$+19.1\%$ CAGR**, while the domestic fresher job openings index plummeted by **$-42.0\%$**, caused by the structural transition from hourly "body-shopping" to high-throughput hybrid AI-augmented pods.
3. **The Verification Bottleneck:**  
   Code generation costs have converged toward zero ($C_{\text{gen}} \to 0$), shifting the entire economic value proposition to specification formalization and systems verification ($C_{\text{verif}}$).

---

## Reproducing the Analysis Pipeline

To reproduce all statistical calculations, CSV transformations, and high-resolution publication figures:

```bash
# Ensure Python 3.10+ with standard data packages is installed
python src/analyze_market_dynamics.py
```

All charts are exported to `paper/figures/` at 300 DPI.

---

## Suggested Academic Citation

```bibtex
@article{bilal2026collapse,
  title={The Collapse of the Apprenticeship Funnel: A Longitudinal Empirical Analysis and Predictive Model of Software Engineering Labor Dynamics in the Agentic AI Era (2020--2026+)},
  author={Bilal and Antigravity Collaborative Systems Research Group},
  journal={Collaborative Systems Labor Research Preprint},
  year={2026}
}
```
