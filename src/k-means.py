import numpy as np 
# 导入pandas包
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# 读取五大人格测试数据
df = pd.read_csv('./data/data-final.csv', delimiter='\t')
print(df.head())

df = df.dropna()
df.drop(['introelapse', 'testelapse', 'endelapse', 'dateload','lat_appx_lots_of_err','long_appx_lots_of_err','IPC','screenh','screenw'],axis=1,inplace= True)
#print(df.head())

df = df[(df!=0).all(axis=1)]

#k-means数据构建
df2 = df.iloc[:,0:50]
df3 = df2.copy()
#print(df2.head())

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
k_fit = kmeans.fit(df2)
predictions = k_fit.labels_
df2['Clusters'] = predictions 
print(df2.head())

Clu_nums = df2['Clusters'].value_counts()
print(Clu_nums)
df2['score_sum']=df.iloc[:,0:50].sum(axis=1)
print(df2.groupby('Clusters')['score_sum'].mean())

df2['EXT_sum']=df.iloc[:,0:10].sum(axis=1)
df2['EST_sum']=df.iloc[:,10:20].sum(axis=1)
df2['AGR_sum']=df.iloc[:,20:30].sum(axis=1)
df2['CSN_sum']=df.iloc[:,30:40].sum(axis=1)
df2['OPN_sum']=df.iloc[:,40:50].sum(axis=1)
print(df2.head())

EXT_sum = df2.groupby('Clusters')['EXT_sum'].mean()/10
EST_sum = df2.groupby('Clusters')['EST_sum'].mean()/10
AGR_sum = df2.groupby('Clusters')['AGR_sum'].mean()/10
CSN_sum = df2.groupby('Clusters')['CSN_sum'].mean()/10
OPN_sum = df2.groupby('Clusters')['OPN_sum'].mean()/10
Clus_5 = {'Clusters':EXT_sum.index,'EXT_s':EXT_sum.values,'EST_s':EST_sum.values,'AGR_s':AGR_sum.values,'CSN_s':CSN_sum.values,'OPN_s':OPN_sum.values}
df_Clus_5 = pd.DataFrame(Clus_5)
print(df_Clus_5)

dataclusters = df_Clus_5.groupby('Clusters').mean()
plt.figure(figsize=(22,3))
for i in range(0, 5):
    plt.subplot(1,5,i+1)
    plt.bar(dataclusters.columns, dataclusters.iloc[:, i], color='green', alpha=0.2)
    plt.plot(dataclusters.columns, dataclusters.iloc[:, i], color='red')
    plt.title('Cluster ' + str(i))
    plt.xticks(rotation=45)
    plt.ylim(0,4);

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_fit = pca.fit_transform(df3)

df_pca = pd.DataFrame(data=pca_fit, columns=['PCA1', 'PCA2'])
df_pca['Clusters'] = predictions
print(df_pca.head())

plt.figure(figsize=(10,10))
sns.scatterplot(data=df_pca, x='PCA1', y='PCA2', hue='Clusters', palette='tab10', alpha=0.8)
plt.title('Personality Clusters after PCA');

'''
my_data = pd.read_excel('my_personality.xlsx')
my_personality = k_fit.predict(my_data)
print('我的个性分类: ', my_personality)
'''