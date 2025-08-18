# 匿名函数与内置函数结合
# 会写lambda匿名函数
# 会与map() filter() sorted() 结合

# 用lambda 求平方
sq = lambda x: x**2
print(sq(5))

# 用map结合lambda转成大写
names = ['tom', 'lucy', 'jim', 'tom']
print(list(map(lambda x: x.upper(), names)))

# 用filter 过滤偶数

nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))