import csv
#以ca为例，若处理其他国家则更改文件名与list_to_add

# 1. 读取原始CSV文件并处理数据
input_file = 'ca_records.csv'
output_file = 'ca_output.csv'

# 读取原始CSV文件
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)  # 将所有数据读取为一个列表

# 处理数据：在每一行后面添加一个列表
processed_data = []
list_to_add = [6.900,6.984,6.815,1.840,1.459,0.701,0.730,0.230,0.368,1.572]  # 要添加到每一行末尾的ca特征列表

for row in data:
    extended_row = row + list_to_add
    processed_data.append(extended_row)

# 2. 将处理后的数据写入新的CSV文件
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(processed_data)

print(f'处理完成，结果保存在 {output_file}')
