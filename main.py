import pandas as pd
from datetime import datetime
df = pd.read_csv(r'C:\Users\Solovov\Dropbox\GoT\lesson_1_data.csv', encoding='windows-1251', sep=';')
print(df.dtypes)
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.columns)
df = df.rename(columns={'Номер': 'number',
                        'Дата создания': 'create_date',
                        'Дата оплаты': 'payment_date',
                        'Title': 'title',
                        'Статус': 'status',
                        'Заработано': 'money',
                        'Город': 'city',
                        'Платежная система': 'payment_system'})
print(df.columns)
print(df.title.head())


#Задача: выгрузить информацию о том, сколько денег какой продукт принес, и вынести по городам


all_money = df.money.sum()
mg = df.groupby(['title', 'city'], as_index=False) \
    .aggregate({'money': 'sum'}) \
    .sort_values('money', ascending=False)
print(mg)
money_by_city = mg
money_by_city.to_csv(r'C:\Users\Solovov\Dropbox\GoT\money_by_city.csv', index=False, encoding='windows-1251', sep=';')

money_title = df \
    .query("status == 'Завершен'") \
    .groupby(['title'], as_index=False) \
    .aggregate({'money': 'sum', 'number': 'count'}) \
    .sort_values('money', ascending=False) \
    .rename(columns={'number': 'success_orders'})

print(df.title.unique())

all_money_end = money_title.money.sum()
print(int(all_money_end) == int(all_money))

today_day = datetime.today().strftime('%Y-%m-%d')
file_name = 'money_title_{}.csv'
file_name.format(today_day)

if int(all_money_end) == int(all_money):
    print('OK! File {} is written.'.format(file_name))
    money_title.to_csv(file_name, index=False, encoding='windows-1251', sep=';')
else:
    print('Error!!!!')