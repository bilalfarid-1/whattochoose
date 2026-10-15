import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configure clean, publication-grade styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['figure.dpi'] = 300

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'longitudinal_se_data.json')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'paper', 'figures')
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def run_analysis():
    raw = load_data()
    ts_df = pd.DataFrame(raw['time_series_data'])
    skills_df = pd.DataFrame(raw['analytical_skills_framework'])
    pasha_metrics = raw['pakistan_industry_benchmarks_2025_2026']
    
    # Export cleaned processed CSVs
    ts_df.to_csv(os.path.join(PROCESSED_DIR, 'time_series_metrics_2020_2026.csv'), index=False)
    skills_df.to_csv(os.path.join(PROCESSED_DIR, 'skills_lifecycle_metrics.csv'), index=False)
    
    print("=" * 60)
    print("RECONCILED EMPIRICAL DATA & BENCHMARKS")
    print("=" * 60)
    
    # 1. Pakistan Export Growth Analysis
    exp_2020 = ts_df.loc[ts_df['year'] == 2020, 'pakistan_it_exports_billion_usd'].values[0]
    exp_2026 = ts_df.loc[ts_df['year'] == 2026, 'pakistan_it_exports_billion_usd'].values[0]
    exp_cagr = ((exp_2026 / exp_2020) ** (1/6) - 1) * 100
    print(f"Pakistan ICT Exports: ${exp_2020:.2f}B (FY20) -> ${exp_2026:.2f}B (FY26 pacing)")
    print(f"Official ICT Exports 6-Year CAGR: +{exp_cagr:.2f}%")
    
    # 2. P@SHA Skills Survey 2025 Benchmarks
    print("\nP@SHA Skills Survey 2025 Industry Dynamics:")
    print(f"- Total annual CS/IT graduates: ~{pasha_metrics['total_annual_cs_it_graduates']:,}")
    print(f"- Member company hires (2024): {pasha_metrics['pasha_member_company_total_hires_2024']:,}")
    print(f"- Fresh graduate hires: {pasha_metrics['pasha_member_fresh_graduate_hires_2024']:,} ({pasha_metrics['fresher_intake_share_pct']}%)")
    print(f"- Demand for experienced professionals: {pasha_metrics['experienced_professional_demand_share_pct']}%")
    
    # 3. Time Series Correlation (Reported as descriptive association with acknowledged confounds)
    corr_ai_entry = ts_df['global_ai_tool_adoption_pct'].corr(ts_df['entry_level_postings_share_pct'])
    print(f"\nDescriptive Association (AI Adoption vs Entry-Level Share): r = {corr_ai_entry:.3f}")
    print("Note: Correlative association only. Confounded by ZIRP conclusion, tech layoffs, and macroeconomic normalization.")
    
    # Generate transparent, professionally credible charts
    plot_figure_1_macro_trends(ts_df)
    plot_figure_2_skills_framework(skills_df)
    plot_figure_3_pakistan_dynamics(ts_df, pasha_metrics)
    plot_figure_4_developer_time_allocation()
    
    print("\n[SUCCESS] All figures successfully generated and saved to paper/figures/.")

def plot_figure_1_macro_trends(df):
    """Figure 1: Co-evolution of Software Postings, Entry-Level Share, and AI Benchmarks"""
    fig, ax1 = plt.subplots(figsize=(10, 5.8))
    
    color_postings = '#2b5c8f'
    color_entry = '#c0392b'
    color_swe = '#8e44ad'
    
    # Left axis: Postings Index and Entry-Level Share
    ax1.plot(df['year'], df['indeed_software_postings_index'], marker='o', color=color_postings, 
             linewidth=2.2, label='Software Job Openings Index (2020=100)')
    ax1.plot(df['year'], df['entry_level_postings_share_pct'] * 2.5, marker='s', linestyle='--', color=color_entry, 
             linewidth=2.2, label='Entry-Level Postings Share (Scaled x2.5)')
    ax1.set_xlabel('Calendar Year', fontweight='bold')
    ax1.set_ylabel('Index / Scaled Postings Metric', color=color_postings, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_postings)
    ax1.set_ylim(0, 160)
    
    # Right axis: SWE-bench Verified Benchmark
    ax2 = ax1.twinx()
    ax2.plot(df['year'], df['swe_bench_verified_top_score_pct'], marker='^', color=color_swe, 
             linewidth=2.2, label='SWE-bench Verified Top Score (%)')
    ax2.plot(df['year'], df['global_ai_tool_adoption_pct'], marker='d', linestyle=':', color='#27ae60',
             linewidth=1.8, label='Developer AI Tool Adoption (%)')
    ax2.set_ylabel('Benchmark Score & Adoption (%)', color=color_swe, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_swe)
    ax2.set_ylim(0, 105)
    
    plt.title('Figure 1: Macro Software Hiring Trajectories vs AI Benchmark Progression (2020–2026)\n'
              '[Sources: Indeed Hiring Lab, Stack Overflow Surveys, Stanford HAI, SWE-bench]', 
              fontsize=11, pad=12, fontweight='bold')
    
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, fontsize=9)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig1_junior_squeeze.png'))
    plt.close()

def plot_figure_2_skills_framework(skills_df):
    """Figure 2: Analytical Competency Shift Model"""
    fig, ax = plt.subplots(figsize=(11, 6))
    
    domains = skills_df['skill_domain']
    trad = skills_df['traditional_value_pre_2022']
    contemp = skills_df['contemporary_value_2026']
    
    y = np.arange(len(domains))
    height = 0.35
    
    rects1 = ax.barh(y - height/2, trad, height, label='Traditional Market Weight (Pre-2022)', color='#95a5a6', alpha=0.85)
    rects2 = ax.barh(y + height/2, contemp, height, label='Contemporary Market Weight (2026)', color='#2980b9')
    
    ax.set_xlabel('Analytical Hiring & Competency Weight (0–100 Scale)', fontweight='bold')
    ax.set_title('Figure 2: Analytical Competency Shift Framework (Pre-2022 vs 2026)\n'
                 '[Evaluation of Automated Syntax vs Systems Verification & Architecture]', 
                 fontsize=11, pad=12, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels(domains, fontsize=9.5)
    ax.legend(loc='lower right', frameon=True)
    ax.set_xlim(0, 110)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig2_skills_lifecycle.png'))
    plt.close()

def plot_figure_3_pakistan_dynamics(df, pasha):
    """Figure 3: Pakistan ICT Exports Growth vs Industry Experience Demand"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={'width_ratios': [1.4, 1]})
    
    # Left subplot: SBP & Pakistan Economic Survey Export Receipts
    color_exp = '#1b4f72'
    bars = ax1.bar(df['year'], df['pakistan_it_exports_billion_usd'], color=color_exp, width=0.55, alpha=0.88)
    ax1.set_xlabel('Fiscal Year', fontweight='bold')
    ax1.set_ylabel('ICT Export Remittances ($B USD)', fontweight='bold')
    ax1.set_title('Pakistan ICT Export Remittance Growth (FY20–FY26)\n[Source: State Bank of Pakistan & Finance Division]', 
                  fontsize=10.5, pad=10, fontweight='bold')
    ax1.set_ylim(0, 5.5)
    
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'${height:.2f}B',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=8.5, fontweight='bold')
                     
    ax1.annotate('Record ~$4.6B pace\n(+21.4% 6-Yr CAGR)',
                 xy=(2026, 4.6), xytext=(2022.5, 4.8),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2),
                 fontsize=9, backgroundcolor='#ffffff')
                 
    # Right subplot: P@SHA 2025 Hiring Demand Distribution
    labels = ['Experienced Professionals\n(71.8%)', 'Fresh Graduate Intake\n(28.2%)']
    sizes = [pasha['experienced_professional_demand_share_pct'], pasha['fresher_intake_share_pct']]
    colors = ['#e67e22', '#3498db']
    
    wedges, texts, autotexts = ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
                                       colors=colors, textprops=dict(fontsize=9))
    plt.setp(autotexts, size=9.5, weight="bold", color="white")
    ax2.set_title('Measured Industry Hiring Demand by Seniority\n[Source: P@SHA Skills Survey 2025]', 
                  fontsize=10.5, pad=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig3_pakistan_paradox.png'))
    plt.close()

def plot_figure_4_developer_time_allocation():
    """Figure 4: Strategic Horizon (2026–2030): Estimated Software Engineer Task Allocation"""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    
    categories = ['Pre-2022\n(Traditional Era)', '2024\n(Disruption Era)', '2026\n(Current Horizon)', '2028-2030\n(Projected Horizon)']
    
    # Task allocations (summing to 100%)
    manual_syntax = np.array([55, 35, 18, 10])
    verification_testing = np.array([15, 25, 38, 42])
    architecture_system_design = np.array([20, 22, 26, 30])
    ai_orchestration_evals = np.array([10, 18, 18, 18])
    
    width = 0.55
    ax.bar(categories, manual_syntax, width, label='Manual Syntax & Routine Implementation', color='#e74c3c')
    ax.bar(categories, verification_testing, width, bottom=manual_syntax, label='Automated Verification, Testing & Debugging', color='#2ecc71')
    ax.bar(categories, architecture_system_design, width, bottom=manual_syntax + verification_testing, label='Systems Architecture, Data Modeling & API Design', color='#3498db')
    ax.bar(categories, ai_orchestration_evals, width, bottom=manual_syntax + verification_testing + architecture_system_design, label='AI Tool Orchestration & Context Engineering', color='#9b59b6')
    
    ax.set_ylabel('Estimated Engineer Effort & Time Allocation (%)', fontweight='bold')
    ax.set_title('Figure 4: The Changing Nature of Engineering Labor (Pre-2022 to 2030)\n'
                 '[Conceptual Model: The Transition from Code Author to Systems Verifier]', 
                 fontsize=11, pad=12, fontweight='bold')
    ax.set_ylim(0, 105)
    ax.legend(loc='upper right', frameon=True, fontsize=8.8)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig4_predictive_2030_forecast.png'))
    plt.close()

if __name__ == '__main__':
    run_analysis()
