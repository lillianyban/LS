import pandas as pd
import os
import re

print("Starting data pipeline")

files = [
    "Data/Raw/2018-2019.csv",
    "Data/Raw/2019-2020.csv",
    "Data/Raw/2020-2021.csv",
    "Data/Raw/2021-2022.csv",
    "Data/Raw/2022-2023.csv",
    "Data/Raw/2023-2024.csv"
]

colmap = {
    "Data Year": "data_year",
    "ID": "building_id_source",
    "Property Name": "property_name",
    "Reporting Status": "reporting_status",
    "Address": "address",
    "ZIP Code": "zip_code",
    "Chicago Energy Rating": "chicago_energy_rating",
    "Exempt From Chicago Energy Rating": "exempt_from_chicago_energy_rating",
    "Community Area": "community_area",
    "Primary Property Type": "primary_property_type",
    "Gross Floor Area - Buildings (sq ft)": "gross_floor_area_buildings_sq_ft",
    "Year Built": "year_built",
    "# of Buildings": "num_buildings",
    "Water Use (kGal)": "water_use_kgal",
    "ENERGY STAR Score": "energy_star_score",
    "Electricity Use (kBtu)": "electricity_use_kbtu",
    "Natural Gas Use (kBtu)": "natural_gas_use_kbtu",
    "District Steam Use (kBtu)": "district_steam_use_kbtu",
    "District Chilled Water Use (kBtu)": "district_chilled_water_use_kbtu",
    "All Other Fuel Use (kBtu)": "all_other_fuel_use_kbtu",
    "Site EUI (kBtu/sq ft)": "site_eui_kbtu_per_sq_ft",
    "Source EUI (kBtu/sq ft)": "source_eui_kbtu_per_sq_ft",
    "Weather Normalized Site EUI (kBtu/sq ft)": "weather_normalized_site_eui_kbtu_per_sq_ft",
    "Weather Normalized Source EUI (kBtu/sq ft)": "weather_normalized_source_eui_kbtu_per_sq_ft",
    "Total GHG Emissions (Metric Tons CO2e)": "total_ghg_emissions_metric_tons_co2e",
    "GHG Intensity (kg CO2e/sq ft)": "ghg_intensity_kg_co2e_per_sq_ft",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Location": "location",
    "Row_ID": "row_id"
}

numeric_cols = [
    "data_year",
    "building_id_source",
    "zip_code",
    "community_area",
    "gross_floor_area_buildings_sq_ft",
    "year_built",
    "num_buildings",
    "water_use_kgal",
    "energy_star_score",
    "electricity_use_kbtu",
    "natural_gas_use_kbtu",
    "district_steam_use_kbtu",
    "district_chilled_water_use_kbtu",
    "all_other_fuel_use_kbtu",
    "site_eui_kbtu_per_sq_ft",
    "source_eui_kbtu_per_sq_ft",
    "weather_normalized_site_eui_kbtu_per_sq_ft",
    "weather_normalized_source_eui_kbtu_per_sq_ft",
    "total_ghg_emissions_metric_tons_co2e",
    "ghg_intensity_kg_co2e_per_sq_ft",
    "latitude",
    "longitude"
]

def snake(s):
    s = s.strip().lower()
    s = s.replace("#", "num_").replace("%", "pct")
    s = s.replace("/", "_per_").replace("-", "_").replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def to_num(series):
    return pd.to_numeric(
        series.astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({"": None, "nan": None, "None": None}),
        errors="coerce"
    )

def get_reporting_year(filepath):
    match = re.search(r"(\d{4})-(\d{4})", filepath)
    return int(match.group(2)) if match else None

def normalize_address(series):
    s = series.astype(str).str.upper()
    s = s.str.replace(r"[^A-Z0-9 ]", " ", regex=True)
    s = s.str.replace(r"\s+", " ", regex=True).str.strip()

    replacements = {
        " NORTH ": " N ",
        " SOUTH ": " S ",
        " EAST ": " E ",
        " WEST ": " W ",
        " STREET ": " ST ",
        " AVENUE ": " AVE ",
        " ROAD ": " RD ",
        " DRIVE ": " DR ",
        " BOULEVARD ": " BLVD ",
        " PLACE ": " PL ",
        " COURT ": " CT ",
        " SUITE ": " STE "
    }

    s = " " + s + " "
    for old, new in replacements.items():
        s = s.str.replace(old, new, regex=False)

    s = s.str.replace(r"\s+", " ", regex=True).str.strip()
    return s

dfs = []

for file in files:
    df = pd.read_csv(file, low_memory=False)

    df = df.rename(columns={c: colmap.get(c, snake(c)) for c in df.columns})

    df["reporting_year"] = get_reporting_year(file)

    for col in numeric_cols:
        if col in df.columns:
            df[col] = to_num(df[col])

    if "address" in df.columns:
        df["address_norm"] = normalize_address(df["address"])
    else:
        df["address_norm"] = None

    if "latitude" in df.columns:
        df["lat_round6"] = df["latitude"].round(6)
    else:
        df["lat_round6"] = None

    if "longitude" in df.columns:
        df["lon_round6"] = df["longitude"].round(6)
    else:
        df["lon_round6"] = None

    dfs.append(df)

panel = pd.concat(dfs, ignore_index=True, sort=False)

panel["resolved_building_id"] = "id_" + panel["building_id_source"].astype("Int64").astype(str)

missing_id = panel["building_id_source"].isna()
panel.loc[missing_id, "resolved_building_id"] = (
    "addrgeo_"
    + panel.loc[missing_id, "address_norm"].fillna("")
    + "_"
    + panel.loc[missing_id, "lat_round6"].astype(str)
    + "_"
    + panel.loc[missing_id, "lon_round6"].astype(str)
)

if not os.path.exists("Content"):
    os.makedirs("Content")

print("Merging complete")

panel.to_csv("Content/energy_benchmarking_panel.csv", index=False)

print(f"Dataset ready with {panel.shape[0]} rows and {panel.shape[1]} columns")

df = panel.dropna(subset=["community_area", "reporting_year"])

community_year = df.groupby(["community_area", "reporting_year"]).agg({
    "site_eui_kbtu_per_sq_ft": "median",
    "total_ghg_emissions_metric_tons_co2e": "median",
    "energy_star_score": "mean",
    "water_use_kgal": "median",
    "resolved_building_id": "nunique"
}).reset_index()

community_year = community_year.rename(columns={
    "resolved_building_id": "num_buildings"
})

community_year.to_csv("Content/community_area_year.csv", index=False)

panel = panel.sort_values(["resolved_building_id", "reporting_year"])

panel["eui_change"] = panel.groupby("resolved_building_id")[
    "site_eui_kbtu_per_sq_ft"
].diff()

panel["ghg_change"] = panel.groupby("resolved_building_id")[
    "total_ghg_emissions_metric_tons_co2e"
].diff()

panel["eui_pct_change"] = panel.groupby("resolved_building_id")[
    "site_eui_kbtu_per_sq_ft"
].pct_change()

panel["ghg_pct_change"] = panel.groupby("resolved_building_id")[
    "total_ghg_emissions_metric_tons_co2e"
].pct_change()

panel["rating_group"] = pd.cut(
    panel["energy_star_score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"]
)

panel.to_csv("Content/building_longitudinal_changes.csv", index=False)

print("Community summaries and longitudinal analysis saved")

print("Pipeline finished successfully")