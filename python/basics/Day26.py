#私有属性与方法

class Student:
    def __init__(self):
        self.__score = 0
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
    def get_score(self):
        return self.__score

s = Student()
s.set_score(60)
print(s.get_score())