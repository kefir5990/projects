import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('coffe_sales_fixed.csv')
df = df.reset_index()
df.date = pd.to_datetime(df.date)

#Расчет выручки по каждой строке
df['profit'] = df['price'] * df['quantity_sold']

#Выручка за весь период
all_earnings = df['profit'].sum()

#Самый популярный продукт
popular_product = df.groupby('product').agg({'quantity_sold':'sum'}).sort_values('quantity_sold', ascending=False).head(1)

#Наибольшая выручка
most_profit = df.groupby('product')['profit'].sum().sort_values(ascending=False).head(1)

#Выручка по категориям
earnings_by_ctegory = df.groupby('category')['profit'].sum().sort_values()

#Город с большей выручкой
top_earnings_by_city = df.groupby('city')['profit'].sum().sort_values(ascending=False).head(1)

#Средний чек по городам
mean_chek_by_city = df.groupby('city').agg({'profit':'mean'}).round(2).sort_values(by='profit')

#Сравнение клиентов с картой лояльности и без
compare_clients = df.groupby('loyalty_card')['profit'].sum()

#Покупаемые товары клиентов с картой
stuff_by_loyalty_clients = df.query("loyalty_card == 'Yes'").groupby('category')['category'].count().sort_values(ascending=False)

#Доходность по размеру помещения
profit_by_store_size = df.groupby('store_size')['profit'].sum().sort_values(ascending=False)

####### Визуализация #######

#Динамика продаж
ax = df.groupby('date').agg({'quantity_sold':'sum'})
#sns.lineplot(data=ax, x='date', y='quantity_sold')

#Изменение ежедневной выручки
ax = df.groupby('date').agg({'profit':'sum'})
#sns.barplot(data=ax, x='date', y='profit')

#Распределение по категориям
ax = df.groupby('category').agg({'profit':'sum'}).sort_values(ascending=False, by='profit')
#sns.barplot(data=ax, x='profit', y='category', orient='h')

#Зависимость выручки от размера магазина 
#sns.barplot(data=df, x='profit', y='store_size')

#Разница выручки между клиентами с картой лояльности и без
sns.barplot(data=df, x='date', y='profit', hue='loyalty_card')


plt.show()



