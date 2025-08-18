# 继承与方法重写

# 父类
class Person:
    def speak(self):
        print("Person speaking")

# 子类
class Student(Person):
    def speak(self):
        print("Student speaking")

s = Student()
s.speak()