# 内置函数

names = ['tom', 'lucy', 'jim', 'tom']

upper = list(map(str.upper, names))
print(upper)

nums = [1, 2, 3, 4, 5]
# 偶数
eve = list(filter(lambda x: x % 2 == 0, nums))
print(eve)

score = {"Tom":90 , "Alice":85, "Bob":95}

# 排序
sort = sorted(score.items(), key=lambda x:x[1], reverse=True)
print(sort)