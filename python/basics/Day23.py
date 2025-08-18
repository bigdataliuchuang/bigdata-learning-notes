# 实例方法与属性
# 会定义实例方法会访问属性

class Person:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f'我的名字是 {self.name}')

p = Person("张三")
p.speak()