# 类方法与静态方法

# 类方法
class Person:
    count = 0 # 类变量
    @classmethod  # 类方法
    def get_count(cls):
        return cls.count
    @staticmethod # 静态方法
    def say_hello():
        print("hello")

Person.say_hello()
print(Person.get_count())


import sys
print(sys.executable)

