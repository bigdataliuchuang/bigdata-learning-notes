# 日期和时间

from datetime import datetime,timedelta

now = datetime.now()
print("当前时间",now)

future = now + timedelta(days=3)
print("3天后的时间",future)

print("格式化：",now.strftime("%Y-%m-%d %H:%M:%S"))