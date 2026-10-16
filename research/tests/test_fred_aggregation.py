import os
import pandas as pd
import pytest

def test_fred_aggregation_offline():
    """
    Offline regression test verifying that annual aggregates of the FRED Indeed Software Postings
    Index (IHLIDXUSTPSOFTDEVE) calculated from the raw snapshot match the harmonized dataset.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "raw", "IHLIDXUSTPSOFTDEVE.csv")
    assert os.path.exists(csv_path), f"Missing raw FRED dataset: {csv_path}"

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
        assert len(year_data) == expected["count"], f"Observation count mismatch for year {year}"
        
        calc_mean = round(year_data["IHLIDXUSTPSOFTDEVE"].mean(), 2)
        calc_min = round(year_data["IHLIDXUSTPSOFTDEVE"].min(), 2)
        calc_max = round(year_data["IHLIDXUSTPSOFTDEVE"].max(), 2)

        assert abs(calc_mean - expected["mean"]) < 0.05, f"Mean mismatch for {year}: {calc_mean} vs {expected['mean']}"
        assert abs(calc_min - expected["min"]) < 0.05, f"Min mismatch for {year}: {calc_min} vs {expected['min']}"
        assert abs(calc_max - expected["max"]) < 0.05, f"Max mismatch for {year}: {calc_max} vs {expected['max']}"
        
        # Verify bounding invariant: min <= mean <= max
        assert calc_min <= calc_mean <= calc_max, f"Bounding violation in {year}"

if __name__ == "__main__":
    test_fred_aggregation_offline()
    print("[PASS] Offline FRED aggregation test passed successfully!")
