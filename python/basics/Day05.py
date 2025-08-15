# 条件判断与循环
# if elif else
# for while

# 输入成绩判断等级
score = int(input("请输入成绩："))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("及格")
elif score >= 60:
    print("及格")
else:
    print("不及格")

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()

