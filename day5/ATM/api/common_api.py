#!/usr/bin/env python3
# Author: Zhangxunan
import time
from ATM.core import db


def credit_bind(card_id, password):
    """
    绑定信用卡
    :param card_id: 卡号
    :param password: 密码
    :return: True or False
    """
    user_dict = db.get_user_info()
    if card_id in user_dict:
        if password == user_dict[card_id]['password']:
            return True
        else:
            return False
    else:
        return False


def checkout(card_id, password, total_amount):
    """
    结账，先从余额里扣，没有余额就从信用额度里扣
    :param card_id: 信用卡号
    :param password: 密码
    :param total_amount: 扣费总金额
    :return: 1.代表密码错误;2.余额不足;0.代表成功
    """
    user_dict = db.get_user_info()
    if user_dict[card_id]['password'] != password:
        return {'code': 1}
    else:
        if total_amount > user_dict[card_id]['balance']:
            tmp = total_amount - user_dict[card_id]['balance']
            if tmp > float(user_dict[card_id]['credit_lines']) - float(user_dict[card_id]['arrears']):
                return {'code': 2}
            else:
                user_dict[card_id]['arrears'] += tmp
                user_dict[card_id]['balance'] = 0
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                running_account = [current_time, -total_amount, '购物']
                user_dict[card_id]['running_account'].append(running_account)
                db.update_user_info(user_dict)
                return {'code': 0}
        else:
            user_dict[card_id]['balance'] -= total_amount
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            running_account = [current_time, -total_amount, '购物']
            user_dict[card_id]['running_account'].append(running_account)
            db.update_user_info(user_dict)
            return {'code': 0}

