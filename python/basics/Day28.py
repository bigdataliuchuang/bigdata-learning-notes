# 综合练习

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Admin(User):
    def ban_user(self,user):
        print(f"{user.username} 已被封禁")

u1 = User("admin","123456")
admin = Admin("admin","123456")
admin.ban_user(u1)