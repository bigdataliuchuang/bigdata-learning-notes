import os
# 文件读取与写入

# 获取当前文件路径
path = os.path.abspath(__file__)

# 文件路径
path_txt = '/Users/liuchuang/Downloads/github/bigdata-learning-notes/python/file/students.txt'

# 写入
# with open(path_txt,'w') as f:
#     f.write("张三\n李四\n王五\n")

# 读取
with open(path_txt,'r',encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 追加
with open(path_txt,'a',encoding="utf-8") as f:
    f.write("赵六\n")