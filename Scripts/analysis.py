import os
import pandas as pd
import numpy as np

print("Running longitudinal analysis...")

input_file = "Data/Processed/energy_benchmarking_panel.csv"
output_dir = "Results/Tables"

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_file, low_memory=False)

df = df.sort_values(["resolved_building_id", "reporting_year"])

df["eui_change"] = (
    df.groupby("resolved_building_id")["site_eui_kbtu_per_sq_ft"]
    .diff()
)

df["ghg_change"] = (
    df.groupby("resolved_building_id")["total_ghg_emissions_metric_tons_co2e"]
    .diff()
)

df["eui_pct_change"] = (
    df.groupby("resolved_building_id")["site_eui_kbtu_per_sq_ft"]
    .pct_change()
)

df["ghg_pct_change"] = (
    df.groupby("resolved_building_id")["total_ghg_emissions_metric_tons_co2e"]
    .pct_change()
)

df["eui_pct_change"] = df["eui_pct_change"].replace([np.inf, -np.inf], pd.NA)
df["ghg_pct_change"] = df["ghg_pct_change"].replace([np.inf, -np.inf], pd.NA)

df["rating_group"] = pd.cut(
    df["energy_star_score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)

df.to_csv("Data/Processed/building_longitudinal_changes.csv", index=False)

yearly_summary = (
    df.groupby("reporting_year")
    .agg({
        "site_eui_kbtu_per_sq_ft": "mean",
        "total_ghg_emissions_metric_tons_co2e": "mean",
        "energy_star_score": "mean",
        "resolved_building_id": "nunique"
    })
    .reset_index()
)

yearly_summary = yearly_summary.rename(columns={
    "site_eui_kbtu_per_sq_ft": "mean_site_eui",
    "total_ghg_emissions_metric_tons_co2e": "mean_ghg_emissions",
    "energy_star_score": "mean_energy_star_score",
    "resolved_building_id": "num_buildings"
})

yearly_summary.to_csv(f"{output_dir}/yearly_summary.csv", index=False)

property_type_summary = (
    df.groupby("primary_property_type")
    .agg({
        "site_eui_kbtu_per_sq_ft": "mean",
        "total_ghg_emissions_metric_tons_co2e": "mean",
        "energy_star_score": "mean",
        "resolved_building_id": "nunique"
    })
    .reset_index()
    .sort_values("resolved_building_id", ascending=False)
)

property_type_summary = property_type_summary.rename(columns={
    "site_eui_kbtu_per_sq_ft": "mean_site_eui",
    "total_ghg_emissions_metric_tons_co2e": "mean_ghg_emissions",
    "energy_star_score": "mean_energy_star_score",
    "resolved_building_id": "num_buildings"
})

property_type_summary.to_csv(f"{output_dir}/property_type_summary.csv", index=False)

print("Longitudinal analysis saved.")