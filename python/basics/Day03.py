# Day03 字典（dict) 操作
# 字典（dict） 是一种无序的存储数据类型，数据是键值对，用{}表示，键是唯一的，值可以重复。
# 字典增删改查，遍历 key value
# 使用 dict 、keys 、values 、items 、get 、setdefault 、pop 、popitem 、clear 、update 、
# in 、not in 、len 、max 、min 、sum 、sorted 、reversed 、tuple 、list 、str 、set 、dict 、range 、zip 、

# 创建字典
d = {'name': '张三', 'age': 20, 'score': 90}

# 用 dict() 构造
d2 = dict(name='李四', age=22, score=85)

# 从键值对列表构造
d3 = dict([('name', '王五'), ('age', 25)])

# 增  改
d['gender'] = '男'
print("增加元素", d)