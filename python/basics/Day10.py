# Json 读写


import json

user = {"name":"张三","age":18,"sex":"男","city":"北京"}
path_json = "/Users/liuchuang/Downloads/github/bigdata-learning-notes/python/file/user.json"

# 写入json文件
with open(path_json,"w",encoding="utf-8" ) as f:
    json.dump(user,f,ensure_ascii=False)

# 读取json文件
with open(path_json,"r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)