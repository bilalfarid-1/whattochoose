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
    
    # 3. Verify as_of_date and measurement_type metadata presence
    for row in ts:
        assert 'as_of_date' in row, f"Missing as_of_date for year {row['year']}"
        assert 'export_measurement_type' in row, f"Missing export_measurement_type for year {row['year']}"
        assert 'ai_metric_measurement_type' in row, f"Missing ai_metric_measurement_type for year {row['year']}"
        
    # 4. Verify Mathematical Reproducibility of the Qualitative Skills Rubric
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
    
    print("[PASS] All data integrity, arithmetic, P@SHA link, and rubric reproduction tests passed successfully!")

if __name__ == '__main__':
    test_data_integrity()
