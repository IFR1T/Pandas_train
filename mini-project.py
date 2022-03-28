import pandas as pd

bookings = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', encoding='windows=1251',
                       sep=';')
bookings_head = bookings.head(7)

bookings = bookings.rename(columns={c: c.replace(' ', '_').lower() for c in bookings.columns})

top_countries = bookings \
    .query('is_canceled == 0') \
    .groupby(['country'], as_index=False) \
    .aggregate({'hotel': 'count'}) \
    .sort_values('hotel')

avg_nights = bookings \
    .groupby(['hotel']) \
    .aggregate({'stays_total_nights': 'mean'})

print(bookings.columns)

print(bookings.shape)

print(bookings.dtypes)

print(top_countries)

print(avg_nights)

diff_rooms = bookings \
    .query('assigned_room_type != reserved_room_type') \
    .groupby(['hotel'], as_index=False) \
    .aggregate({'assigned_room_type': 'count'})
print(diff_rooms)

date_arrival = bookings \
    .groupby(['arrival_date_month', 'arrival_date_year']) \
    .aggregate({'assigned_room_type': 'count'}) \
    .sort_values('assigned_room_type')

print(date_arrival)

cancel_reservation = bookings \
    .groupby(['arrival_date_year', 'arrival_date_month']) \
    ['is_canceled'].value_counts()\
    .sort_values()

print(cancel_reservation)

ages = bookings[['adults', 'children', 'babies']].describe()

print(ages)

bookings['total_kids'] = bookings['children'] + bookings['babies']
print(round(bookings.groupby('hotel').agg({'total_kids': 'mean'}), 2))

kids_cancel = bookings.query('total_kids > 0').is_canceled.mean()
print(kids_cancel)
adult_cancel = bookings.query('total_kids == 0').is_canceled.mean()
print(adult_cancel)