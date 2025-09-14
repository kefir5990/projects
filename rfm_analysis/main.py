import pandas as pd

df = pd.read_csv('rfm_ht_data.csv', low_memory=False)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

last_date = df['InvoiceDate'].max()

rfm_table = df.groupby('CustomerCode').agg({'InvoiceDate' : lambda x: (last_date-x.max()).days,
                                            'InvoiceNo':'count',
                                            'Amount':'sum'})

rfm_table.rename(columns={'InvoiceDate':'recency',
                                      'InvoiceNo':'frequency',
                                      'Amount':'monetary_value'}, inplace=True)

rfm_segmentation = rfm_table
quantiles = rfm_table.quantile(q=[0.25, 0.5, 0.75])

def RClass(value, parameter_name, quantiles_table):
    if value <= quantiles_table[parameter_name][0.25]:
        return 1
    elif value <= quantiles_table[parameter_name][0.5]:
        return 2
    elif value <= quantiles_table[parameter_name][0.75]:
        return 3
    else:
        return 4
    
def FMClass(value, parameter_name, quantiles_table):
    if value <= quantiles_table[parameter_name][0.25]:
        return 4
    elif value <= quantiles_table[parameter_name][0.5]:
        return 3
    elif value <= quantiles_table[parameter_name][0.75]:
        return 2
    else:
        return 1
    
rfm_segmentation['R_Quartile'] = rfm_segmentation['recency'].apply(RClass, args=('recency', quantiles))
rfm_segmentation['F_Quartile'] = rfm_segmentation['frequency'].apply(FMClass, args=('frequency', quantiles))
rfm_segmentation['M_Quartile'] = rfm_segmentation['monetary_value'].apply(FMClass, args=('monetary_value', quantiles))

rfm_segmentation['RFMClass'] = rfm_segmentation.R_Quartile.map(str)+rfm_segmentation.F_Quartile.map(str)+rfm_segmentation.M_Quartile.map(str)

#Максимальное количество покупок одним пользователем
max_frequency = rfm_segmentation.frequency.max()

#Верхняя граница покупок 4 класс, M
hb_m = rfm_segmentation.query('M_Quartile == 4').monetary_value.max()

#Нижняя граница количества покупок 1 класс, F
lb_f= rfm_segmentation.query('F_Quartile == 1').frequency.min()

#Верхняя граница количества покупок класс 2, R
hb_r = rfm_segmentation.query('R_Quartile == 2').frequency.max()

#Сколько пользователей попало в сегмент 111
c111 = rfm_segmentation[rfm_segmentation['RFMClass'] == '111'].shape[0]

#Сколько пользователей попало в сегмент 311
c311 = rfm_segmentation[rfm_segmentation['RFMClass'] == '311'].shape[0]

#В каком RFM-сегменте самое большое кол-во пользователей 
most_users = rfm_segmentation.reset_index().groupby('RFMClass').CustomerCode.count().sort_values(ascending=False).head(1)
print(most_users)