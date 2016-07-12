#!/usr/bin/env python3
# Author: Zhangxunan
import time

from ATM.core import db


def init_db():
    """
    初始化数据库
    :return:None
    """
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    user_info = {
        '622622': {
            'name': 'tom',
            'password': '123456',
            'credit_lines': 30000,
            'balance': 0,
            'arrears': 0,
            'overdue': 0,
            'running_account': [[current_time, -100, '转账'], ],
            'login_num': 0,
            'status': 1,
        }
    }

    admin_info = {
        'admin': ['123456', 1]
    }

    db.update_user_info(user_info)
    db.update_user_info(admin_info, 1)


init_db()
