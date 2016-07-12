#!/usr/bin/env python3
# Author: Zhangxunan
import os
import sys
import time

from prettytable import PrettyTable

from ATM.core import db, manage
from ATM.core import public

USER_INFO = {'is_login': False}


def start_menu():
    """
    开始菜单
    :return:None
    """
    menu_start = '''
        1.普通用户登录    2.管理员登录
        0.退出
    '''
    print(menu_start)


def ordinary_menu():
    """
    普通用户菜单
    :return:None
    """
    menu_ordinary = """
        1.个人信息      2.提－－现
        3.还－－款      4.打印账单
        5.转－－账      0.退－－出
    """
    print(menu_ordinary)


def manager_menu():
    """
    管理员菜单
    :return: None
    """
    menu_manager = """
        1.添加用户      2.注销账户
        3.冻结账户      4.信用额度
        0.退－－出
    """
    print(menu_manager)


def login(role=2):
    """
    登录
    :return:None
    """
    if role == 1:
        user_dict = db.get_user_info(1)
        username = input('用户名:')
        password = input('密码:')
        if username in user_dict:
            if password == user_dict[username][0]:
                USER_INFO['username'] = username
                USER_INFO['is_login'] = True
                print('\033[32m管理员 %s 您好!\033[0m' % username)
            else:
                print('\033[31m密码错误!\033[0m')
        else:
            print('\033[31m用户名不存在!\033[0m')
    else:
        user_dict = db.get_user_info()
        card_id = input('信用卡号:').strip()
        password = input('密码:')
        if card_id in user_dict:
            if user_dict[card_id]['status'] == 1:
                if password == user_dict[card_id]['password']:
                    USER_INFO['username'] = user_dict[card_id]['name']
                    USER_INFO['card_id'] = card_id
                    USER_INFO['is_login'] = True
                    user_dict[card_id]['login_num'] += 1
                    db.update_user_info(user_dict)
                    print('\033[32m登录成功，欢迎 %s 先生/女士,这是您第 %d 登录!\033[0m' %
                          (user_dict[card_id]['name'], user_dict[card_id]['login_num']))
                else:
                    print('\033[31m密码错误!\033[0m')
            else:
                print('\033[31m您的账户已经冻结!\033[0m')
        else:
            print('\033[32m此卡号不存在!\033[0m')


def show_info():
    """
    显示用户信息
    :return: None
    """
    x = PrettyTable(["卡号", "姓名", "信用额度", "余额", "欠款", "登录次数"])
    x.align["时间"] = "l"
    x.padding_width = 1
    user_info = db.get_user_info()
    card_id = USER_INFO['card_id']
    user = [card_id]
    fields = ['name', 'credit_lines', 'balance', 'arrears', 'login_num']
    for item in fields:
        user.append(user_info[card_id][item])
    x.add_row(user)
    print(x)
    public.write_log(USER_INFO['username'], '[查看]查看自己的用户信息')


def transfers():
    """
    转账，转账等于提现
    :return:None
    """
    user_info = db.get_user_info()
    card_id = USER_INFO['card_id']
    credit_line = float(user_info[card_id]['credit_lines'])
    arrears = float(user_info[card_id]['arrears'])
    balance = float(user_info[card_id]['balance'])
    trans_quota = credit_line*0.5+balance-arrears
    print('\033[34m您最多可转账[%.2f]元!\033[0m' % trans_quota)
    card_num = input('请输入对方的账户(信用卡号):')
    if card_num in user_info:
        print('您要给[%s]转账!' % user_info[card_num]['name'])
        trans_money = input('请输入转账金额:')
        if trans_money.isdigit():
            trans_money = int(trans_money)
            if trans_money > trans_quota:
                print('\033[31m您转账的金额超过了可转账的金额!\033[0m')
            else:
                if user_info[card_num]['arrears'] == 0:
                    user_info[card_num]['balance'] += trans_money
                else:
                    if trans_money > user_info[card_num]['arrears']:
                        user_info[card_num]['balance'] = trans_money - user_info[card_num]['arrears']
                        user_info[card_num]['arrears'] = 0
                    else:
                        user_info[card_num]['arrears'] -= trans_money
                # 收账账户的流水
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                running_account = [current_time, trans_money, '转账']
                user_info[card_num]['running_account'].append(running_account)
                # 转账账户的流水
                if user_info[card_id]['balance'] == 0:
                    user_info[card_id]['arrears'] += trans_money
                else:
                    if user_info[card_id]['balance'] > trans_money:
                        user_info[card_id]['balance'] -= trans_money
                    else:
                        user_info[card_id]['arrears'] = user_info[card_id]['arrears'] + \
                                                        trans_money-user_info[card_id]['balance']
                        user_info[card_id]['balance'] = 0
                running_account = [current_time, -trans_money, '转账']
                user_info[card_id]['running_account'].append(running_account)
                db.update_user_info(user_info)
                print('\033[32m您向[%s]转账成功!\033[0m' % user_info[card_num]['name'])
                public.write_log(USER_INFO['username'], '[转账]向%s转账成功!' % user_info[card_num]['name'])
        else:
            print('\033[31m您的输入无效!\033[0m')
    else:
        print('\033[31m此卡号不存在!\033[0m')


def cash_advance():
    """
    信用卡提现，提现最多能提你信用额度的一半，如果有余额的话会先从余额里面扣，没有的话才会用信用额度。
    :return:None
    """
    user_info = db.get_user_info()
    card_id = USER_INFO['card_id']
    credit_line = float(user_info[card_id]['credit_lines'])
    arrears = float(user_info[card_id]['arrears'])
    balance = float(user_info[card_id]['balance'])
    cash_quota = credit_line*0.5-arrears+balance
    print('\033[34m根据你的信用额度，您最多能提取你信用额度的一半现金加你的余额!\033[0m')
    print('\033[32m您的信用额度为[%.2f]元, 您的余额为[%.2f]元,您的欠款为[%.2f]元,您最终最多能提现[%.2f]元\033[0m' %
          (credit_line, balance, arrears, cash_quota))

    cash_money = input('请输入您要提取的现金:')
    repay_money = 0
    if cash_money.isdigit():
        cash_money = int(cash_money)
        # 提取的现金为最多为 总额度*0.5-欠款。
        if 0 < cash_money <= cash_quota:
            if cash_money <= balance:
                user_info[card_id]['balance'] -= cash_money
            else:
                repay_money = cash_money - balance
                # 提取现金交5%手续费，交记录到欠款的key里
                user_info[card_id]['arrears'] = float(user_info[card_id]['arrears']) + repay_money*1.05
                user_info[card_id]['balance'] = 0
            # 流水账
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            running_account = [current_time, -cash_money*1.05, '提现']
            user_info[card_id]['running_account'].append(running_account)
            db.update_user_info(user_info)
            print('\033[32m提取现金成功，您提取了[%.2f]元，手续费为[%.2f]元\033[0m' % (cash_money, repay_money*0.05))
            public.write_log(USER_INFO['username'], '[提现]提取%.2f元现金成功' % cash_money)
        else:
            print('\033[31m超出范围!\033[0m')
    else:
        print('\033[31m无效的输入!\033[0m')


def overdue():
    """
    过期未还或者未还完欠款的，按欠款总额的成分之五加息
    :return: None
    """
    user_info = db.get_user_info()
    card_id = USER_INFO['card_id']
    current_time = time.localtime(time.time())
    if current_time.tm_mday > 10 and user_info[card_id]['arrears'] > 0:
        user_info[card_id]['arrears'] *= 1.0005


def repayment():
    """
    还款，如果还清之后，会以余额的方式存到账户里。
    :return:None
    """
    user_info = db.get_user_info()
    card_id = USER_INFO['card_id']
    arrears = user_info[card_id]['arrears']
    if arrears == 0:
        print('\033[34m您有[%2.f]元欠款,已经还清!\033[0m' % arrears)
        return
    else:
        print('\033[34m您还有[%2.f]元欠款!\033[0m' % arrears)
    repay = input('请输入你还款的金额:')
    if repay.isdigit():
        repay = int(repay)
        user_info[card_id]['arrears'] -= repay
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        running_account = [current_time, repay, '还款']
        user_info[card_id]['running_account'].append(running_account)
        db.update_user_info(user_info)
        print('\033[34m您已经还了[%.2f]元，您还欠[%.2f]元!\033[0m' % (repay, user_info[card_id]['arrears']))
        public.write_log(USER_INFO['username'], '[还款]还款%.2f元' % repay)
    else:
        print('\033[31m您的输入无效!\033[0m')


def bill():
    """
    打印账单，打印上个月22号到这个月22号的账单，不到时间不打印
    :return:None
    """
    x = PrettyTable(["时间", "流水", "描述"])
    x.align["时间"] = "l"
    x.padding_width = 1
    current_time = time.localtime(time.time())
    c_mday = current_time.tm_mday
    if c_mday == 22:
        user_info = db.get_user_info()
        card_id = USER_INFO['card_id']
        if user_info[card_id]['running_account']:
            for item in user_info[card_id]['running_account']:
                s_time = time.strptime(item[0], "%Y-%m-%d %H:%M:%S")
                if s_time.tm_mon >= current_time.tm_mon - 1 and s_time.tm_mday >= c_mday:
                    x.add_row(item)
            print(x)
        else:
            print('\033[32m无记录!\033[0m')
    else:
        print('\033[31m还没有到出账单日期!\033[0m')


def ordinary():
    """
    普通用户菜单
    :return: None
    """
    login()
    if not USER_INFO['is_login']:
        return
    else:
        while True:
            ordinary_menu()
            num = input('请输入编号:').strip()
            if num.isdigit():
                num = int(num)
                if num == 1:
                    show_info()
                elif num == 2:
                    cash_advance()
                elif num == 3:
                    repayment()
                elif num == 4:
                    bill()
                elif num == 5:
                    transfers()
                elif num == 0:
                    sys.exit(0)
                else:
                    print('\033[31m请输入正确的编号!\033[0m')
            else:
                if num == '':
                    pass
                else:
                    print('\033[31m必须输入编号!\033[0m')


def manager():
    """
    管理员菜单
    :return:
    """
    login(1)
    if not USER_INFO['is_login']:
        return
    else:
        while True:
            manager_menu()
            num = input('请输入编号:')
            if num.isdigit():
                num = int(num)
                if num == 1:
                    manage.user_add()
                elif num == 2:
                    manage.close_account()
                elif num == 3:
                    manage.frozen_account()
                elif num == 4:
                    manage.credit_lines()
                elif num == 0:
                    sys.exit(0)
                else:
                    print('\033[31m请输入正确的编号!\033[0m')
            else:
                if num == '':
                    pass
                else:
                    print('\033[31m必须输入编号!\033[0m')


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, 'logs')
    public.set_logging(log_dir, 'debug')
    while True:
        start_menu()
        num = input('请选择：')
        if num.isdigit():
            num = int(num)
            if num == 1:
                ordinary()
            elif num == 2:
                manager()
            elif num == 0:
                sys.exit(0)
            else:
                print('\033[31m请输入正确的编号!\033[0m')
        else:
            if num == '':
                pass
            else:
                print('\033[31m只能输入编号!\033[0m')


if __name__ == '__main__':
    main()



