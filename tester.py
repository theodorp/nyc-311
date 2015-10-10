import pandas as pd

chunk = 10**5
iter_csv = pd.read_csv('311_Service_Requests_from_2014.csv', usecols=['Created Date', \
						'Complaint Type', 'Descriptor', 'Location Type', 'Borough', 'Latitude', \
						'Longitude'], parse_dates=['Created Date'], iterator=True, chunksize=chunk)

# df = pd.concat([chunk[chunk['Descriptor'] == 'Loud Music/Party'] for chunk in iter_csv])
df = pd.concat(chunk for chunk in iter_csv)
df.to_csv('reduced_2014.csv', index=False)


# # reader = pd.read_csv('311_Service_Requests_from_2014.csv', usecols=['Created Date', \
# 						# 'Complaint Type', 'Descriptor', 'Location Type', 'Borough', 'Latitude', 'Longitude'],\
# 						# parse_dates=['Created Date'])

# # reader['Weekday'] = pd.DatetimeIndex(reader['Created Date']).weekday
# # reader['Hour'] = pd.DatetimeIndex(reader['Created Date']).hour

# # reader = reader[(reader['Descriptor'] == 'Loud Music/Party')]

# # reader.to_csv('parties_2014.csv', index=False)

# df = pd.read_csv('parties_2014.csv', parse_dates=['Created Date'])

# print(df.head())

# #####
# # test_df = df[df['Weekday'] == 2]
# # print(len(test_df.Longitude))
# # print(len(df[df['Weekday'] == 2]['Longitude']))
# #####