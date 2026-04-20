import pandas as pd

df = pd.read_csv("Content/energy_benchmarking_panel.csv")

print("\n--- Dataset Overview ---")
print("Shape:", df.shape)

print("\n--- Average Site EUI by Year ---")
print(df.groupby("data_year")["site_eui_kbtu_per_sq_ft"].mean())

print("\n--- Average GHG Emissions by Year ---")
print(df.groupby("data_year")["total_ghg_emissions_metric_tons_co2e"].mean())

print("\n--- Count by Property Type ---")
print(df["primary_property_type"].value_counts().head(10))