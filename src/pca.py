import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv
# 假设有三个数据集，每个数据集都是一个矩阵，行数相同
def to_ndarray(input_file):
    with open(input_file, 'r', newline='') as csvfile:
         reader = csv.reader(csvfile)
         data = list(reader) 
    for row in data:
        del row[14]
        del row[12]
        del row[5]
        del row[5]
       # row=[cell.replace('"', '') for cell in row]
        row=[cell.replace('\\n', '') for cell in row]
    sum=0
    
    data_array = np.array(data, dtype=float)
    return data_array

# 生成三个随机数据集
au=to_ndarray('data/output_au.csv')
ca=to_ndarray('data/output_ca.csv')
inn=to_ndarray('data/output_in.csv')
uk=to_ndarray('data/output_uk.csv')
us=to_ndarray('data/output_us.csv')
s_au=au.shape[0]
s_ca=ca.shape[0]
s_inn=inn.shape[0]
s_uk=uk.shape[0]
s_us=us.shape[0]


# 合并三个数据集为一个大的数据矩阵
all_data = np.vstack([au,ca,inn,uk,us])

# 创建PCA对象，指定保留的主成分数量为2
pca = PCA(n_components=10)

# 在所有数据上进行PCA
principal_components = pca.fit_transform(all_data)

# 提取每个数据集对应的主成分数据
pc_data1 = principal_components[:s_au]
pc_data2 = principal_components[s_au:s_ca]
pc_data3 = principal_components[s_ca:s_inn]
pc_data4=principal_components[s_inn:s_uk]
pc_data5=principal_components[s_uk:]

# 可视化主成分分析结果
plt.figure(figsize=(20, 30))
plt.scatter(pc_data1[:1000, 0], pc_data1[:1000, 1], color='b', label='au', alpha=1)
plt.scatter(pc_data2[:1000, 0], pc_data2[:1000, 1], color='g', label='ca', alpha=1)
plt.scatter(pc_data3[:1000, 0], pc_data3[:1000, 1], color='r', label='inn', alpha=1)
plt.scatter(pc_data4[:1000, 0], pc_data4[:1000, 1], color='c', label='uk', alpha=1)
plt.scatter(pc_data5[:1000, 0], pc_data5[:1000, 1], color='y', label='us', alpha=0.5)
plt.title('PCA of five Datasets')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)
plt.show()
