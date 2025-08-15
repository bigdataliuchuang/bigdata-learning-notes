# csv 文件读取与写入

import csv

# 写入

data = [["产品","销量"],["A",100],["B",200]]

path_csv ="/Users/liuchuang/Downloads/github/bigdata-learning-notes/python/file/sales.csv"
with open(path_csv,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 读取
with open(path_csv,'r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)