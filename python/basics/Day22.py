# 类与对象

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('张三',18)
print(p.name,p.age)
