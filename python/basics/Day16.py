# 参数类型
# 掌握 *args  **kwargs

# 函数
def greet(name = "Python"):
    print(f"Hello",{name})
# 参数
def sum_all(*args):
    return sum(args)

# 关键字参数
def print_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

greet()
print(sum_all(1,2,3,4,5))
print_info(name="Python",age=18)