# Project Plan

## Title
<!-- Give your project a short title. -->
Awesome MADE project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a statistically significant correlation between global sea level change and global surface temperature change from 2000 to 2021?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The correlation between the two datasets, global sea level change (2000-2021) and the GISS Surface Temperature Analysis version 4 (GISTEMP v4), can provide insights into the relationship between rising sea levels and global surface temperature changes during the specified period.

A positive correlation may suggest that as global surface temperatures increase, there is a corresponding rise in sea levels. This correlation could be indicative of the influence of global warming on both the thermal expansion of seawater and the melting of ice sheets and glaciers, contributing to the observed sea level changes.

Conversely, a weaker or negative correlation might indicate that other factors, such as local geological processes or regional variations, are playing a more dominant role in driving sea level changes during this specific timeframe.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: NASA (GISTEMP)
* Metadata URL: https://data.giss.nasa.gov/gistemp/
* Data URL: https://data.giss.nasa.gov/gistemp/tabledata_v4/NH.Ts+dSST.csv
* Data Type: CSV

Northern Hemisphere-Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies

### Datasource2: NASA (GISTEMP)
* Metadata URL: https://data.giss.nasa.gov/gistemp/
* Data URL: https://data.giss.nasa.gov/gistemp/tabledata_v4/SH.Ts+dSST.csv
* Data Type: CSV

Southern Hemisphere-Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies

### Datasource3: NASA.GOV
* Metadata URL: https://climate.nasa.gov/
* Data URL: https://www.kaggle.com/datasets/kkhandekar/global-sea-level-1993-2021/data                                                                       
* Data Type: CSV

Change in sea level since 1993 as observed by satellites

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract Data from the two datasets
2. create graphs
3. check correlation
4. conclude with a result of the analysis
