import numpy as np 
# 导入pandas包
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# 读取五大人格测试数据
df_au = pd.read_csv('./data/output_au.csv')
df_ca = pd.read_csv('./data/output_ca.csv')
df_in = pd.read_csv('./data/output_in.csv')
df_uk = pd.read_csv('./data/output_uk.csv')
df_us = pd.read_csv('./data/output_us.csv')
headers = ['ext', 'est', 'agr', 'csn', 'opn', 'dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err', 'Ladder score', 'upperwhisker', 'owerwhisker', 'GDP', 'Social support', 'Healthy life expectancy', 'Freedom', 'Generosity', 'Perceptions of corruption', 'Dystopia + residual']
df_au.columns = headers
df_ca.columns = headers
df_in.columns = headers
df_uk.columns = headers
df_us.columns = headers
df_au.drop(['dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err'],axis=1,inplace= True)
df_in.drop(['dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err'],axis=1,inplace= True)
df_uk.drop(['dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err'],axis=1,inplace= True)
df_us.drop(['dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err'],axis=1,inplace= True)
df_ca.drop(['dateload', 'timestamp', 'screenw', 'screenh', 'introelapse', 'testelapse', 'endelapse', 'country', 'lat_appx_lots_of_err', 'long_appx_lots_of_err'],axis=1,inplace= True)

mean_df_in = df_in.mean()
mean_df_au = df_au.mean()
mean_df_uk = df_uk.mean()
mean_df_us = df_us.mean()
mean_df_ca = df_ca.mean()

p_g = {'country':[ 'America', 'Australia', 'Britain', 'Canada', 'India'], 
       'EXT':[mean_df_us['ext'], mean_df_au['ext'], mean_df_uk['ext'], mean_df_ca['ext'], mean_df_in['ext']],
       'EST':[mean_df_us['est'], mean_df_au['est'], mean_df_uk['est'], mean_df_ca['est'], mean_df_in['est']],
       'AGR':[mean_df_us['agr'], mean_df_au['agr'], mean_df_uk['agr'], mean_df_ca['agr'], mean_df_in['agr']],
       'CSN':[mean_df_us['csn'], mean_df_au['csn'], mean_df_uk['csn'], mean_df_ca['csn'], mean_df_in['csn']],
       'OPN':[mean_df_us['opn'], mean_df_au['opn'], mean_df_uk['opn'], mean_df_ca['opn'], mean_df_in['opn']],
       'Ladder score':[mean_df_us['Ladder score'], mean_df_au['Ladder score'], mean_df_uk['Ladder score'], mean_df_ca['Ladder score'], mean_df_in['Ladder score']],
       'upperwhisker':[mean_df_us['upperwhisker'], mean_df_au['upperwhisker'], mean_df_uk['upperwhisker'], mean_df_ca['upperwhisker'], mean_df_in['upperwhisker']], 
       'owerwhisker':[mean_df_us['owerwhisker'], mean_df_au['owerwhisker'], mean_df_uk['owerwhisker'], mean_df_ca['owerwhisker'], mean_df_in['owerwhisker']], 
       'Explained by: Log GDP per capita':[mean_df_us['GDP'], mean_df_au['GDP'], mean_df_uk['GDP'], mean_df_ca['GDP'], mean_df_in['GDP']], 
       'Explained by: Social support':[mean_df_us['Social support'], mean_df_au['Social support'], mean_df_uk['Social support'], mean_df_ca['Social support'], mean_df_in['Social support']], 
       'Explained by: Healthy life expectancy':[mean_df_us['Healthy life expectancy'], mean_df_au['Healthy life expectancy'], mean_df_uk['Healthy life expectancy'], mean_df_ca['Healthy life expectancy'], mean_df_in['Healthy life expectancy']], 
       'Explained by: Freedom to make life choices':[mean_df_us['Freedom'], mean_df_au['Freedom'], mean_df_uk['Freedom'], mean_df_ca['Freedom'], mean_df_in['Freedom']], 
       'Explained by: Generosity':[mean_df_us['Generosity'], mean_df_au['Generosity'], mean_df_uk['Generosity'], mean_df_ca['Generosity'], mean_df_in['Generosity']], 
       'Explained by: Perceptions of corruption':[mean_df_us['Perceptions of corruption'], mean_df_au['Perceptions of corruption'], mean_df_uk['Perceptions of corruption'], mean_df_ca['Perceptions of corruption'], mean_df_in['Perceptions of corruption']], 
       'Dystopia + residual':[mean_df_us['Dystopia + residual'], mean_df_au['Dystopia + residual'], mean_df_uk['Dystopia + residual'], mean_df_ca['Dystopia + residual'], mean_df_in['Dystopia + residual']]}
df_person_global = pd.DataFrame(p_g)
print(df_person_global.head)
df_person_global.to_csv('./data/person_global.csv',index=False)
