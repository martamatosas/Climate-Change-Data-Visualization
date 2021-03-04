Climate Change

Visualizations, static images, originally they originallly animated or interactive, embedded in a website (http://localhost:9000/ClimateChange/):

1- Rise of the average temperature of the Earth's surface, 1850 - 2019
The variation of the global surface temperature in Celsius (C) is calculated with respect to the mean of the global temperatures from 1850 to 1900, period adopted as an approximation of preindustrial conditions by the Intergovernmental Panel on Climate Change.
Three thresholds are marked: 1, 1.5 and 2 degree Celsius. The last two are relevant to the aim of the Paris Agreement of “holding the increase in the global average temperature to well below 2°C above pre-industrial levels and pursuing efforts to limit the temperature increase to 1.5°C.”

<img width="422" alt="Capture_Climate_Spiral_2017" src="https://user-images.githubusercontent.com/53956697/109977859-430c0a80-7ccb-11eb-8c46-f46871560ecd.PNG">


2- Occurrence of temperature anomalies
Temperature anomalies indicate how much warmer or colder it is than normal for a specific place and time. For this analysis, normal is defined as the average over the 30-year period 1951-1980 for that place and time of year in degrees Celsius (C), following NASA definition.

Occurrence of monthly temperature anomalies in 197 countries, 1743 - 2013
Top graph: sum of country temperature anomalies per month and year (Celsius).
Bottom graph: annual average of temperature anomalies per year (Celsius).

<img width="700" alt="Capture_Anomalies" src="https://user-images.githubusercontent.com/53956697/109979199-a185b880-7ccc-11eb-86ea-47a508528d7d.PNG">

3- Evolution of carbon dioxide concentration in the atmosphere, 803,719 BCE - 2018

<img width="699" alt="Capture_Atmospheric CO2" src="https://user-images.githubusercontent.com/53956697/109980493-f970ef00-7ccd-11eb-8090-523211beb7e8.PNG">


Files:

1- Data: original data files:

Global_temp_var_monthly.txt

GlobalandTemperaturesByCountry.csv

co2-concentration-long-term.csv

annual-co2-emissions-per-country.csv

2- Python programs:

- Climate Change_Global Temp.py

Input: Global_temp_var_monthly.txt

Output: ClimateSpiral.gif

-	Climate Change_anomalies.ipynb: 

Input: GlobalandTemperaturesByCountry.csv

Output: annual-co2-emissions-per-country-region.csv 

-	Climate Change_clean_co2-long-term.py:

Input: co2-concentration-long-term.csv

Output: co2-concentration-long-term_numeric.csv
 
- Climate Change_add region_co2-per-country.py:

Input: annual-co2-emissions-per-country.csv

Output: annual-co2-emissions-per-country-region.csv

