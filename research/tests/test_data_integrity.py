import json
import os
import re

DATE_REGEX = re.compile(r'^\d{4}-\d{2}-\d{2}$')

def test_data_integrity():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'data', 'raw', 'longitudinal_se_data.json')
    
    assert os.path.exists(json_path), f"Missing data file: {json_path}"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    ts = data['time_series_data']
    assert len(ts) == 7, f"Expected 7 annual records (2020-2026), found {len(ts)}"
    
    # 1. Verify Pakistan Export Arithmetic (Reported FY26: $4.60B)
    exp_2020 = [r for r in ts if r['year'] == 2020][0]['pakistan_it_exports_billion_usd']
    exp_2026 = [r for r in ts if r['year'] == 2026][0]['pakistan_it_exports_billion_usd']
    
    assert abs(exp_2026 - 4.60) < 0.01, f"Expected 4.60B reported figure, found {exp_2026}"
    
    # Check 6-year CAGR: ((4.60 / 1.44) ** (1/6) - 1) * 100 = 21.36%
    calculated_cagr = ((exp_2026 / exp_2020) ** (1.0 / 6.0) - 1.0) * 100.0
    recorded_cagr = data['pakistan_industry_benchmarks_2025_2026']['export_revenue_cagr_fy20_to_fy26_pct']
    assert abs(calculated_cagr - recorded_cagr) < 0.05, f"CAGR mismatch: {calculated_cagr} vs {recorded_cagr}"
    assert abs(calculated_cagr - 21.36) < 0.05, f"Expected ~21.4% CAGR, got {calculated_cagr}"
    
    # 2. Verify P@SHA Ratios and Direct Link
    pasha = data['pakistan_industry_benchmarks_2025_2026']
    total_hires = pasha['pasha_member_company_total_hires_2024']
    fresh_hires = pasha['pasha_member_fresh_graduate_hires_2024']
    expected_fresh_pct = (fresh_hires / total_hires) * 100.0
    recorded_fresh_pct = pasha['fresher_intake_share_pasha_member_firms_pct']
    assert abs(expected_fresh_pct - recorded_fresh_pct) < 0.1, "P@SHA fresher share mismatch"
    assert "Skills-Survey-2025.pdf" in pasha['direct_report_pdf_url']
    
    # 3. Verify Date Formats and Temporal/Provenance Metadata
    required_temporal_fields = [
        'as_of_date', 
        'observation_period_start', 
        'observation_period_end', 
        'data_retrieved_at',
        'export_measurement_type',
        'ai_metric_measurement_type',
        'us_postings_measurement_type',
        'us_postings_min',
        'us_postings_max',
        'us_postings_obs_count'
    ]
    
    for row in ts:
        year = row['year']
        for field in required_temporal_fields:
            assert field in row, f"Missing '{field}' in time series record for year {year}"
            
        # Verify ISO date regex (YYYY-MM-DD)
        for date_key in ['as_of_date', 'observation_period_start', 'observation_period_end', 'data_retrieved_at']:
            val = row[date_key]
            assert DATE_REGEX.match(val), f"Field '{date_key}' value '{val}' does not match YYYY-MM-DD in year {year}"
            
        # Ensure observation period start <= end
        assert row['observation_period_start'] <= row['observation_period_end'], f"Invalid period range for year {year}"
        
        # Verify min <= mean <= max bounding for FRED postings
        postings_val = row['us_indeed_software_postings_index']
        assert row['us_postings_min'] <= postings_val <= row['us_postings_max'], f"Bounding invariant failed for year {year}"
        
    # Verify specific 2026 temporal distinction: snapshot ending 2026-10-09 vs data retrieved in October
    row_2026 = [r for r in ts if r['year'] == 2026][0]
    assert row_2026['observation_period_end'] == "2026-10-09", "2026 snapshot should have observation_period_end: 2026-10-09"
    assert row_2026['data_retrieved_at'] == "2026-10-16", "2026 data_retrieved_at should be 2026-10-16"
    
    # 4. Verify SWE-bench Benchmark Provenance and Null Handling
    # SWE-bench Verified was launched August 13, 2024. Observations for 2020-2023 and 2026 MUST be null.
    for row in ts:
        year = row['year']
        # Ensure deprecated top_score fields do not exist
        assert 'swe_bench_verified_top_score_pct' not in row, f"Found deprecated top_score field in year {year}"
        assert 'swe_bench_original_top_score_pct' not in row, f"Found deprecated top_score field in year {year}"
        
        if year in [2024, 2025]:
            assert isinstance(row['swe_bench_verified_selected_milestone_pct'], (int, float)), f"Expected numeric Verified score in {year}"
            assert row['swe_bench_verified_selected_milestone_pct'] > 0.0, f"Expected non-zero Verified score in {year}"
            assert row['benchmark_swe_verified_model'] is not None, f"Missing benchmark_swe_verified_model in {year}"
            assert DATE_REGEX.match(row['benchmark_swe_verified_snapshot_date']), f"Invalid snapshot date in {year}"
        else:
            assert row['swe_bench_verified_selected_milestone_pct'] is None, (
                f"SWE-bench Verified must be null for unobserved/ongoing year {year}, found: {row['swe_bench_verified_selected_milestone_pct']}"
            )
            assert row['benchmark_swe_verified_model'] is None, f"benchmark_swe_verified_model must be null in {year}"
            assert row['benchmark_swe_verified_snapshot_date'] is None, f"benchmark_swe_verified_snapshot_date must be null in {year}"
            
        # Original SWE-bench was introduced in late 2023
        if year == 2023:
            assert abs(row['swe_bench_original_selected_milestone_pct'] - 1.96) < 0.01, "Expected 1.96% verified Claude 2 baseline in 2023"
        else:
            assert row['swe_bench_original_selected_milestone_pct'] is None, f"swe_bench_original_selected_milestone_pct should be null in {year}"
            
    # Verify discrete SWE-bench milestones table exists
    assert 'swe_bench_milestones' in data, "Missing swe_bench_milestones table"
    assert len(data['swe_bench_milestones']) >= 4, "Expected at least 4 discrete SWE-bench milestones"
    for m in data['swe_bench_milestones']:
        assert 'denominator' in m and m['denominator'] > 0
        assert 'score_pct' in m and m['score_pct'] > 0
        assert 'primary_source_url' in m and m['primary_source_url'].startswith('http')
        assert 'benchmark_report_date' in m and len(m['benchmark_report_date']) == 10
        assert 'source_revision_date' in m and len(m['source_revision_date']) == 10
        assert 'model_release_date' in m and len(m['model_release_date']) == 10
        assert 'date_clarification' in m and len(m['date_clarification']) > 10

    # Explicitly verify Agentless date distinction: evaluation snapshot (2024-09-02), arXiv v1 (2024-07-01), arXiv v2 (2024-10-29), model release (2024-05-13)
    agentless_m = next(m for m in data['swe_bench_milestones'] if m['milestone_id'] == 'swe_verified_2024_gpt4o')
    assert agentless_m['benchmark_report_date'] == '2024-09-02'
    assert agentless_m['evaluation_snapshot_date'] == '2024-09-02'
    assert agentless_m['source_revision_date'] == '2024-10-29'
    assert agentless_m['arxiv_v1_date'] == '2024-07-01'
    assert agentless_m['arxiv_v2_date'] == '2024-10-29'
    assert agentless_m['model_release_date'] == '2024-05-13'

    # Verify Claude 3.5 Sonnet Verified leaderboard attribution and peer-reviewed corroboration
    sonnet_m = next(m for m in data['swe_bench_milestones'] if m['milestone_id'] == 'swe_verified_2024_sonnet35')
    assert 'swebench.com' in sonnet_m['primary_source_url']
    assert 'SWE-bench Official Leaderboard' in sonnet_m['citation']
    assert 'proceedings.neurips.cc' in sonnet_m['peer_reviewed_source_url']
    assert 'NeurIPS 2025' in sonnet_m['peer_reviewed_citation']
        
    # Verify Stanford Digital Economy Lab early career research section exists with verified authors and title
    assert 'stanford_adp_early_career_employment_research' in data
    s_res = data['stanford_adp_early_career_employment_research']
    assert 'Brynjolfsson' in s_res['citation']
    assert 'Chandar' in s_res['citation']
    assert 'Chen' in s_res['citation']
    assert 'Canaries in the Coal Mine' in s_res['paper_title']
    assert 'digitaleconomy.stanford.edu' in s_res['primary_source_url']

    # Ensure no record in time_series_data retains redundant benchmark fields
    for row in ts:
        assert 'benchmark_resolved' not in row, f"Found deprecated 'benchmark_resolved' in year {row['year']}"
        assert 'expected_resolved_tasks' not in row, f"Redundant 'expected_resolved_tasks' found in time_series year {row['year']}"

    # Verify that task counts (resolved_tasks or expected_resolved_tasks) are canonically housed in swe_bench_milestones
    for m in data['swe_bench_milestones']:
        assert ('resolved_tasks' in m or 'expected_resolved_tasks' in m), f"Canonical milestone {m['milestone_id']} missing task resolution metric"
        if '2025' in m['milestone_id']:
            assert 'expected_resolved_tasks' in m, f"2025 milestone {m['milestone_id']} must use expected_resolved_tasks"

    # 5. Verify Mathematical Reproducibility of the Qualitative Skills Rubric
    rubric = data['author_qualitative_skills_rubric']
    weights = rubric['scoring_weights']
    w_auto = weights['automation_resistance_weight']
    w_verif = weights['verification_necessity_weight']
    w_screen = weights['screening_rigor_weight']
    
    for skill in rubric['skills_evaluations']:
        auto_score = skill['automation_exposure_score']
        verif_score = skill['verification_necessity_score']
        screen_score = skill['screening_rigor_score']
        
        calculated_val = round((100.0 - auto_score) * w_auto + verif_score * w_verif + screen_score * w_screen)
        recorded_val = skill['calculated_contemporary_score']
        assert calculated_val == recorded_val, f"Rubric formula mismatch for {skill['skill_domain']}: calc {calculated_val} vs rec {recorded_val}"
        assert calculated_val == skill['contemporary_2026_weight'], f"Weight mismatch for {skill['skill_domain']}"
    
    print("[PASS] All data integrity, arithmetic, P@SHA link, ISO date formats, benchmark nulls, FRED bounds, and rubric reproduction tests passed successfully!")

if __name__ == '__main__':
    test_data_integrity()
