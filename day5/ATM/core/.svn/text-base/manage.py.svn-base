#!/usr/bin/env python3
# Author: Zhangxunan
from ATM.core import db


def user_add():
    """
    添加用户
    :return:None
    """
    card_id = input('请输入卡号:').strip()
    username = input('请输入姓名:').strip()
    password = input('请输入密码：')
    credit_line = input('请输入信用额度:').strip()
    user_info = db.get_user_info()
    if card_id in user_info:
        print('\033[31m此卡号已经存在!\033[0m')
        return
    else:
        user_info[card_id] = {
                'name': username,
                'password': password,
                'credit_lines': credit_line,
                'balance': 0,
                'arrears': 0,
                'running_account': [],
                'login_num': 0,
                'status': 1
            }
        db.update_user_info(user_info)
        print('\033[32m添加账户[%s]成功!\033[0m' % card_id)
#        public.write_log(USER_INFO['username'], '添加账户 %s 成功!' % card_id)


def close_account():
    """
    注销账户
    :return:None
    """
    user_info = db.get_user_info()
    card_id = input('请输入注销的信用卡号:').strip()
    if card_id in user_info:
        if user_info[card_id]['arrears'] == 0:
            confirm_choice = input('你确定要注销此用户？(默认为N, Y/y N/n):')
            if confirm_choice == 'Y' or confirm_choice == 'y':
                user_info.pop(card_id)
                db.update_user_info(user_info)
                print('\033[32m注销账户[%s]成功!\033[0m' % card_id)
            elif confirm_choice == '' or confirm_choice == 'N' or confirm_choice == 'n':
                print('\033[33m取消注销[%s]账户!\033[0m' % card_id)
            else:
                print('\033[32m您的输入无效!\033[0m')
        else:
            print('\033[31m您还有欠款%d，还清后才能注销!\033[0m' % user_info[card_id]['arrears'])
    else:
        print('\033[31m此卡号不存在!\033[0m')


def frozen_account():
    """
    冻结账户
    :return:None
    """
    user_info = db.get_user_info()
    frozen_card_id = input('请输入要冻结的账户:').strip()
    if frozen_card_id in user_info:
        confirm_choice = input('你确定要冻结此账户?(默认为N,Y/y N/n):').strip()
        if confirm_choice == 'Y' or confirm_choice == 'y':
            user_info[frozen_card_id]['status'] = 2
            db.update_user_info(user_info)
            print('\033[31m[%s] 账户已经冻结!\033[0m' % frozen_card_id)
        elif confirm_choice == '' or confirm_choice == 'N' or confirm_choice == 'n':
            print('\033[32m账户冻结已取消!\033[0m')
        else:
            print('\033[32m无效的输入!\033[0m')
    else:
        print('\033[32m此卡号不存在!\033[0m')


def credit_lines():
    """
    信用额度
    :return:None
    """
    user_info = db.get_user_info()
    card_id = input('请输入卡号:').strip()
    if card_id in user_info:
        print('%s 的信用额度是:%d' % (card_id, user_info[card_id]['credit_lines']))
        raise_credit = input('请输入提升额度(现有额度+提升额度):')
        if raise_credit.isdigit():
            raise_credit = int(raise_credit)
            if 0 < raise_credit < 100000:
                user_info[card_id]['credit_lines'] += raise_credit
                db.update_user_info(user_info)
            else:
                print('\033[31m提升额度不能是负数或大于100000\033[0m')
        else:
            print('\033[31m输入无效\033[0m')
    else:
        print('\033[31m此卡号不存在!\033[0m')
