# 返回值与作用域
#理解函数返回值
# 理解局部变量和全局变量

def get_user():
    return "Tom",20

name , age = get_user()
print(name,age)

count = 0
# 函数中定义的变量，是局部变量
def increment():
    global count
    count += 1

increment()
print(count)
