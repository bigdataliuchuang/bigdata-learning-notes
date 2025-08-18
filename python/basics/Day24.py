# 类变量与实例变量

class Person:
    count = 0 # 类变量
    def __init__(self,name,age):
        self.name = name # 实例变量
        Person.count +=1

p1 = Person('Tom',18)
p2 = Person('Jerry',20)
print(Person.count)