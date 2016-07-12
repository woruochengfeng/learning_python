#!/usr/bin/env python3
# Author: Zhangxunan
import json
import os

from SHOPPING.core import public

# 读配置文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(BASE_DIR, 'conf')
conf_name = os.path.join(CONF_DIR, 'atm.conf')

config = public.get_config(conf_name, 'db')
DB_DIR = os.path.join(BASE_DIR, 'db')
if 'user_db_name' in config:
    user_db_name = os.path.join(DB_DIR, config['user_db_name'])
if 'admin_db_name' in config:
    admin_db_name = os.path.join(DB_DIR, config['admin_db_name'])


def get_user_info(role=2):
    """
    读文件获取用户信息
    :param role:角色，１为管理员，２为普通用户，默认为普通用户
    :return: 用户信息字典
    """
    if role == 1:
        f = open(admin_db_name, 'r')
    elif role == 2:
        f = open(user_db_name, 'r')

    else:
        return
    user_dict = json.load(f)
    f.close()
    return user_dict


def update_user_info(user_dict, role=2):
    """
    更新用户信息到文件
    :param user_dict:更新后的字典
    :param role: 角色
    :return: None
    """
    if role == 1:
        f = open(admin_db_name, 'w')
    elif role == 2:
        f = open(user_db_name, 'w')
    else:
        return
    json.dump(user_dict, f)
    f.close()


