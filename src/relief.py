import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import confusion_matrix, classification_report
import math
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import random
def clean_and_convert(x):
    if isinstance(x, str):
        x = x.replace('"', '').replace("'", '')  # 去除单引号和双引号
        return float(x)  # 转换为浮点数
    else:
        return float(x)  # 如果是整数，直接转换为浮点数
def to_pd(input):
    df = pd.read_csv(input)
    #一下数据与本次问题无关
    df=df.drop(df.columns[14],axis=1)
    df=df.drop(df.columns[12],axis=1)
    df=df.drop(df.columns[5],axis=1)
    df=df.drop(df.columns[5],axis=1)  
    df=df.applymap(clean_and_convert)
    return df

df1=to_pd('data/output_au.csv')
df2=to_pd('data/output_ca.csv')
df3=to_pd('data/output_uk.csv')
df4=to_pd('data/output_us.csv')
df5=to_pd('data/output_in.csv')



# 进行因子分析
fa = FactorAnalysis(n_components=5)
df=np.vstack([df1,df2,df3,df4,df5])
fa.fit(df)
df=pd.DataFrame(df)
# 查看因子负荷矩阵
loadings = pd.DataFrame(fa.components_.T, index=df.columns)
print(loadings)

# 绘制碎石图（Scree Plot）
evr = fa.noise_variance_
plt.plot(np.arange(1, len(evr) + 1), evr, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Components')
plt.ylabel('Explained Variance Ratio')
plt.xticks(np.arange(1, len(evr) + 1))
plt.title('global reliable')
plt.show()


from pingouin import reliability

# 计算 Cronbach's α
alpha = reliability.cronbach_alpha(df[0:5])

print(f"Cronbach's α: {alpha}")
