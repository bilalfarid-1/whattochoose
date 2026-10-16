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
    skills_df = pd.DataFrame(raw['author_qualitative_skills_rubric']['skills_evaluations'])
    pasha_metrics = raw['pakistan_industry_benchmarks_2025_2026']
    milestones_df = pd.DataFrame(raw.get('swe_bench_milestones', []))
    
    # Export cleaned processed CSVs
    ts_df.to_csv(os.path.join(PROCESSED_DIR, 'time_series_metrics_2020_2026.csv'), index=False)
    skills_df.to_csv(os.path.join(PROCESSED_DIR, 'skills_lifecycle_metrics.csv'), index=False)
    if not milestones_df.empty:
        milestones_df.to_csv(os.path.join(PROCESSED_DIR, 'swe_bench_milestones.csv'), index=False)
    
    print("=" * 68)
    print("AUDITED MACROECONOMIC & INDUSTRY BENCHMARKS")
    print("=" * 68)
    
    # 1. Pakistan Export Growth Analysis
    exp_2020 = ts_df.loc[ts_df['year'] == 2020, 'pakistan_it_exports_billion_usd'].values[0]
    exp_2026 = ts_df.loc[ts_df['year'] == 2026, 'pakistan_it_exports_billion_usd'].values[0]
    exp_cagr = ((exp_2026 / exp_2020) ** (1/6) - 1) * 100
    print(f"Pakistan ICT Export Remittances: ${exp_2020:.2f}B (FY20) -> ${exp_2026:.2f}B (FY26 reported outturn)")
    print(f"Official ICT Exports 6-Year CAGR: +{exp_cagr:.2f}% per annum (~21.4%)")
    print("Sources: SBP, Finance Division, & APP July 2026 reported FY26 outturn (~$4.60B)")
    
    # 2. P@SHA Skills Survey 2025 Benchmarks
    print("\nP@SHA Skills Survey 2025 Industry Dynamics (Member Companies Scope):")
    print(f"- National annual CS/IT graduates estimate: ~{pasha_metrics['total_annual_cs_it_graduates_national_estimate']:,}")
    print(f"- Total hires across surveyed member companies (2024): {pasha_metrics['pasha_member_company_total_hires_2024']:,}")
    print(f"- Fresh graduate hires: {pasha_metrics['pasha_member_fresh_graduate_hires_2024']:,} ({pasha_metrics['fresher_intake_share_pasha_member_firms_pct']}%)")
    print(f"- Demand for experienced professionals: {pasha_metrics['experienced_professional_demand_share_pct']}%")
    print(f"- Direct Report PDF: {pasha_metrics['direct_report_pdf_url']}")
    
    # 3. Stack Overflow AI Adoption Metrics
    so_2023 = ts_df.loc[ts_df['year'] == 2023, 'global_ai_tool_engagement_pct'].values[0]
    so_2024 = ts_df.loc[ts_df['year'] == 2024, 'global_ai_tool_engagement_pct'].values[0]
    so_2025 = ts_df.loc[ts_df['year'] == 2025, 'global_ai_tool_engagement_pct'].values[0]
    print(f"\nDeveloper AI Tool Engagement (Stack Overflow Surveys):")
    print(f"- 2023: {so_2023}% (44% actively using, 26% planning to use)")
    print(f"- 2024: {so_2024}% (62% actively using, 14% planning to use)")
    print(f"- 2025: {so_2025}% (~84% using/planning, 51% daily use among professional devs)")
    
    # 4. FRED Indeed Software Postings Aggregates
    print("\nFRED Indeed U.S. Software Job Openings Index (IHLIDXUSTPSOFTDEVE):")
    for _, row in ts_df.iterrows():
        y = int(row['year'])
        mean_val = row['us_indeed_software_postings_index']
        min_val = row.get('us_postings_min')
        max_val = row.get('us_postings_max')
        count = row.get('us_postings_obs_count')
        print(f"- {y}: Mean {mean_val:.2f} (Min {min_val:.2f}, Max {max_val:.2f}, N={count})")

    # Generate transparent, professionally credible charts
    plot_figure_1_macro_trends(ts_df, milestones_df)
    plot_figure_2_skills_framework(skills_df)
    plot_figure_3_pakistan_dynamics(ts_df, pasha_metrics)
    plot_figure_4_developer_time_allocation()
    
    print("\n[SUCCESS] All figures successfully generated and saved to paper/figures/.")

def plot_figure_1_macro_trends(df, milestones_df=None):
    """Figure 1: Co-evolution of U.S. Software Postings and AI Benchmark Progression"""
    fig, ax1 = plt.subplots(figsize=(10.5, 6.0))
    
    color_postings = '#2b5c8f'
    color_swe_full = '#e67e22'
    color_swe_verified = '#8e44ad'
    color_ai = '#27ae60'
    
    # Left axis: Indeed U.S. Software Postings Index (FRED: IHLIDXUSTPSOFTDEVE)
    ax1.plot(df['year'], df['us_indeed_software_postings_index'], marker='o', color=color_postings, 
             linewidth=2.4, label='U.S. Software Postings Index (FRED IHLIDXUSTPSOFTDEVE, Feb 2020=100)')
    ax1.set_xlabel('Calendar Year', fontweight='bold')
    ax1.set_ylabel('U.S. Software Job Openings Index (Feb 2020=100)', color=color_postings, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_postings)
    ax1.set_ylim(40, 240)
    
    # Annotate key FRED economic inflection points
    ax1.annotate('Post-ZIRP Tech Peak\n(2022 Mean: 195.6)', xy=(2022, 195.59), xytext=(2020.8, 215),
                 arrowprops=dict(facecolor=color_postings, arrowstyle='->', lw=1.2),
                 fontsize=8.5, backgroundcolor='#ffffff')
    ax1.annotate('Post-ZIRP Stabilization\n(2024–2026 Mean: ~65–73)', xy=(2025, 65.05), xytext=(2023.2, 45),
                 arrowprops=dict(facecolor=color_postings, arrowstyle='->', lw=1.2),
                 fontsize=8.5, backgroundcolor='#ffffff')
    
    # Right axis: SWE-bench Discrete Milestones & AI Tool Engagement
    ax2 = ax1.twinx()
    
    # Developer AI Tool Engagement: Plot measured survey observations (2023-2025)
    so_mask = df['global_ai_tool_engagement_pct'].notna() & (df['ai_metric_measurement_type'] == 'survey_audited')
    ax2.plot(df.loc[so_mask, 'year'], df.loc[so_mask, 'global_ai_tool_engagement_pct'], marker='d', color=color_ai,
             linewidth=2.0, label='Developer AI Tool Use/Plan (Stack Overflow 2023–2025, %)')
             
    # Plot 2026 analytical projection as a distinct open point (not connected to survey measurements)
    proj_mask = df['ai_metric_measurement_type'] == 'author_projection'
    if proj_mask.any():
        ax2.scatter(df.loc[proj_mask, 'year'], df.loc[proj_mask, 'global_ai_tool_engagement_pct'],
                    marker='d', facecolors='none', edgecolors=color_ai, s=75, linewidth=1.8, zorder=5,
                    label='2026 Analytical Projection (88%, Author Scenario)')

    # Discrete SWE-bench Milestones (Scatter Points, Disconnected to prevent misleading continuity)
    # 1. 2023 SWE-bench Full Baseline (Claude 2: 1.96%, Oct 2023)
    ax2.scatter([2023], [1.96], color=color_swe_full, marker='s', s=80, zorder=6,
                label='SWE-bench Full Baseline (Claude 2: 1.96%, Oct 2023)')
    ax2.annotate('Claude 2\n(1.96% Full, N=2,294)', xy=(2023, 1.96), xytext=(2022.2, 9),
                 fontsize=7.8, color=color_swe_full, fontweight='bold',
                 arrowprops=dict(facecolor=color_swe_full, arrowstyle='->', lw=0.9))

    # 2. 2024 SWE-bench Verified Launch Milestones (Aug 13, 2024)
    ax2.scatter([2024, 2024], [38.8, 33.6], color=color_swe_verified, marker='^', s=85, zorder=6,
                label='SWE-bench Verified (Aug 2024: GPT-4o 38.8%, Sonnet 3.5 33.6%)')
    ax2.annotate('GPT-4o (38.8%)\nSonnet 3.5 (33.6%)', xy=(2024, 38.8), xytext=(2023.3, 44),
                 fontsize=7.8, color=color_swe_verified, fontweight='bold',
                 arrowprops=dict(facecolor=color_swe_verified, arrowstyle='->', lw=0.9))

    # 3. 2025 SWE-bench Verified Milestones (Feb 24, 2025)
    ax2.scatter([2025, 2025], [63.7, 70.3], color=color_swe_verified, marker='*', s=120, zorder=6,
                label='SWE-bench Verified (Feb 2025: Sonnet 3.7 70.3% High-Compute, 63.7% Base)')
    ax2.annotate('Sonnet 3.7 High-Compute (70.3%)\nBaseline (63.7%, N=489)', xy=(2025, 70.3), xytext=(2024.1, 75),
                 fontsize=7.8, color=color_swe_verified, fontweight='bold',
                 arrowprops=dict(facecolor=color_swe_verified, arrowstyle='->', lw=0.9))
                    
    ax2.set_ylabel('Benchmark Score & Developer Adoption (%)', color=color_swe_verified, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_swe_verified)
    ax2.set_ylim(0, 105)
    
    plt.title('Figure 1: U.S. Software Job Openings Index vs Discrete AI Benchmarks & Adoption (2020–2026)\n'
              '[Macroeconomic Co-Evolution | Sources: FRED (IHLIDXUSTPSOFTDEVE), Stack Overflow, SWE-bench Verified]', 
              fontsize=9.8, pad=12, fontweight='bold')
    
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, fontsize=8.0)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig1_junior_squeeze.png'), dpi=300)
    plt.close()

def plot_figure_2_skills_framework(skills_df):
    """Figure 2: Author-Assigned Qualitative Competency Valuation"""
    fig, ax = plt.subplots(figsize=(11, 6))
    
    domains = skills_df['skill_domain']
    trad = skills_df['pre_2022_weight']
    contemp = skills_df['contemporary_2026_weight']
    
    y = np.arange(len(domains))
    height = 0.35
    
    rects1 = ax.barh(y - height/2, trad, height, label='Author Pre-2022 Baseline Score', color='#95a5a6', alpha=0.85)
    rects2 = ax.barh(y + height/2, contemp, height, label='Author 2026 Horizon Score', color='#2980b9')
    
    ax.set_xlabel('Author-Assigned Qualitative Competency Weight (0–100 Scale)', fontweight='bold')
    ax.set_title('Figure 2: Author-Assigned Qualitative Competency Valuation (Pre-2022 vs 2026)\n'
                 '[Evaluated on Automation Exposure, Verification Necessity, and Interview Screening Frequency]', 
                 fontsize=10.5, pad=12, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels(domains, fontsize=9.2)
    ax.legend(loc='lower right', frameon=True)
    ax.set_xlim(0, 110)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig2_skills_lifecycle.png'))
    plt.close()

def plot_figure_3_pakistan_dynamics(df, pasha):
    """Figure 3: Pakistan ICT Exports Growth vs Member Company Demand"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={'width_ratios': [1.4, 1]})
    
    # Left subplot: SBP & Pakistan Economic Survey Export Receipts
    color_exp = '#1b4f72'
    bars = ax1.bar(df['year'], df['pakistan_it_exports_billion_usd'], color=color_exp, width=0.55, alpha=0.88)
    ax1.set_xlabel('Fiscal Year', fontweight='bold')
    ax1.set_ylabel('ICT Export Remittances ($B USD)', fontweight='bold')
    ax1.set_title('Pakistan ICT Export Remittances (FY20–FY26)\n[Source: State Bank of Pakistan, Finance Division & APP]', 
                  fontsize=10.5, pad=10, fontweight='bold')
    ax1.set_ylim(0, 5.5)
    
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'${height:.2f}B',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=8.5, fontweight='bold')
                     
    ax1.annotate('FY26: ~$4.60B reported outturn\n(+21.4% 6-Yr CAGR)',
                 xy=(2026, 4.60), xytext=(2021.6, 4.85),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2),
                 fontsize=8.5, backgroundcolor='#ffffff')
                 
    # Right subplot: P@SHA 2025 Hiring Demand Distribution (Member Companies Scope)
    labels = ['Experienced Professionals\n(71.8%)', 'Fresh Graduate Intake\n(28.2%)']
    sizes = [pasha['experienced_professional_demand_share_pct'], pasha['fresher_intake_share_pasha_member_firms_pct']]
    colors = ['#e67e22', '#3498db']
    
    wedges, texts, autotexts = ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
                                       colors=colors, textprops=dict(fontsize=9))
    plt.setp(autotexts, size=9.5, weight="bold", color="white")
    ax2.set_title('Member Company Hiring Demand (2024)\n[Sample: Surveyed P@SHA Member Firms, N=47,393]', 
                  fontsize=10.2, pad=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig3_pakistan_paradox.png'))
    plt.close()

def plot_figure_4_developer_time_allocation():
    """Figure 4: Author-Defined Conceptual Scenario of Software Engineer Labor Allocation"""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    
    categories = ['Pre-2022\n(Traditional Baseline)', '2024\n(Disruption Baseline)', '2026\n(Current Horizon)', '2028-2030\n(Projected Scenario)']
    
    # Illustrative scenario allocations (summing to 100%)
    manual_syntax = np.array([55, 35, 18, 10])
    verification_testing = np.array([15, 25, 38, 42])
    architecture_system_design = np.array([20, 22, 26, 30])
    ai_orchestration_evals = np.array([10, 18, 18, 18])
    
    width = 0.55
    ax.bar(categories, manual_syntax, width, label='Manual Syntax & Routine CRUD Coding', color='#e74c3c')
    ax.bar(categories, verification_testing, width, bottom=manual_syntax, label='Automated Testing, Verification & Debugging', color='#2ecc71')
    ax.bar(categories, architecture_system_design, width, bottom=manual_syntax + verification_testing, label='Systems Architecture, Data Modeling & API Design', color='#3498db')
    ax.bar(categories, ai_orchestration_evals, width, bottom=manual_syntax + verification_testing + architecture_system_design, label='AI Orchestration, Context Engineering & Evals', color='#9b59b6')
    
    ax.set_ylabel('Author-Defined Estimated Effort Allocation (%)', fontweight='bold')
    ax.set_title('Figure 4: Author-Defined Scenario of Software Labor Task Allocation (2020–2030)\n'
                 '[Illustrative Model: Transition from Syntax Transcription to Systems Verification]', 
                 fontsize=10.5, pad=12, fontweight='bold')
    ax.set_ylim(0, 105)
    ax.legend(loc='upper right', frameon=True, fontsize=8.8)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig4_predictive_2030_forecast.png'))
    plt.close()

if __name__ == '__main__':
    run_analysis()
