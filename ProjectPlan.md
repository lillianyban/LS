**Overview**
>This project examines how building energy performance in Chicago has changed since the introduction of the city’s Energy Rating system in 2019. The goal is to understand whether the public display of energy ratings has influenced energy efficiency and environmental outcomes over time.
>
>We will use multi-year Chicago Energy Benchmarking data (2019–2023), which includes metrics such as Energy Use Intensity (EUI), greenhouse gas emissions, water usage, and energy ratings. These datasets will be combined across years to create a longitudinal view of building performance. We will also incorporate additional building-level attributes (such as building type or location) to allow for comparisons across categories.
>
>Our approach follows the data lifecycle covered in class. We will first acquire and organize the datasets, then clean and standardize fields across years (e.g., handling missing values, inconsistent formats, and schema differences). Next, we will integrate the datasets into a unified structure using common identifiers such as building ID and year. After integration, we will perform exploratory data analysis to identify trends and patterns in energy performance.
>
>The final outcome will include reproducible code, documented data processing steps, and visualizations that highlight how energy performance has evolved across buildings and neighborhoods in Chicago.


**Team**
>Our team consists of Sena and Lillian. Both members will collaborate on all major aspects of the project while maintaining clear primary responsibilities.
>
>Lillian will focus primarily on project organization, repository structure, and documentation. She will ensure that the workflow is clearly structured and reproducible, including maintaining clean file organization and writing supporting documentation for each step of the data lifecycle.
>
>Sena will focus primarily on data acquisition, cleaning, and preparation. This includes identifying data quality issues, standardizing fields across datasets, and preparing the data for integration. Sena will also take the lead on implementing data integration and ensuring consistency across years.
>
>Both team members will work together on exploratory data analysis, visualization, and interpretation of results. Responsibilities may shift as needed to ensure that all components of the project are completed effectively and meet course requirements.

**Research or Business Questions**
>The primary goal of this project is to understand how Chicago’s Energy Rating system has impacted building performance over time.
>The main research questions are:
>- How have energy efficiency (measured by Energy Use Intensity) and greenhouse gas emissions changed since the introduction of energy ratings in 2019?
>- Do buildings with higher energy ratings consistently perform better than lower-rated buildings across multiple years?
>- How have individual buildings improved or declined over time in terms of energy performance?
>- Are there differences in performance trends across building types or neighborhoods?

>These questions align with the available data and will help guide our overall approach to integrating and analyzing it.


**Datasets**
>
*Dataset 1*
>Key fields include Chicago Building ID, property name, address, ZIP code, property type, floor area, Energy Star score, EUI, GHG emissions, water use, and energy consumption. One of the main challenges is that the dataset is not consistent across years. Column names change, some fields get added or removed, and certain data like star ratings only starts appearing in 2019. A few buildings are also exempt from the rating system. Address formatting is also inconsistent, which makes it harder to track the same building over time.
>
*Dataset 2*
>This dataset adds geographic and demographic context. We are using Chicago community area boundaries from the city’s data portal, along with ACS data from the Census Bureau, including income, race, and housing characteristics. Since ACS data is reported at the Census tract level, we will use a CMAP crosswalk to aggregate it up to the community area level so it matches the building data.
>
*Dataset 3*
>This dataset includes annual heating and cooling degree days. The goal here is to control for weather differences across years, since energy use can change simply because of temperature, not necessarily because buildings became more or less efficient.
>
*How the Datasets Connect*
>First, we will combine the six annual benchmarking files into one dataset and add a reporting_year column. After that, we need to match buildings across years, which is not straightforward because building IDs are not always reliable and addresses are formatted differently. To deal with this, we will use fuzzy matching on addresses along with location data to group records that likely represent the same building and assign them a consistent ID.
>
>Next, we link buildings to community areas using the existing community area field, which connects directly to the city’s boundary data. Once that is done, we can aggregate results at the neighborhood level, such as median EUI by year. Then we bring in the ACS data by using a crosswalk to convert tract level data into community area level estimates.
>
>Finally, we merge in the weather data by year using a simple join. At the end, we will have one dataset where each row represents a building in a given year, along with its neighborhood characteristics and weather context.

**Timeline (Lilly)**
>Step 1: Repository setup and data acquisition. Set up the GitHub repo, download all datasets, and make sure everything looks correct.
>
>Step 2: Schema audit and normalization. Go through the six CSVs and standardize column names across years.
>
>Step 3: CSV merging and year tagging. Combine all files into one dataset with a reporting_year column.
>
>Step 4: Address clustering and building ID resolution. Use fuzzy matching and location data to track buildings across years.
>
>Step 5: Exploratory data analysis (EDA). Look at summary statistics and distributions, and flag any unusual values or missing data.
>
>Step 6: Community area aggregation and spatial join. Link buildings to community areas and bring in ACS data.
>
>Step 7: Longitudinal change analysis. Analyze year to year changes and compare different groups of buildings.
>
>Step 8: Building type and weather controlled analysis. Break results down by property type and account for weather differences.
>
>Step 9: Equity and geographic analysis. Map trends and analyze relationships with income, race, and housing.
>
>Step 10: Visualization and narrative development. Create final visuals and clearly explain findings.
>
>Step 11: Final report, documentation and cleanup. Finalize the report, clean up code, and document everything.

**Constraints (Lilly)**
>Not every building reports data every year, which creates gaps and makes comparisons harder. The dataset also changes across years, which adds extra work and increases the chance of inconsistencies. Address matching will not be perfect, so some errors are unavoidable.
>
>More importantly, we cannot prove causation. Any trends we see could be due to other factors like renovations, rising energy costs, or broader industry changes. Weather also affects energy use, which makes year to year comparisons harder. In addition, ACS data does not perfectly line up with community areas, so some values will be estimates. We also need to be careful when presenting results, since highlighting underperforming areas could have real world implications.

**Gaps and Needed Input (Lilly)**
>We do not have data on building occupancy, which can significantly affect energy use. We also do not know which buildings made upgrades, so it is hard to tell what actually caused improvements. Lease structures, like who pays utilities, also matter, but we do not have that information.
>
>Our pre placard baseline is limited, since we only have one year of data before ratings started. We also cannot confirm whether buildings actually displayed their ratings. From a modeling standpoint, we will likely need more advanced methods since observations are not independent. Finally, spatial patterns may require additional techniques that we have not fully worked out yet. 
