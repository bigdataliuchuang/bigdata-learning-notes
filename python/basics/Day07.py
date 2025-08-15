# 模块与标准库

import os
import sys

print("当前目录文件:",os.listdir("."))

# 命令行参数
if len(sys.argv) >=2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print("和：", a + b )