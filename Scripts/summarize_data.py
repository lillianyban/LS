import os
import pandas as pd

print("Creating summary and quality tables...")

input_file = "Data/Processed/energy_benchmarking_panel.csv"
tables_dir = "Results/Tables"

os.makedirs(tables_dir, exist_ok=True)
df = pd.read_csv(input_file, low_memory=False)

missing_values = (
    df.isna()
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

missing_values.columns = ["column", "missing_count"]
missing_values["missing_percent"] = (
    missing_values["missing_count"] / len(df) * 100
)

missing_values.to_csv(f"{tables_dir}/missing_values.csv", index=False)

summary_stats = df.describe(include="all")
summary_stats.to_csv(f"{tables_dir}/summary_stats.csv")

year_counts = (
    df["reporting_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_counts.columns = ["reporting_year", "row_count"]
year_counts.to_csv(f"{tables_dir}/year_counts.csv", index=False)

property_type_counts = (
    df["primary_property_type"]
    .value_counts()
    .head(20)
    .reset_index()
)

property_type_counts.columns = ["primary_property_type", "count"]
property_type_counts.to_csv(f"{tables_dir}/property_type_counts.csv", index=False)

community_df = df[df["community_area"].notna()]

print("Rows before filtering:", len(df))
print("Rows after filtering (community_area not null):", len(community_df))

if len(community_df) > 0:
    community_area_year = (
        community_df
        .groupby(["community_area", "reporting_year"])
        .agg({
            "site_eui_kbtu_per_sq_ft": "median",
            "total_ghg_emissions_metric_tons_co2e": "median",
            "energy_star_score": "mean",
            "water_use_kgal": "median",
            "resolved_building_id": "nunique"
        })
        .reset_index()
    )

    community_area_year = community_area_year.rename(columns={
        "site_eui_kbtu_per_sq_ft": "median_site_eui",
        "total_ghg_emissions_metric_tons_co2e": "median_ghg_emissions",
        "energy_star_score": "mean_energy_star_score",
        "water_use_kgal": "median_water_use",
        "resolved_building_id": "num_buildings"
    })

    community_area_year.to_csv(
        "Data/Processed/community_area_year.csv",
        index=False
    )

    print("Community area aggregation saved.")
else:
    print("Warning: community_area column has no usable data.")

print("Summary and quality tables saved.")