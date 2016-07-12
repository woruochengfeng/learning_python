#!/usr/bin/env python3
# Author: Zhangxunan
import os
import sys
# 程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 添加环境变量
sys.path.append(BASE_DIR)

from ATM.core import credit

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('用法: %s start' % sys.argv[0])
        sys.exit(0)

    credit.main()
