# Data Dictionary

This document describes the structure and meaning of the datasets generated in this project.

-------

## 1. energy_benchmarking_panel.csv

Combined dataset created from multiple years of Chicago Energy Benchmarking data.

- data_year: Year the building performance data corresponds to
- building_id_source: Original building ID from the source dataset
- property_name: Name of the building or property
- reporting_status: Reporting status for the building record
- address: Street address of the building
- zip_code: ZIP code of the building
- chicago_energy_rating: City-assigned Chicago Energy Rating, when available
- exempt_from_chicago_energy_rating: Whether the building is exempt from the Chicago Energy Rating requirement

- community_area: Chicago community area where the building is located
- primary_property_type: Main type or use category of the building
- gross_floor_area_buildings_sq_ft: Total gross floor area of the building in square feet
- year_built: Year the building was constructed
- num_buildings: Number of buildings included in the property record
- water_use_kgal: Annual water use in thousand gallons
- energy_star_score: ENERGY STAR score, when available
- electricity_use_kbtu: Electricity use in kBtu
- natural_gas_use_kbtu: Natural gas use in kBtu
- district_steam_use_kbtu: District steam use in kBtu
- district_chilled_water_use_kbtu: District chilled water use in kBtu
- all_other_fuel_use_kbtu: Other fuel use in kBtu
- site_eui_kbtu_per_sq_ft: Site Energy Use Intensity in kBtu per square foot
- source_eui_kbtu_per_sq_ft: Source Energy Use Intensity in kBtu per square foot
- weather_normalized_site_eui_kbtu_per_sq_ft: Weather-normalized Site EUI
- weather_normalized_source_eui_kbtu_per_sq_ft: Weather-normalized Source EUI
- total_ghg_emissions_metric_tons_co2e: Total greenhouse gas emissions in metric tons CO2e
- ghg_intensity_kg_co2e_per_sq_ft: Greenhouse gas emissions intensity in kg CO2e per square foot
- latitude: Latitude coordinate of the building
- longitude: Longitude coordinate of the building
- location: Geographic point field from the source data
- reporting_year: Year the dataset was reported
- address_norm: Standardized address field created during cleaning
- lat_round6: Latitude rounded to 6 decimal places
- lon_round6: Longitude rounded to 6 decimal places
- row_id: Row identifier from the source data, when available
- resolved_building_id: Final building identifier used for tracking buildings across years

---

## 2. building_longitudinal_changes.csv

Dataset capturing year-to-year changes in energy performance metrics for each building.

- resolved_building_id: Unique identifier used to track buildings across years
- reporting_year: Year of observation for the building record
- site_eui_kbtu_per_sq_ft: Site Energy Use Intensity for the given year
- total_ghg_emissions_metric_tons_co2e: Total greenhouse gas emissions for the given year
- energy_star_score: ENERGY STAR score for the building in that year

- prev_site_eui_kbtu_per_sq_ft: Site EUI from the previous year (for comparison)
- prev_total_ghg_emissions_metric_tons_co2e: Emissions from the previous year
- prev_energy_star_score: ENERGY STAR score from the previous year

- eui_change: Absolute change in site EUI compared to the previous year
- ghg_change: Absolute change in greenhouse gas emissions compared to the previous year
- energy_star_score_change: Change in ENERGY STAR score compared to the previous year

---

## 3. community_area_year.csv

Aggregated dataset summarizing building energy performance at the Chicago community area level for each year.

- community_area: Name of the Chicago community area
- reporting_year: Year corresponding to the aggregated data

- median_site_eui: Median Site Energy Use Intensity (EUI) across buildings in the community area
- median_ghg_emissions: Median greenhouse gas emissions across buildings in the community area
- mean_energy_star_score: Average ENERGY STAR score across buildings in the community area
- median_water_use: Median annual water usage across buildings in the community area

- num_buildings: Number of buildings included in the aggregation for that community area and year
---

## 4. summary tables (Results/Tables)

### missing_values.csv

Dataset summarizing missing data for each column in the integrated dataset.

- column: Column name
- missing_count: Number of missing values

- missing_percent: Percentage of missing values

### summary_stats.csv

Dataset containing descriptive statistics computed for numeric columns in the integrated dataset.

- statistic: Type of summary statistic (e.g., mean, standard deviation, minimum, maximum)

- column: Name of the variable being summarized
- value: Computed value of the statistic for that column

### year_counts.csv

Dataset summarizing the number of records per year in the integrated dataset.

- reporting_year: Year corresponding to the records

- row_count: Number of observations (rows) for that year

### property_type_counts.csv

Dataset summarizing the frequency of each building type in the integrated dataset.

- primary_property_type: Type of building (e.g., Office, Residential, School)

- count: Number of occurrences of each building type

### yearly_summary.csv

Dataset summarizing average energy performance metrics across all buildings for each year.

- reporting_year: Year corresponding to the aggregated data
- mean_site_eui: Average Site Energy Use Intensity (EUI) across buildings
- mean_ghg_emissions: Average greenhouse gas emissions across buildings

- mean_energy_star_score: Average ENERGY STAR score across buildings
- num_buildings: Number of buildings included in that year

### property_type_summary.csv

Dataset summarizing average energy performance metrics by building type.

- primary_property_type: Type of building (e.g., Office, Residential, School)
- mean_site_eui: Average Site Energy Use Intensity (EUI) for that building type
- mean_ghg_emissions: Average greenhouse gas emissions for that building type

- mean_energy_star_score: Average ENERGY STAR score for that building type
- num_buildings: Number of buildings included for that building type