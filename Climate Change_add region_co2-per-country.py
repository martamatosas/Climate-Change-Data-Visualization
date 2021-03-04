# Import Co2 emission by country and year (1949 to 2017)
import pandas as pd
data = pd.read_csv('annual-co2-emissions-per-country.csv')
# inspect
print(data.head())
# get country list
country_list = data['Entity'].unique()
#print(country_list)

# create lists of EU countries
European_Union= ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark',
                 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia',
                 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Slovakia',
                 'Slovenia', 'Spain', 'Sweden', 'United Kingdom', 'Bonaire Sint Eustatius and Saba',
                 'British Virgin Islands', 'Czechoslovakia', 'Faeroe Islands', 'Guadeloupe', 'Cayman Islands',
                 'Sint Maarten (Dutch part)', 'Martinique']

# create lists of values in entity that are regions
regions_in_entity = ['Africa', 'Americas (other)', 'Asia and Pacific (other)', 'EU-28', 'Middle East', 'Europe (other)', 'World']

# create column 'Entity2' to be filled in with countries and EU-28
data['Entity2'] = ''

# fill column 'Entity2' in
nrows = data.shape[0]
for i in range(0, nrows):
    entity = data.iloc[i, 0]
    if European_Union.count(entity) > 0:
        data.iloc[i, 4] = 'EU-28'
    elif regions_in_entity.count(entity) > 0:
        data.iloc[i, 4] = 'NA'
    else:
        data.iloc[i, 4] = entity

# create lists of countries per region
Africa = ['Botswana', 'Burundi', 'Comoros', 'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya', 'Madagascar', 'Malawi',
          'Mauritius', 'Mayotte', 'Mozambique', 'Reunion', 'Rwanda', 'Seychelles', 'Somalia', 'Tanzania', 'Uganda',
          'Zambia', 'Zimbabwe', 'Angola', 'Cameroon', 'Central African Republic', 'Chad', 'Congo', 'Equatorial Guinea',
          'Gabon', 'Sao Tome', 'Principe', 'Algeria', 'Egypt', 'Libya', 'Morocco', 'South Sudan', 'Tunisia',
          'Western Sahara', 'Benin', 'Burkina Faso', 'Cape Verde', 'Cote D’Ivoire', 'Gambia', 'Ghana', 'Guinea',
          'Guinea-Bissau', 'Liberia', 'Mali', 'Mauritania', 'Niger', 'Nigeria', 'Saint Helena', 'Senegal',
          'Sierra Leone', 'South Africa', 'Togo', "Cote d'Ivoire", 'Democratic Republic of Congo', 'Lesotho', 'Namibia',
          'Sao Tome and Principe', 'Swaziland']
Antarctica = ['Antarctic Fisheries']
Asia = ['Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Hong Kong',
        'India', 'Indonesia', 'Japan', 'North Korea', 'South Korea',
        'Kyrgyzstan', 'Laos', 'Macao', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'Pakistan',
        'Philippines', 'Singapore', 'Sri Lanka', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor Leste', 'Turkmenistan',
        'Uzbekistan', 'Vietnam', 'Turkey', 'Timor', 'Tonga', 'Afghanistan', 'Bahrain', 'Iraq', 'Iran', 'Israel',
        'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia', 'Syria', 'United Arab Emirates',
        'Yemen', 'Sudan']
America = ['Bermuda', 'Canada', 'Greenland', 'Saint Pierre', 'Miquelon', 'Mexico', 'Belize', 'Costa Rica',
                 'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'United States',
                 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Dominican Republic', 'Curacao',
                 'Guyana', 'Haiti', 'Jamaica', 'OECS', 'Antigua and Barbuda', 'Dominica', 'Grenada',
                 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Suriname', 'Trinidad and Tobago',
                 'Turks and Caicos', 'Anguilla', 'Grenada', 'Montserrat', 'Saint Kitts and Nevis',
                 'Saint Pierre and Miquelon', 'Turks and Caicos Islands', 'Argentina', 'Bolivia', 'Brazil',
                  'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 'Guyana', 'Paraguay',
                  'Peru', 'Suriname', 'Uruguay', 'Venezuela', 'Cuba']

Oceania = ['Australia', 'Fiji', 'French Polynesia', 'Guam', 'Kiribati', 'The Marshall Islands',
           'Micronesia', 'New Caledonia', 'New Zealand', 'Papua New Guinea', 'Samoa', 'American Samoa',
           'Solomon Islands', 'Vanuatu', 'Christmas Island', 'Cook Islands', 'Micronesia', 'Micronesia (country)', 'Nauru', 'Niue',
           'Palau', 'Tuvalu', 'Wallis and Futuna Islands']
Europe = ['EU-28', 'Armenia', 'Albania', 'Andorra', 'Belarus', 'Kazakhstan', 'Kyrgysztan', 'Liechtenstein', 'Macedonia',
          'Montenegro', 'Serbia', 'Bosnia and Herzegovina', 'Marshall Islands', 'Moldova', 'Switzerland',
          'Russia', 'Kazakhastan', 'Ukraine', 'Gibraltar', 'Azerbaijan', 'Georgia']

# create column for region
data['Region'] = ''
# fill column 'Region' in
for i in range(0, nrows):
    entity2 = data.iloc[i, 4]
    if Africa.count(entity2) > 0:
        data.iloc[i, 5] = 'Africa'
    elif Antarctica.count(entity2) > 0:
        data.iloc[i, 5] = 'Antarctica'
    elif Asia.count(entity2) > 0:
        data.iloc[i, 5] = 'Asia'
    elif Europe.count(entity2) > 0:
        data.iloc[i, 5] = 'Europe'
    elif America.count(entity2) > 0:
        data.iloc[i, 5] = 'America'
    elif Oceania.count(entity2) > 0:
        data.iloc[i, 5] = 'Oceania'
    elif entity2 == 'NA':
        data.iloc[i, 5] = 'NA'
    else:
        data.iloc[i, 5] = 'NA'

data.to_csv('annual-co2-emissions-per-country-region.csv')