import pandas as pd
import time

df = pd.read_csv('parties_2014.csv')

# df = df[(df['Borough'] == 'MANHATTAN') | (df['Borough'] == 'BROOKLYN')]

# # weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# # df['Day'] = pd.DatetimeIndex(df['Created Date']).weekday
# # df['Day'] = df['Day'].apply(lambda x: weekdays[x])

# df['Time'] = pd.DatetimeIndex(df['Created Date']).time
# df['Time'] = df['Time'].apply(lambda x: str(x)[0:2]+str(x)[3:5])

# df['Week'] = pd.DatetimeIndex(df['Created Date']).week

# # df = df[[0,5,6,7,8,9]]
# df.drop(['Complaint Type', 'Descriptor', 'Location Type', 'Borough'], inplace=True, axis=1)

# df.to_csv('NYC-2014-Parties.csv', index=False)

print(df['Location Type'].unique())