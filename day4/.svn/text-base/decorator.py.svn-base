#!/usr/bin/env python3
# Author: Zhangxunan
import sys
from prettytable import PrettyTable


USER_INFO = {'is_login': False}


# 装饰器，判断是否登录
def is_login(func):
    """
    装饰器，在使用功能之前判断用户是否登录，没登录是不能使用某些功能的
    :param func: 使用装饰器的函数的函数名
    :return: 将新的函数名传回去赋值给使用装饰器的函数
    """
    def inner(*args, **kwargs):
        if USER_INFO['is_login']:
            return func(*args, **kwargs)
        else:
            print('\033[31m您还未登录，请登录！\033[0m')
    return inner


# 装饰器，判断用户是否是管理员
def is_manager(func):
    """
    装饰器，在使用某些功能之前判断用户是否为管理员，非管理员不能使用
    :param func: 使用装饰器的函数的函数名
    :return: 将新的函数名传回去赋值给使用装饰器的函数
    """
    def inner(*args, **kwargs):
        if USER_INFO['role'] == '1':
            return func(*args, **kwargs)
        else:
            print('\033[31m您不是管理员，没有权限使用这些功能，抱歉!\033[0m')
    return inner


# 开始菜单
def start_menu():
    """
    开始菜单，程序刚开始运行的时候会显示这个菜单
    :return: None
    """
    menu_start = '''
        1.登－－录       2.注册
        3.修改密码       4.个人信息
        5.后台管理       0.退出
    '''
    print(menu_start)


# 后台管理菜单，只有管理员才能查看此菜单
def manager_menu():
    """
    后台管理菜单，只有管理员才能查看此菜单
    :return: None
    """
    menu_manager = '''
        1.添加用户      2.删除用户
        3.提升权限      4.修改用户密码(ANY)
        5.搜－－索      6.显示用户信息(ALL)
        0.返－－回
    '''
    print(menu_manager)


# 获取用户信息
def get_user_info():
    """
    将所有用户信息从文件读出来，然后存到字典里,字典的格式:{username:[password,email,phone,role]}
    :return: user_dict  返回存有所有用户信息的字典
    """
    user_dict = {}
    with open('user.db', 'r') as f:
        for user in f:
            user = user.strip()
            user = user.split('|')
            user_dict[user[0]] = user[1:]
    return user_dict


# 更新用户信息
def update_user_info(user_dict):
    """
    更新用户信息，将更新后的字典，比如添加用户，先将用户添加到字典里，然后把更新后的字典写到文件里
    :param user_dict: 更新后的字典
    :return: None
    """
    users = []
    # 没什么大作用，就是将字典的key排一下序
    for user in user_dict:
        users.append(user)
    users.sort()
    # 将更新后的字典写到文件里
    with open('user.db', 'w') as f:
        for user in users:
            user_dict[user][3] = str(user_dict[user][3])
            user_str = '%s|%s\n' % (user, '|'.join(user_dict[user]))
            f.write(user_str)


# 注册
def register():
    """
    新用户注册，接收用户输入，将输入的用户信息存到get_user_info获取的字典里，然后再通过update_user_info函数更新文件
    :return: None
    """
    # 获取所有用户信息
    user_dict = get_user_info()
    print('注册:')
    # 接收用户输入
    username = ''
    while not username:
        username = input('用户名:').strip()
        if username == '':
            print('\033[31m用户名不能为空!\033[0m')
        elif username in user_dict:
            print('\033[31m此用户名已经注册!\033[0m')
            username = ''
    while True:
        email = input('邮箱:').strip()
        if email == '' or '@' not in email:
            print('\033[31m不能为空或者格式不正确！格式：用户名@主机名\033[0m')
            continue
        break
    while True:
        phone = input('手机:').strip()
        if phone == '' or not phone.isdigit() or len(phone) != 11:
            print('\033[31m不能为空，并且必须输入11位数字!\033[0m')
            continue
        break
    while True:
        password = input('密码:')
        confirm_password = input('再输一次密码:')
        if password == '' or confirm_password == '':
            print('密码不能为空!')
            continue
        break

    if password == confirm_password:
        # 将输入用户信息存到字典里
        user = [password, email, phone, 2]
        user_dict[username] = user
        # 更新用户信息
        update_user_info(user_dict)
        print('\033[32m注册成功!\033[0m')


# 登录
def login():
    """
    用户登录，get_user_info()从文件里获取所有用户信息，然后判断用户输入用户名是否存在字典里，并且判断密码是否正确。
    最后登录成功后将用户信息存到全局变量USER_INFO字典里
    :return: None
    """
    user_dict = get_user_info()
    counter = 3
    print('用户登录')
    while True:
        if counter == 0:
            break
        username = input('用户名:').strip()
        password = input('密码:')
        if username in user_dict and password == user_dict[username][0]:
            print('\033[32m登录成功，欢迎！\033[0m')
            USER_INFO['username'] = username
            USER_INFO['email'] = user_dict[username][1]
            USER_INFO['phone'] = user_dict[username][2]
            USER_INFO['role'] = user_dict[username][3]
            USER_INFO['is_login'] = True
            break
        else:
            print('\033[31m用户名或密码错误!\033[0m')
        counter -= 1


@is_login
def changepwd_oneself():
    """
    更改自己密码，管理员，普通用户都能通过此函数更改自己密码,此功能只能是登录后使用
    :return: None
    """
    user_dict = get_user_info()
    counter = 3
    while True:
        # 最多出错三次，counter=0的时候退出循环.
        if counter == 0:
            break
        # 判断用户登录后保存在全局变量名是否存在存所有用户信息的字典中。
        if USER_INFO['username'] in user_dict:
            old_password = input('旧的密码:')
            new_password = input('新密码:')
            confirm_password = input('再次输入新密码:')
            if old_password == '':
                print('\033[31m旧的密码不能为空!\033[0m')
                counter -= 1
                continue
            # 如果新密码为空的话会设置默认密码。
            if new_password == '' or confirm_password == '':
                new_password = '123456'
                confirm_password = '123456'
                print('\033[33m您输入的密码为空，已经设置为默认密码!\033[0m')

            # 如果输入的旧密码和文件里存的密码相同，并且两次输入的新密码一致，就更新密码
            if old_password == user_dict[USER_INFO['username']][0] and new_password == confirm_password:
                user_dict[USER_INFO['username']][0] = new_password
                update_user_info(user_dict)
                print('\033[32m密码修改成功!\033[0m')
                break
            else:
                print('\033[31m旧密码错误或两次输入的新密码不一致!\033[0m')
        else:
            print('\033[31m不存在此用户!\033[0m')
        counter -= 1


@is_login
@is_manager
def changepwd():
    """
    只有管理员才能使用此功能，可修改任一用户的密码
    :param:None
    :return: None
    """
    user_dict = get_user_info()
    username = input('请输入要修改密码的用户名:')
    if username in user_dict:
        new_password = input('新密码:')
        confirm_password = input('再次输入新密码:')
        # 如果两次输入的密码都为空,则将用户密码设置为'123456'
        if new_password == '' and confirm_password == '':
            new_password = '123456'
            confirm_password = '123456'
            print('\033[33m已经将用户的密码设置为默认密码!\033[0m')
        if new_password == confirm_password:
            user_dict[username][0] = new_password
            update_user_info(user_dict)
            print('\033[32m密码修改成功!\033[0m')
        else:
            print('\033[31m两次输入的密码不一致,更改密码失败!\033[0m')
    else:
        if username == '':
            print('\033[32用户名不能为空!\033[0m')
        else:
            print('\033[32m此用户不存在!\033[0m')


@is_login
def show_info():
    """
    显示个人信息，只有登录后才可以使用此功能.显示个人信息是不显示密码的。
    :return: None
    """
    # 使用了prettytable模块，使显示更好看
    x = PrettyTable(["姓名", "邮箱", "手机号码", "角色"])
    x.align["姓名"] = "l"
    x.padding_width = 1
    user_dict = get_user_info()
    # 判断登录用户是否存在在用户信息字典里
    if USER_INFO['username'] in user_dict:
        # 将密码从列表里pop掉
        user_dict[USER_INFO['username']].pop(0)
        # 将用户名插入到列表的第一个元素
        user_dict[USER_INFO['username']].insert(0, USER_INFO['username'])
        # 将代表管理员，普通用户的数字替换为汉字
        if user_dict[USER_INFO['username']][3] == '1':
            user_dict[USER_INFO['username']][3] = '管理员'
        else:
            user_dict[USER_INFO['username']][3] = '普通用户'
        x.add_row(user_dict[USER_INFO['username']])
        print(x)


@is_login
@is_manager
def show_info_all():
    """
    显示所有用户信息，此功能只有登录后，并且是管理员才能使用。
    :return: None
    """
    x = PrettyTable(["姓名", "密码", "邮箱", "手机号码", "角色"])
    x.align["姓名"] = "l"
    x.padding_width = 1
    user_dict = get_user_info()
    users = []
    for user in user_dict:
        users.append(user)
    users.sort()
    for user in users:
        # 将用户名插入到列表的第一个元素
        user_dict[user].insert(0, user)
        # 密码用6个*代替
        user_dict[user][1] = '*'*6
        if user_dict[user][4] == '1':
            user_dict[user][4] = '管理员'
        else:
            user_dict[user][4] = '普通用户'
        x.add_row(user_dict[user])
    print(x)


@is_manager
def search():
    """
    搜索功能，只有管理员才能使用此功能
    :return: None
    """
    users = []
    # 输入关键字
    keyword = input('搜索:')
    with open('user.db', 'r') as f:
        for line in f:
            # 判断用户输入的关键字是否在每一行中，如果存在则将这一行存到列表里
            if keyword in line:
                line = line.strip()
                user = line.split('|')
                user[1] = '*'*6
                if user[4] == '1':
                    user[4] = '管理员'
                elif user[4] == '2':
                    user[4] = '普通用户'
                else:
                    user[4] = '未知'
                # 将小列表存到大列表里
                users.append(user)
    if len(users) == 0:
        print('\033[33m未找到相关信息!\033[0m')
    else:
        x = PrettyTable(["姓名", '密码', "邮箱", "手机号码", "角色"])
        x.align["姓名"] = "l"
        x.padding_width = 1
        for user in users:
            x.add_row(user)
        print(x)


@is_manager
def user_add():
    """
    添加用户，此功能只能是管理员使用。
    :return:None
    """
    user_dict = get_user_info()
    username = ''
    while not username:
        username = input('用户名:').strip()
        if username in user_dict:
            print('\033[31m此用户已存在!\033[0m')
            username = ''
        elif username == '':
            print('\033[31m用户名不能为空!\033[0m')
        else:
            pass
    while True:
        email = input('邮箱:')
        if email == '':
            print('\033[31m邮箱不能为空!\033[0m')
        elif '@' not in email:
            print('\033[31m邮箱格式不正确!邮箱格式:用户名@主机名\033[0m')
        else:
            break
    while True:
        phone = input('手机号码:')
        if phone.isdigit() and len(phone) == 11:
            break
        elif phone == '':
            print('\033[31m手机号吗不能为空!\033[0m')
        else:
            print('\033[31m请输入11位的手机号码!\03[0m')
    while True:
        role = input('角色(管理员:1 普通用户:2):')
        if role.isdigit() and (role == '1' or role == '2'):
            break
        elif role == '':
            print('\033[31m必须指定一个角色!\033[0m')
        else:
            print('\033[31m必须是1或2,其它的无效!\033[0m')
    while True:
        password = input('密码:')
        confirm_password = input('再输入一次密码:')
        if password == '' and confirm_password == '':
            password = '123456'
            confirm_password = '123456'
            break
        elif password == confirm_password:
            user_dict[username] = [password, email, phone, role]
            update_user_info(user_dict)
            print('\033[32m添加用户成功!\033[0m')
            break
        else:
            print('\033[31m两次输入的密码不一致\033[0m')


@is_manager
def user_del():
    """
    删除用户，此功能只能是管理员使用
    :return: None
    """
    user_dict = get_user_info()
    username = input('请输入要删除的用户名:')
    if username in user_dict and username != 'admin':
        confirm_choice = input('确定要删除？默认为Y (Y/y or N/n):')
        if confirm_choice == 'Y' or confirm_choice == 'y' or confirm_choice == '':
            user_dict.pop(username)
            update_user_info(user_dict)
            print('\033[32m删除用户成功!\033[0m')
        elif confirm_choice == 'N' or confirm_choice == 'n':
            print('取消删除此用户!')
        else:
            print('\033[31m你想闹哪样?\033[0m')
    else:
        if username == 'admin':
            print('\033[31madmin管理员不能删除!\033[0m')
        else:
            print('\033[31m此用户不存在!\033[0m')


@is_manager
def elevation_of_privilege():
    """
    提权，降权，管理员可将普通用户提升为管理员，也可将管理员将为普通用户。
    :return: None
    """
    user_dict = get_user_info()
    username = input('请输入要提权/降权的用户:')
    role = input('请输入数字(管理员:1 普通用户:2):')
    if username in user_dict:
        if role.isdigit():
            if role == '1':
                user_dict[username][3] = role
                update_user_info(user_dict)
                print('\033[32m已经将%s提升为管理员!\033[0m' % username)
            elif role == '2':
                user_dict[username][3] = role
                update_user_info(user_dict)
                print('\033[32m已经将%s降为普通用户!\033[0m' % username)
            else:
                print('\033[31m无效的数字,更改权限失败!\033[0m')
        else:
            if username == '':
                print('\033[31m请输入一个用户名!\033[0m')
            else:
                print('\033[31m不存在此用户!\033[0m')

    else:
        print('\033[31m此用户不存在!\033[0m')


@is_login
@is_manager
def manager():
    """
    后台管理菜单，只有管理能进入后台管理菜单。
    :return: None
    """
    while True:
        manager_menu()
        num = input('请输入菜单编号:')
        if num.isdigit():
            num = int(num)
            if num == 1:
                user_add()
            elif num == 2:
                user_del()
            elif num == 3:
                elevation_of_privilege()
            elif num == 4:
                changepwd()
            elif num == 5:
                search()
            elif num == 6:
                show_info_all()
            elif num == 0:
                break
            else:
                print('\033[31m请输入正确的编号!\033[0m')
        else:
            if num == '':
                pass
            else:
                print('\033[31m只能输入编号!\033[0m')


def main():
    """
    主函数，程序入口，显示开始菜单，并等待用户选择。
    :return: None
    """
    while True:
        start_menu()
        num = input('请输入菜单编号:')
        if num.isdigit():
            num = int(num)
            if num == 1:
                if USER_INFO['is_login']:
                    print('\033[31m您已经登录!\033[0m')
                else:
                    login()
            elif num == 2:
                register()
            elif num == 3:
                changepwd_oneself()
            elif num == 4:
                show_info()
            elif num == 5:
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


main()
