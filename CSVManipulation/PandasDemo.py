import pandas as pd

#Pandas DataFrame
df = pd.read_csv('CSVManipulation/GaCovidData.csv')
print(df.head())
print(df.tail())
date_myBirthday = df[(df['state'] == 'GA')]
print(len(date_myBirthday))


