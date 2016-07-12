#!/usr/bin/env python3
# Author: Zhangxunan

import json
import os

from SHOPPING.core import public

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(BASE_DIR, 'conf')
conf_name = os.path.join(CONF_DIR, 'shopping.conf')

config = public.get_config(conf_name, 'db')
DB_DIR = os.path.join(BASE_DIR, 'db')
if 'user_db_name' in config:
    user_db_name = os.path.join(DB_DIR, config['user_db_name'])
if 'shopping_records' in config:
    shopping_records = os.path.join(DB_DIR, config['shopping_records'])
if 'shopping_cart' in config:
    shopping_cart = os.path.join(DB_DIR, config['shopping_cart'])


def get_user_info():
    """
    获取商城用户信息
    :return: user_dict用户信息字典
    """
    with open(user_db_name, 'r') as f:
        user_dict = json.load(f)
    return user_dict


def update_user_info(user_dict):
    """
    更新用户信息
    :return: None
    """
    with open(user_db_name, 'w') as f:
        json.dump(user_dict, f)


def get_shopping_records():
    """
    获取购物历史记录
    :return:
    """
    with open(shopping_records, 'r') as f:
        shopping_records_dict = json.load(f)
    return shopping_records_dict


def update_shopping_records(shopping_records_dict):
    """
    更新购物历史记录
    :return: None
    """
    with open(shopping_records, 'w')as f:
        json.dump(shopping_records_dict, f)


def get_shopping_cart(username):
    """
    获取用户的购物车，如果用户把商品加到购物车之后没有付款，购物车的信息会存到文件里
    :param username:用户名
    :return: 购物车列表
    """
    with open(shopping_cart, 'r') as f:
        shopping_cart_dict = json.load(f)
        if username in shopping_cart_dict:
            return shopping_cart_dict[username]
        else:
            return []


def update_shopping_cart(username, shopping_cart_list):
    """
    更新购物车信息
    :param username:用户名
    :param shopping_cart_list:　购物车列表
    :return: None
    """
    with open(shopping_cart, 'r') as f:
        shopping_cart_dict = json.load(f)

    with open(shopping_cart, 'w') as f:
        shopping_cart_dict[username] = shopping_cart_list
        json.dump(shopping_cart_dict, f)
