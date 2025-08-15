# 函数

#定义一个函数计算总价
def calc_total(price,qty):
    return price * qty

print(calc_total(10,2))

# 定义一个函数，返回最大值
def max_number(*args):
    return max(args)

print(max_number(10,20,30,40,50))