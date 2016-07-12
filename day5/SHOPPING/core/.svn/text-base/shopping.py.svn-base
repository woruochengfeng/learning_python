#!/usr/bin/env python3
# Author: Zhangxunan
import sys
import os
import time

from prettytable import PrettyTable

from SHOPPING.core import shop_db
from SHOPPING.core import public
from ATM.api import common_api

USER_INFO = {'is_login': False}
SHOPPING_CART = []


def goods_list():
    """
    商品列表
    :return:商品列表字典
    """
    shoppingmall = {
        '汽车类':
            [('BMW X3', '33333'),
             ('Audi Q5', '33355'),
             ('Pasate', '55566'),
             ('Tesla Model S', '8888888')],

        '家电类':
            [('小米电视3S', '8999'),
             ('乐视超级电视X65', '5998'),
             ('格力空调', '3000'),
             ('海尔洗衣机', '4000')],
        '衣服类':
            [('HM', '299'),
             ('UNIQLO', '199'),
             ('JackJones', '300'),
             ('Adidas', '700')],
        '手机类':
            [('小米手机5', '1999'),
             ('iPhone6s Plus', '6888'),
             ('华为P9 Plus', '4388'),
             ('OPPO R9 Plus', '3299')]
    }
    return shoppingmall


def register():
    """
    注册
    :return:None
    """
    user_dict = shop_db.get_user_info()
    username = input('请输入注册的用户名:')
    password = input('请输入密码:')
    confirm_password = input('请再次输入密码:')
    if username in user_dict:
        print('此用户已注册,请换个用户名再试!')
        return
    else:
        if username == '' or password == '':
            print('用户名或密码不能为空')
            return
        if password == confirm_password:
            user_dict[username] = [password, '']
            shop_db.update_user_info(user_dict)
            public.write_log(username, '注册成功')
            print('注册成功，您现在可以登录了!')

        else:
            print('两次输入的密码不一致!')


def login():
    """
    登录
    :return:None
    """
    user_dict = shop_db.get_user_info()
    username = input('用户名:')
    password = input('密码:')
    if username in user_dict and password == user_dict[username][0]:
        USER_INFO['username'] = username
        USER_INFO['card_id'] = user_dict[username][1]
        USER_INFO['is_login'] = True
        public.write_log(username, '登录成功')
        print('登录成功!')
    else:
        if username == '' or password == '':
            print('用户名或密码不能为空!')
        else:
            public.write_log(username, '尝试登录失败，用户名或密码错误')
            print('用户名或密码错误!')


def shopping(goods, numbers):
    """
    购物车，将选中的商品加入购物车
    :param goods:商品名称
    :param numbers: 商品数量
    :return:None
    """
    flag = False
    if SHOPPING_CART:
        for item in SHOPPING_CART:
            if goods[0] == item[0]:
                item[2] += numbers
                item[3] += int(goods[1]) * numbers
                public.write_log(USER_INFO['username'], '两次购买 %s,自动将订单合并' % goods[0])
                flag = True
                break
    if flag:
        return
    shop_cart = [goods[0],
                 goods[1],
                 numbers,
                 int(goods[1]) * numbers]
    SHOPPING_CART.append(shop_cart)
    public.write_log(USER_INFO['username'], '将%d个%s加入购物车' % (shop_cart[2], shop_cart[0]))
    return


def write_shopping_history():
    """
    写购物记录,将购物记录写到文件里
    :return:None
    """
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    shopping_records_dict = shop_db.get_shopping_records()
    if USER_INFO['username'] in shopping_records_dict:
        shopping_records_dict[USER_INFO['username']][current_time] = SHOPPING_CART
    else:
        shopping_records_dict[USER_INFO['username']] = {current_time: SHOPPING_CART}
    shop_db.update_shopping_records(shopping_records_dict)
    public.write_log(USER_INFO['username'], '购物记录写到文件里')


def read_shopping_history():
    """
    读购物记录，将文件里的购物记录读出来
    :return：None
    """
    shopping_records_dict = shop_db.get_shopping_records()
    if USER_INFO['username'] in shopping_records_dict:
        list_key = list(shopping_records_dict[USER_INFO['username']].keys())
        list_key.sort()
        x = PrettyTable(["商品名称", "单价", "数量", "小计"])
        x.align["商品名称"] = "l"
        x.padding_width = 1
        for item in list_key:
            print('时间:', item)
            for shop_records in shopping_records_dict[USER_INFO['username']][item]:
                x.add_row(shop_records)
            print(x)
            x.clear_rows()
        public.write_log(USER_INFO['username'], '查看购物记录!')
    else:
        print('您还没有购物记录!')


def credit_bind():
    """
    绑定银行卡
    :return:
    """
    user_dict = shop_db.get_user_info()
    if not USER_INFO['card_id']:
        card_id = input('请输入要绑定的信用卡号:')
        password = input('请输入信用卡密码：')
        result = common_api.credit_bind(card_id, password)
        if result:
            user_dict[USER_INFO['username']][1] = card_id
            USER_INFO['card_id'] = card_id
            shop_db.update_user_info(user_dict)
            public.write_log(USER_INFO['username'], '绑定信用卡成功,卡号为：%s' % card_id)
            print('绑定信用卡%s成功' % card_id)
        else:
            public.write_log(USER_INFO['username'], '绑定信用卡失败，卡号或密码错误!')
            print('绑定信用卡失败，卡号或密码错误!')
    else:
        print('您已经绑定信用卡,卡号为:%s' % USER_INFO['card_id'])


def checkout(total_amount):
    """
    结账
    :param total_amount:总金额
    :return: True:结账成功，False：结账失败，None：其它
    """
    print('您绑定的信用卡号是：%s' % USER_INFO['card_id'])
    password = input('请输入此信用卡号的密码：')

    result = common_api.checkout(USER_INFO['card_id'], password, total_amount)
    if result['code'] == 0:
        return True
    elif result['code'] == 1 or result['code'] == 2:
        return False
    else:
        return


def shopping_cart():
    """
    购物车，如果不结账，购物车里的信息会保存到文件里，重新登录后程序会读文件。
    :return:None：付款失败
    """
    total_amount = 0
    if SHOPPING_CART:
        x = PrettyTable(["商品名称", "单价", "数量", "小计"])
        x.align["商品名称"] = "l"
        x.padding_width = 1

        for item in SHOPPING_CART:
            total_amount += item[3]
            x.add_row(item)
        print(x)
        print('总计: %d 元' % total_amount)

        confirm_checkout = input('是否要结账？(默认为结账 Y/y N/n):')
        if confirm_checkout == 'Y' or confirm_checkout == 'y' or confirm_checkout == '':
            if not USER_INFO['card_id']:
                print('您还没绑定信用卡，请先张绑定之后再付款!')
                return
            result = checkout(total_amount)
            if result:
                public.write_log(USER_INFO['username'], '结账成功，总共消费%d元' % total_amount)
                print('成功付款,总共消费%d元，欢迎下次光临!' % total_amount)
            else:
                public.write_log(USER_INFO['username'], '付款失败,密码错误或余额不足')
                print('付款失败，密码错误或余额不足')
                return
            write_shopping_history()
            SHOPPING_CART.clear()
            shop_db.update_shopping_cart(USER_INFO['username'], SHOPPING_CART)
            public.write_log(USER_INFO['username'], '清空购物车')
        elif confirm_checkout == 'N' or confirm_checkout == 'n':
            public.write_log(USER_INFO['username'], '取消结账')
            print('取消结账!')
        else:
            print('无效的输入!')
    else:
        print('购物车为空!')


def goods_menu():
    """
    显示购物菜单
    :return:
    """
    goods = goods_list()
    goods_class = list(goods.keys())
    goods_class.sort()

    while True:
        for i, v in enumerate(goods_class, 1):
            print(i, v)

        class_num = input('请选择品类(b/back 返回上一级):')
        if class_num.isdigit():
            class_num = int(class_num)
            if class_num < 0 or class_num > 4:
                print('请输入有效的编号!')
                continue
            else:
                while True:
                    for i, v in enumerate(goods[goods_class[class_num - 1]], 1):
                        print(i, ' '.join(v))
                    goods_num = input('请选择(b/back 返回上一级):')
                    if goods_num.isdigit():
                        goods_num = int(goods_num)
                        if goods_num < 0 or goods_num > 4:
                            print('请输入有效的编号:')
                            continue
                        else:
                            numbers = input('请输入购买的商品数量:')
                            if numbers.isdigit():
                                numbers = int(numbers)
                                shopping(goods[goods_class[class_num - 1]][goods_num - 1], numbers)
                                shop_db.update_shopping_cart(USER_INFO['username'], SHOPPING_CART)
                    elif goods_num == 'b' or goods_num == 'back':
                        break
                    elif goods_num == 'q' or goods_num == 'quit':
                        sys.exit(0)
                    else:
                        print('必须输入编号!')
        elif class_num == 'b' or class_num == 'back':
            break
        elif class_num == 'q' or class_num == 'quit':
            sys.exit(0)
        else:
            print('必须输入编号!')


def main_menu():
    """
    登录后显示的菜单，主要功能有购物，购物记录，购物车（购物车包含结账功能），
    :return: None
    """
    login()
    SHOPPING_CART.extend(shop_db.get_shopping_cart(USER_INFO['username']))
    public.write_log(USER_INFO['username'], '读取购物车信息')
    menu_main = """
        1.购－物       2.购物记录
        3.购物车       4.绑定银行卡
        5.返－回       0.退－出
    """
    while True:
        print(menu_main)
        menu_num = input('请选择:')
        if menu_num.isdigit():
            menu_num = int(menu_num)
            if menu_num == 1:
                goods_menu()
            elif menu_num == 2:
                read_shopping_history()
            elif menu_num == 3:
                shopping_cart()
            elif menu_num == 4:
                credit_bind()
            elif menu_num == 5:
                break
            elif menu_num == 0:
                sys.exit(0)
            else:
                print('请输入有效的编号!')
        else:
            if menu_num == '':
                continue
            else:
                print('只能输入编号!')


def start_menu():
    """
    开始菜单
    :return:None
    """
    menu_start = """
        1.登录    2.注册
        0.退出
    """
    print(menu_start)


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, 'logs')
    public.set_logging(log_dir, 'debug')
    while True:
        start_menu()
        num = input('请选择:')
        if num.isdigit():
            num = int(num)
            if num == 1:
                main_menu()
            elif num == 2:
                register()
            elif num == 0:
                sys.exit(0)
            else:
                print('请选择有效的序号!')
        else:
            if num == '':
                pass
            else:
                print('无效的输入!')


if __name__ == '__main__':
    main()
