import json
import os
import pandas as pd
import pytest

def test_fred_aggregation_offline():
    """
    Offline regression test verifying that annual aggregates of the FRED Indeed Software Postings
    Index (IHLIDXUSTPSOFTDEVE) calculated from the raw snapshot match:
    1. The known audited statistical properties (count, mean, min, max, partial status).
    2. The harmonized empirical JSON dataset (longitudinal_se_data.json) directly.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "raw", "IHLIDXUSTPSOFTDEVE.csv")
    json_path = os.path.join(base_dir, "data", "raw", "longitudinal_se_data.json")
    
    assert os.path.exists(csv_path), f"Missing raw FRED dataset: {csv_path}"
    assert os.path.exists(json_path), f"Missing harmonized JSON dataset: {json_path}"

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    json_ts_by_year = {r["year"]: r for r in json_data["time_series_data"]}

    df = pd.read_csv(csv_path)
    df["IHLIDXUSTPSOFTDEVE"] = pd.to_numeric(df["IHLIDXUSTPSOFTDEVE"], errors="coerce")
    df["observation_date"] = pd.to_datetime(df["observation_date"])
    df = df.dropna(subset=["IHLIDXUSTPSOFTDEVE"])
    df["year"] = df["observation_date"].dt.year

    expected_aggregates = {
        2020: {"count": 335, "mean": 78.91, "min": 64.70, "max": 100.78, "partial": True},
        2021: {"count": 365, "mean": 148.41, "min": 90.54, "max": 217.96, "partial": False},
        2022: {"count": 365, "mean": 195.59, "min": 130.51, "max": 233.83, "partial": False},
        2023: {"count": 365, "mean": 90.40, "min": 72.17, "max": 130.27, "partial": False},
        2024: {"count": 366, "mean": 69.53, "min": 66.53, "max": 72.58, "partial": False},
        2025: {"count": 365, "mean": 65.05, "min": 61.10, "max": 68.02, "partial": False},
        2026: {"count": 282, "mean": 73.13, "min": 66.92, "max": 78.34, "partial": True},
    }

    for year, expected in expected_aggregates.items():
        year_data = df[df["year"] == year]
        calc_count = len(year_data)
        calc_mean = round(year_data["IHLIDXUSTPSOFTDEVE"].mean(), 2)
        calc_min = round(year_data["IHLIDXUSTPSOFTDEVE"].min(), 2)
        calc_max = round(year_data["IHLIDXUSTPSOFTDEVE"].max(), 2)

        # 1. Assert against expected constants
        assert calc_count == expected["count"], f"Observation count mismatch for year {year}"
        assert abs(calc_mean - expected["mean"]) < 0.05, f"Mean mismatch for {year}: {calc_mean} vs {expected['mean']}"
        assert abs(calc_min - expected["min"]) < 0.05, f"Min mismatch for {year}: {calc_min} vs {expected['min']}"
        assert abs(calc_max - expected["max"]) < 0.05, f"Max mismatch for {year}: {calc_max} vs {expected['max']}"
        assert calc_min <= calc_mean <= calc_max, f"Bounding violation in {year}"

        # 2. Assert directly against harmonized JSON dataset (Raw CSV vs JSON binding)
        assert year in json_ts_by_year, f"Year {year} missing from longitudinal_se_data.json"
        json_rec = json_ts_by_year[year]
        
        json_mean = json_rec["us_indeed_software_postings_index"]
        json_min = json_rec["us_postings_min"]
        json_max = json_rec["us_postings_max"]
        json_count = json_rec["us_postings_obs_count"]

        assert abs(calc_mean - json_mean) < 0.05, f"Raw vs JSON mean mismatch for {year}: {calc_mean} vs {json_mean}"
        assert abs(calc_min - json_min) < 0.05, f"Raw vs JSON min mismatch for {year}: {calc_min} vs {json_min}"
        assert abs(calc_max - json_max) < 0.05, f"Raw vs JSON max mismatch for {year}: {calc_max} vs {json_max}"
        assert calc_count == json_count, f"Raw vs JSON count mismatch for {year}: {calc_count} vs {json_count}"

if __name__ == "__main__":
    test_fred_aggregation_offline()
    print("[PASS] Offline FRED aggregation test passed successfully with JSON dataset verification!")
