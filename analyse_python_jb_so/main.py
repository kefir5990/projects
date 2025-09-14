import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from scipy.stats import bootstrap

#Считывание данных JetBrains
py_df = pd.read_csv('2020_sharing_data_outside.csv', low_memory=False)

general_columns = ['age',
                   'are.you.datascientist',
                   'is.python.main',
                   'company.size',
                   'country.live',
                   'employment.status',
                   'first.learn.about.main.ide',
                   'how.often.use.main.ide',
                   'is.python.main',
                   'main.purposes'
                   'missing.features.main.ide'
                   'nps.main.ide',
                   'python.version.most',
                   'python.years',
                   'python2.version.most',
                   'python3.version.most',
                   'several.projects',
                   'team.size',
                   'use.python.most',
                   'years.of.coding'
                  ]

def column_multi_name(column_name):
    if column_name in general_columns:              
        return ('general', column_name)             
    else:
        first, rest = column_name.rsplit('.', 1)    
        return (first, rest)  

py_df.columns = (
    pd
    .MultiIndex.from_tuples([
    column_multi_name(one_column_name)
    for one_column_name in py_df.columns ])
) 

py_df = py_df[sorted(py_df.columns)]

#Топ 10 сред для разработки
top10_ide = py_df['ide', 'main'].value_counts().head(10)

#Топ 10 языков программирования
top10_lang = py_df['other.lang'].agg('count').sort_values(ascending=False).head(10)

#Топ 10 полностью представленных стран
top10_full_presented_countries = py_df[('general', 'country.live')].value_counts().head(10)

#Процент разработчиков на Python
py_devs_percent = py_df[('general', 'python.years')].value_counts(normalize=True)

#Разработчики с большим опытом
high_exp_devs = py_df['general'][py_df[('general', 'python.years')] == '11+years'].groupby('country.live')['python.years'].count().sort_values(ascending=False).head(1)

#Считывание данных StackOverflow
so_df = pd.read_csv('survey_results_public.csv', low_memory=False)
pd.options.display.float_format = '{:,.2f}'.format

#Средняя зарплата
mean_salary = so_df.groupby('Employment')['ConvertedCompYearly'].mean().sort_values(ascending=False).dropna()

#Таблица уровней знания
table_edlevel = so_df.pivot_table(index='Country', columns='EdLevel', values='ConvertedCompYearly')

#Количество разработчиков, работавших с Python
so_df = so_df.dropna(subset='LanguageHaveWorkedWith')
so_df = so_df[so_df['LanguageHaveWorkedWith'].str.contains('Python')].shape[0]

print()



