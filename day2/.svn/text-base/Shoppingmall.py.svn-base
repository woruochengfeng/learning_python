#!/usr/bin/env python3
# Author: Zhangxunan

import getpass
import sys
import json
import time
shoppingmall = {
    '汽车类':{
        'BMW X3':33333,
        'Audi Q5':33355,
        'Pasate':55566,
        'Tesla Model S': 8888888
    },
    '家电类':{
        '小米电视3S':8999,
        '乐视超级电视X65':5998,
        '格力空调':3000,
        '海尔洗衣机':4000
    },
    '衣服类':{
        'HM':299,
        'UNIQLO':199,
        'JackJones':300,
        'Adidas':700
    },
    '手机类':{
        '小米手机5':1999,
        'iPhone6s Plus':6888,
        '华为P9 Plus': 4388,
        'OPPO R9 Plus': 3299
    }
}
#获取用户信息，包括用户名，密码，余额
def get_user_info():
    f = open('user.txt','r')
    users_info = json.load(f)
    f.close()
    return users_info

#用户注册
def user_register(username,password,salary):
    f = open('user.txt','r')
    user_info = json.load(f)
    f.close()
    user_info[username] = [password,salary]
    f = open('user.txt','w')
    json.dump(user_info,f)
    f.close()

#用户登录
def user_login():
    while True:
        username = input("username:").strip()
        password = getpass.getpass('password:')
        users_info = get_user_info()
        if username in users_info and users_info[username][0] == password:
            print("登录成功")
            break
        else:
            print('用户名或密码错误，请重新输入')
    return {username:users_info[username]}

#充值
def recharge(username,balance,recharge_money):
    f = open('user.txt','r')
    user_info = json.load(f)
    balance += recharge_money
    user_info[username][1]=balance
    f = open('user.txt','w')
    json.dump(user_info,f)
    f.close()
    return balance
#结账
def close_accounts(username,balance,total_money):
    if balance >= total_money:
        balance -= total_money
        f = open('user.txt','r')
        user_info = json.load(f)
        user_info[username][1]=balance
        f = open('user.txt','w')
        json.dump(user_info,f)
        return balance
    else:
        return -1
#写购物记录到文件里
def write_shopping_records(username,shopping_cart):
    f = open('shopping_records.txt', 'r')
    shopping_record = json.load(f)
    shopping_date = time.strftime('%Y-%m-%d %H:%M:%S')
    if username in shopping_record:
        shopping_record[username][shopping_date] = shopping_cart
    else:
        shopping_record[username]={shopping_date:shopping_cart}
    f = open('shopping_records.txt','w')
    json.dump(shopping_record,f)
    f.close()

#读购物记录
def read_shopping_records(username):
    f = open('shopping_records.txt','r')
    shopping_records = json.load(f)
    f.close()
    if username in shopping_records:
        shopping_records = shopping_records[username]
        #按日期排序
        date_list = list(shopping_records.keys())
        date_list.sort()
        date_list.reverse()
        for shopping_date in date_list:
            print(shopping_date.center(40,'-'))
            print('%s\t%s\t%s\t%s' % ('商品', '单价', '数量', '总计'))
            for product in shopping_records[shopping_date]:
                print('\t'.join([str(pro) for pro in product]))
            print('\n')
    else:
        print('您还没有购物记录!')
#    return shopping_records

#购物车的商品总共多少钱
total_money = 0
consumption_amount = 0
#购物车
shopping_cart= []

while True:
    info = input('欢迎来到XX购物商城，你是否已经有账号?(Y/y(登录) N/n(注册)):')
    if info == 'Y' or info == 'y':
        break
    elif info == 'N' or info == 'n':
        username = input('请你输入要注册的用户名:')
        password = getpass.getpass('设置您的密码：')
        balance = input('请输入您要存入的钱：')
        user_register(username, password, balance)
        break
    else:
        print('您输入了无效的选项，只能是Y/y N/n')

user_info = user_login()
username = list(user_info.keys())[0]
balance = int(user_info[username][1])


#start_menu = '''
#    1.查询余额      2.充值
#    3.购物记录      4.购物
#    0.退出
#'''

start_menu = {
     1:'查询余额',
     2:'充值',
     3:'购物记录',
     4:'购物',
     5:'退出'
}


first_level_menu = {}
second_level_menu = {}

shoppingmall_keys = list(shoppingmall.keys())
shoppingmall_keys.sort()
for i,v in enumerate(shoppingmall_keys,1):
    first_level_menu[i] = v

while True:
    print('菜单'.center(20,'*'))
    for item in start_menu:
        print(item,start_menu[item])
    print('菜单'.center(20, '*'))
    start_menu_num = input('请选择:').strip()
    if start_menu_num.isdigit():
        start_menu_num = int(start_menu_num)
        if start_menu_num in start_menu:
            if start_menu_num == 1:
                print('您的余额为:%d 元' % balance)
                continue
            elif start_menu_num == 2:
                while True:
                    recharge_money = input('请输入您要充值的金额(单位:元):').strip()
                    if recharge_money.isdigit():
                        recharge_money = int(recharge_money)
                        if recharge_money < 0:
                            print('不能输入负数')
                            continue
                        break
                    else:
                        print('只能输入数字')
                        continue
                balance = recharge(username, balance, recharge_money)
                continue
            elif start_menu_num == 3:
                read_shopping_records(username)
                continue
            elif start_menu_num == 4:
                pass
            elif start_menu_num == 5:
                sys.exit(0)
            else:
                continue
        else:
            continue
    else:
        continue
    while True:
        print('购物区'.center(20,'*'))
        for item in first_level_menu:
            print(item,first_level_menu[item])
        print('购物区'.center(20, '*'))
        if len(shopping_cart) != 0:
            print('已经加入到购物车的商品:')
            print('%-15s%-10s%-5s%-8s' % ('商品', '单价', '数量', '总计'))
            for i in range(len(shopping_cart)):
                print('%-15s%-10s%-5s%-8s' % (shopping_cart[i][0], shopping_cart[i][1], shopping_cart[i][2], shopping_cart[i][3]))
        choice_first_num = input('请选择(q:退出 b返回):')
        if choice_first_num.isdigit():
            choice_first_num = int(choice_first_num)
            if choice_first_num not in first_level_menu:
                print("请输入一个有效的编号")
                continue
        elif choice_first_num == 'q' or choice_first_num == 'quit':
            sys.exit(0)
        elif choice_first_num == 'b' or choice_first_num == 'back':
            break
        else:
            print('您必须输入编号而不是其它!')
            continue


        shoppingmall_sencond_keys = list(shoppingmall[first_level_menu[choice_first_num]].keys())
        shoppingmall_sencond_keys.sort()
        for i,v in enumerate(shoppingmall_sencond_keys,1):
            second_level_menu[i] = v
        while True:
            print('%s'.center(20,'*') % first_level_menu[choice_first_num])
            for item in second_level_menu:
                print(item,second_level_menu[item],shoppingmall[first_level_menu[choice_first_num]][second_level_menu[item]])
            print('%s'.center(20, '*') % first_level_menu[choice_first_num])

            choice_second_num = input("请输入商品的编号数量(格式：编号 数量)或结账:s 返回上一级:b退出:q:").strip()
            choice_second_num_list = choice_second_num.split()
            if len(choice_second_num_list) == 0:
                continue
            if len(choice_second_num_list) == 1:
                if choice_second_num_list[0] == 's':
                    res = close_accounts(username,balance,consumption_amount)
                    if res == -1:
                        print('您的账户的钱不足，请充值!')
                        break
                    else:
                        balance = res
                        write_shopping_records(username,shopping_cart)
                        print('您总共消费了 %d 元您的余额还有 %d 元!' % (consumption_amount, balance))
                        shopping_cart = []
                        break
                elif choice_second_num_list[0] == 'q' or choice_second_num_list[0] == 'quit':
                    sys.exit(0)
                elif choice_second_num_list[0] == 'b' or choice_second_num_list[0] == 'back':
                    break
                else:
                    continue
            for i in range(len(choice_second_num_list)):
                if choice_second_num_list[i].isdigit():
                    choice_second_num_list[i] = int(choice_second_num_list[i])
                    if choice_second_num_list[i] not in second_level_menu:
                        print('请输入有效的编号或数量!')
                        continue
                else:
                    print('必须输入编号,数量而不是其它!')
                    continue
            name_of_goods = second_level_menu[choice_second_num_list[0]]
            unit_price_of_goods = shoppingmall[first_level_menu[choice_first_num]][second_level_menu[choice_second_num_list[0]]]
            number_of_goods =  choice_second_num_list[1]
            total_price = unit_price_of_goods * number_of_goods
            if len(shopping_cart) != 0:
                for record in shopping_cart:
                    if record[0] == name_of_goods:
                        record[2] += number_of_goods
                        record[3] += total_price
                        break
                else:
                    shopping_cart.append([name_of_goods, unit_price_of_goods, number_of_goods, total_price])
            else:
                shopping_cart.append([name_of_goods,unit_price_of_goods,number_of_goods,total_price])

            print('已经加入到购物车的商品:')
            print('%-15s%-10s%-5s%-8s' %('商品','单价','数量','总计'))
            for i in range(len(shopping_cart)):
                total_money += shopping_cart[i][3]
                print('%-15s%-10s%-5s%-8s' % (shopping_cart[i][0],shopping_cart[i][1],shopping_cart[i][2],shopping_cart[i][3]))
            print('总金额: %d 元'.rjust(30,' ') % total_money)
            consumption_amount = total_money
            total_money = 0







