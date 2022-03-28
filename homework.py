import pandas as pd
taxi = pd.read_csv(r'C:\Users\Solovov\Dropbox\GoT\2_taxi_nyc.csv')
print(taxi.shape)
print(taxi.dtypes)
taxi = taxi.rename(columns = {'pcp 01': 'pcp_01',
                              'pcp 06': 'pcp_06',
                              'pcp 24': 'pcp_24'})
print(taxi.columns)
print(taxi['borough'].value_counts())
print(taxi \
      .groupby('borough') \
      .aggregate({'pickups': 'sum'}))
min_pickups = taxi \
      .groupby('borough') \
      .aggregate({'pickups': 'sum'})\
      .idxmin()
print(min_pickups)

print(taxi \
      .groupby(['borough', 'hday']) \
      .aggregate({'pickups': 'mean'}))

pickups_by_mon_bor = taxi \
    .groupby(['borough', 'pickup_month'], as_index=False) \
    .aggregate({'pickups': 'sum'}) \
    .sort_values('pickups', ascending=False)
