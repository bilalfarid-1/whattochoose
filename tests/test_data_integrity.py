import json
import os
import math

def test_data_integrity():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'data', 'raw', 'longitudinal_se_data.json')
    
    assert os.path.exists(json_path), f"Missing data file: {json_path}"
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    ts = data['time_series_data']
    assert len(ts) == 7, f"Expected 7 annual records (2020-2026), found {len(ts)}"
    
    # 1. Verify Pakistan Export Arithmetic
    exp_2020 = [r for r in ts if r['year'] == 2020][0]['pakistan_it_exports_billion_usd']
    exp_2026 = [r for r in ts if r['year'] == 2026][0]['pakistan_it_exports_billion_usd']
    
    # Check straight-line annualization: 3.388 * 12 / 9 = 4.5173...
    expected_annualized = 3.388 * (12.0 / 9.0)
    assert abs(exp_2026 - expected_annualized) < 0.01, f"FY26 projection mismatch: {exp_2026} vs {expected_annualized}"
    
    # Check 6-year CAGR: ((exp_2026 / exp_2020) ** (1/6) - 1) * 100
    calculated_cagr = ((exp_2026 / exp_2020) ** (1.0 / 6.0) - 1.0) * 100.0
    recorded_cagr = data['pakistan_industry_benchmarks_2025_2026']['export_revenue_cagr_fy20_to_fy26_pct']
    assert abs(calculated_cagr - recorded_cagr) < 0.1, f"CAGR mismatch: {calculated_cagr} vs {recorded_cagr}"
    assert abs(calculated_cagr - 20.98) < 0.1, f"Expected ~21.0% CAGR, got {calculated_cagr}"
    
    # 2. Verify P@SHA Ratios
    pasha = data['pakistan_industry_benchmarks_2025_2026']
    total_hires = pasha['pasha_member_company_total_hires_2024']
    fresh_hires = pasha['pasha_member_fresh_graduate_hires_2024']
    expected_fresh_pct = (fresh_hires / total_hires) * 100.0
    recorded_fresh_pct = pasha['fresher_intake_share_pasha_member_firms_pct']
    assert abs(expected_fresh_pct - recorded_fresh_pct) < 0.1, f"P@SHA fresher share mismatch"
    
    # 3. Verify as_of_date and measurement_type metadata presence
    for row in ts:
        assert 'as_of_date' in row, f"Missing as_of_date for year {row['year']}"
        assert 'export_measurement_type' in row, f"Missing export_measurement_type for year {row['year']}"
        assert 'ai_metric_measurement_type' in row, f"Missing ai_metric_measurement_type for year {row['year']}"
        
    # 4. Verify Qualitative Rubric presence
    rubric = data['author_qualitative_skills_rubric']
    assert 'scoring_criteria' in rubric
    assert len(rubric['skills_evaluations']) >= 5
    
    print("[PASS] All data integrity, arithmetic, and provenance tests passed successfully!")

if __name__ == '__main__':
    test_data_integrity()
