import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('subscription_data.csv', parse_dates=['created_date', 'canceled_date'])
df['month_created'] = df.created_date.dt.to_period('M').dt.to_timestamp()

#Количество подписок по месяцам
plt.figure(figsize=(12, 7))
df_monthly = df.groupby('month_created', as_index=False).agg({'customer_id':'count'})
sns.lineplot(data=df_monthly, x='month_created', y='customer_id')
plt.ylabel('Sub_count')
plt.xlabel('Month')
plt.title('Subscriptions per Month')
plt.xticks(df_monthly.month_created.unique(), rotation = 45)
plt.show()

#Процент пользователей, которые оформили подписку на 5 месяцев и более
df['duration_days'] = (df['canceled_date'] - df['created_date']).dt.days
df['duration_month'] = df['duration_days'] / 30
long_term_users_percent = df.query('duration_month >= 5').customer_id.count() / df.customer_id.count() *100
print(long_term_users_percent)

# Распределение пользователей по группам в зависимости
# от продолжительности подписки и визуализация
def foo(x):
    if x<=1:
        return 'low'
    elif 1<x<=3:
        return 'medium'
    elif 3<x<=6:
        return 'high'
    else:
        return 'extremely_high'
df['group_duration'] = df['duration_month'].apply(foo)
ax = df.groupby('group_duration', as_index=False)['customer_id'].count().sort_values('customer_id')
sns.barplot(data=ax, x='group_duration', y='customer_id')
plt.title("Distribution into Groups")
plt.xlabel('Group')
plt.ylabel('Users count')
plt.show()

# Тенденция средней длительности подписки по месяцам
ax = df.groupby('month_created', as_index=False).agg({'duration_days':'mean'})
plt.figure(figsize=(10,7))
sns.lineplot(data=ax, x='month_created', y='duration_days')
plt.title('Average subscription duration time')
plt.xlabel('Month')
plt.ylabel('Days count')
plt.xticks(df.month_created.unique(),
           rotation = 45)
plt.show()

# Визуализация числа пользователей, отменивших подписку
# и нахождение пиков
ax = df.groupby(df['canceled_date'].dt.to_period('M'), as_index=False).agg({'customer_id':'count'})
sns.lineplot(data=ax)
plt.title('Canceled subs')
plt.xlabel('Month')
plt.ylabel('Value of Canceled Users')
plt.show()
print(ax)