import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("Results/Figures", exist_ok=True)

df = pd.read_csv("Data/Processed/energy_benchmarking_panel.csv")

# Avg EUI by year
eui_by_year = df.groupby("reporting_year")["site_eui_kbtu_per_sq_ft"].mean()

plt.figure()
eui_by_year.plot()
plt.title("Average Site EUI by Year")
plt.xlabel("Year")
plt.ylabel("EUI")
plt.savefig("Results/Figures/eui_by_year.png")
plt.close()

# Avg GHG by year
ghg_by_year = df.groupby("reporting_year")["total_ghg_emissions_metric_tons_co2e"].mean()

plt.figure()
ghg_by_year.plot()
plt.title("Average GHG Emissions by Year")
plt.xlabel("Year")
plt.ylabel("GHG")
plt.savefig("Results/Figures/ghg_by_year.png")
plt.close()

print("Plots saved.")