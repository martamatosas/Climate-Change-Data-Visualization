# Import long term Co2 concemtration in atmosephere dataset
import pandas as pd
data = pd.read_csv('co2-concentration-long-term.csv')
# inspect
print(data.head())
print(data.tail())
print(data.info())
#transform 'Year' to numeric
data['Year numeric'] = data['Year']
print(data.head())
for i in range(0, data.shape[0]):
    year = data.iloc[i, 2]
    if 'BCE' in year:
        new_year = '-' + year
        new_year = new_year.replace('BCE', '')
        data.iloc[i, -1] = new_year
data['Year'] = pd.to_numeric(data['Year numeric'])
# confirm successful transformation
print(data.info())
# save clean data to csv
data.to_csv('co2-concentration-long-term_numeric.csv')