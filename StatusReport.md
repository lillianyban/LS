# Status Report

## Overview

This project examines how building energy performance in Chicago has changed over time using the city’s Energy Benchmarking data. The goal is to build a multi-year dataset that allows us to analyze trends in energy use, greenhouse gas emissions, and building characteristics across reporting years.

We selected the Chicago Energy Benchmarking dataset because it directly aligns with our research goals and provides consistent, multi-year building-level data suitable for longitudinal analysis.

At this stage, we focused on constructing a clean and reproducible data pipeline for combining annual benchmarking datasets. This includes standardizing column names, cleaning numeric fields, and merging multiple years of data into a single panel dataset for further analysis.


## Progress on Planned Tasks

We have completed Steps 1–5 of our planned workflow, which includes data acquisition, schema standardization, dataset merging, building identifier resolution, and initial exploratory data analysis.

We collected six annual Chicago Energy Benchmarking datasets covering reporting years 2019 through 2024 and organized them within a structured directory (`Data/Raw`) to improve clarity and reproducibility.

We developed a preprocessing script (`clean_and_merge.py`) that standardizes column names across datasets, converts numeric fields into consistent formats, and normalizes address data. The script also constructs helper fields such as a resolved building identifier and reporting year.

Using this script, we successfully combined all six annual datasets into a single panel dataset. The resulting dataset contains over 21,000 records and 35 columns, representing building-level observations across multiple years.

We also performed initial exploratory data analysis on the combined dataset. This included reviewing dataset dimensions, calculating average Site EUI and greenhouse gas emissions by year, and examining the most common property types represented in the dataset.


## Current Artifacts

The following artifacts have been created so far:

- Raw datasets: `Data/Raw/2018-2019.csv` through `Data/Raw/2023-2024.csv`
- Preprocessing script: `clean_and_merge.py`
- Analysis script: `analysis.py`
- Combined dataset: `Content/energy_benchmarking_panel.csv`

The combined dataset is generated directly from the preprocessing script, ensuring that the workflow is reproducible.


## Reproducibility

The preprocessing pipeline is fully reproducible using the provided script. To recreate the dataset, a user can run: python3 clean_and_merge.py


This script reads the raw datasets from the `Data/Raw` directory, performs column standardization, numeric conversion, and identifier construction, and outputs the combined dataset to: Content/energy_benchmarking_panel.csv


All dependencies are standard Python libraries (pandas, os, re), and no manual steps are required.


## Changes to the Project Plan

Since the original project plan, we adjusted our approach to focus first on building a clean and consistent multi-year dataset before integrating additional external data sources. Our initial plan included incorporating additional datasets early in the workflow, but we determined that ensuring a stable and reliable core dataset was a necessary first step.

This adjustment simplifies the workflow and improves reproducibility while still supporting our overall research goals.


## Challenges Encountered

One major challenge has been inconsistencies across the annual datasets. Column names vary between years, and some fields are missing or recorded differently. We addressed this by creating a column mapping system to standardize field names.

Another challenge is missing data in key variables such as energy use and emissions. Our initial analysis shows that several columns have a significant number of missing values, which will need to be handled carefully in future steps. We also began assessing data quality by examining missing value distributions and identifying which variables are sufficiently complete for analysis versus those that may require filtering or imputation.

We also encountered issues with identifying buildings consistently across years, as some records have missing or unreliable IDs. To address this, we implemented a preliminary resolved building identifier using existing IDs and normalized address/location data.

Finally, we encountered technical issues related to file structure and output paths when saving processed data, which we resolved by correcting directory handling in our script.


## Exploratory Data Analysis

After constructing the combined dataset, we conducted an initial exploratory data analysis (EDA) to better understand its structure and key variables.

We confirmed that the dataset contains 21,051 observations and 35 columns, indicating that the six annual benchmarking files were successfully integrated. We then analyzed trends in key metrics such as Site Energy Use Intensity (EUI) and total greenhouse gas emissions by year. Preliminary results show variation in both metrics over time, suggesting that building performance may have changed across reporting years.

We also examined the distribution of primary property types. The most common categories include Multifamily Housing, K–12 Schools, and Office buildings, which provides insight into the composition of the dataset and will inform future comparisons.

Additionally, this analysis helped identify data quality issues such as mixed data types and missing values in several columns. These findings will guide future cleaning and analysis steps.


## Updated Timeline

- Completed: Data collection and repository setup (Step 1)  
- Completed: Schema standardization and normalization (Step 2)  
- Completed: Dataset merging and year tagging (Step 3)  
- Completed: Building ID resolution (Step 4)  
- Completed: Initial exploratory data analysis (Step 5)  
- Next: Community-level aggregation and external data integration (Step 6)  
- Next: Longitudinal and grouped analysis (Steps 7–8)  

## Next Steps

With the core dataset constructed and initial exploratory analysis completed, the next phase of the project will focus on extending the dataset and deepening the analysis.

The immediate next step is to integrate additional contextual data, such as community-level demographic or geographic information. This will allow us to analyze how building energy performance varies across different neighborhoods and socioeconomic conditions.

We also plan to refine our building-level tracking across years. While a preliminary resolved building identifier has been implemented, further improvements may be needed to ensure consistent matching for buildings with incomplete or inconsistent identifiers.

In addition, we will expand our exploratory analysis into more detailed comparisons, including trends by building type and changes within individual buildings over time. This will help us better understand whether improvements are consistent across categories or concentrated in specific groups.

Finally, we will begin developing visualizations to clearly communicate trends in energy use and emissions. These visualizations will be used to support our final analysis and highlight key insights from the data.

## Data Quality and Cleaning Approach

Our data cleaning strategy focused on ensuring consistency and usability across multiple years of data. We applied a standardized column mapping to align schema differences, converted relevant fields to numeric types, and normalized address fields to improve consistency.

We also created a resolved building identifier to handle missing or inconsistent IDs across datasets. While this approach is not perfect, it provides a reasonable foundation for tracking buildings across years.

In addition, we examined missing value patterns and identified which variables are suitable for analysis versus those that may require filtering or additional processing. These steps ensure that our dataset is both consistent and appropriate for further analysis.


## Individual Contributions

### Lillian
here...

### Sena

Sena contributed to debugging and refining the data processing pipeline, including resolving issues with file structure and ensuring the script correctly generated the combined dataset.

Sena also helped organize the project directory and update file paths to improve reproducibility. In addition, Sena implemented an initial exploratory analysis script (`analysis.py`) to summarize key variables and verify that the dataset was ready for further analysis.

Finally, Sena contributed to writing and refining the status report to accurately reflect the project’s progress and workflow.