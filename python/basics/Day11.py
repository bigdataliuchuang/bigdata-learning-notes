# 异常处理

# 使用 try/except 捕获错误，使用finally

try:
    a = int(input("请输入数字A："))
    b = int(input("请输入数字B："))
    print(a/b)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("请输入数字")
finally:
    print("程序结束")