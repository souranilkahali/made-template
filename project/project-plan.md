# Project Plan

## Title
<!-- Give your project a short title. -->
Awesome MADE project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does the accident data correlates with the vehicle counting point data?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The counting data is collected as nodal electricity counts on a representative key date (Monday - Friday, not on public holidays and outside school holidays).


For example, at a 4-arm junction, 12 junction flows (turns) are recorded. The counting is carried out using a specially attached video camera.


The traffic count is evaluated in 3 time blocks (6 a.m. - 10 a.m., 11 a.m. - 2 p.m. and 3 p.m. - 7 p.m.). The daily traffic is extrapolated from the time blocks using specific factors.


The values ​​can be viewed analogously to the technical term DTVw (average daily traffic on weekdays). The unit is vehicle/24h. The values ​​result in the route loads on the roads leading to the respective junction.

The accident statistics data has to be extracted and analysis has to be done to find the correlation 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: mobilithek
* Metadata URL: https://mobilithek.info/offers/-7344603824143622751
* Data URL: https://offenedaten-koeln.de/sites/default/files/KFZ_Zaheldaten_2016-2019_node.csv
* Data Type: CSV

Vehicle counting points and values dataset of ​​Cologne 

### Datasource2: data.europa.eu
* Metadata URL: https://data.europa.eu/data/datasets/70dd472a-dce0-401c-bb3e-5322d626e1f0?locale=en
* Data URL: https://offenedaten-koeln.de/dataset/unfallstatistik-k%C3%B6ln/resource/a32e0d4a-8a29-4b18-a49d-a9e1966c8c6f#{}                                                                                 
* Data Type: CSV

Accident statistics dataset of Cologne

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract Data from the two datasets
2. create graphs
3. check correlation
4. conclude with a result of the analysis
