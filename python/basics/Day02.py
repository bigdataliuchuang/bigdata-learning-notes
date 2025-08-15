# Day 2: 列表操作
# 列表创建，增删改查，切片，排序
# 使用 append 、insert 、pop、remove 、del 、clear 、index 、count 、sort
# reverse 、copy 、extend 、+ 、* 、in 、not in 、max 、min 、sum 、len 、
# sorted 、reversed 、
# tuple 、list 、str 、set 、dict 、range 、zip 、

## 列表创建
lst = [10,20,30]
lst2 = list((40,50,60))
lst3 = []
print("初始化列表：" ,lst)

# 增加元素
lst.append(70)  #末尾追加
lst.insert(0,15) # 索引指定插入
lst.extend([80,90]) # 追加多个元素
lst = lst + [100,110] # 使用 + 拼接列表
lst = lst * 2 # 使用 * 列表复制
print("增加元素后：",lst)

# 删除元素
lst.pop() # 删除末尾元素
lst.pop(0) # 删除指定索引元素
lst.remove(20) # 删除指定元素
del lst[0] # 删除指定索引元素
del lst[0:2] # 按照切片删除
# lst.clear() # 清空列表
print("删除元素后：",lst)

# 修改元素
lst[0] = 999 # 直接修改指定位置元素
lst [1:3] = [888,777]  # 使用切片修改 ，修改90 100
print("修改元素后：",lst)

# 查询元素
print("查询索引：",lst.index(888)) # 查询元素索引
print("数据出现次数：",lst.count(888))
print("列表长度：" ,len(lst))
print("最大值:",max(lst))
print("最小值:",min(lst))
print("总和:",sum(lst))
print("元素是否存在：", 15 in lst)
print("元素是否不存在：", 15 not in lst)

# 排序
lst.sort() # 升序
lst.sort(reverse=True) # 降序
print("排序后：",lst)

new_lst = sorted(lst) # 返回新列表（升序）
print("sorted 排序",new_lst)

# 反转
lst.reverse()
print("reverse 反转",lst)

rev_list = reversed(lst)  # 返回迭代器
print("reversed 反转",list(rev_list))

# 复制

lst_copy = lst.copy() #浅拷贝
lst_copy2 = list(lst) #用构造方法复制
print("复制结果：" , lst_copy,lst_copy2)

# 切片 左毕右开 [10, 15, 20, 30, 70, 80, 90, 100, 110, 777, 888, 999]
#               0   1   2   3   4   5   6   7    8   9    10   11
print("切片[1:4]",lst[1:4])
print("步长切片：",lst[::2])
print("反向切片：",lst[::-1])

# 其他数据结构互转

tup = tuple(lst) # 列表转元祖
print("元祖：",tup)
st = set(lst) # 列表转集合
print("集合：",st)
dct = dict(zip(range(len(lst)),lst)) # zip 组合转字典
print("字典：",dct)
rng = list(range(10)) # range生成列表
print("range：",rng)
s = str(lst) # 列表转字符串
print("字符串：",s)

# zip

names = ["张三","李四","王五"]
score = [90,80,70]
zipped = list(zip(names,score))
print("zip：",zipped)