# 列表推导式与生成器表达式

sq = [x **2 for x in range(1,10)]
print(sq)

total = sum(x **2 for x in range(1,10))
print( total)