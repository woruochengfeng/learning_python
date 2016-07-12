#!/usr/bin/env python3
# Author: Zhangxunan
import sys
import os
import json
import time


def menu_start():
    """
    显示开始菜单
    :return: None
    """
    start_menu = '''
        1.获取ha记录    2.增加ha记录
        3.删除ha记录
    '''
    print(start_menu)


def file_rename():
    """
    将老的配置文件名字，改为老文件名字＋修改时间
    将新的配置文件名字，改为正式的配置文件名
    :return:　None
    """
    ctime = time.strftime('%Y_%m_%d_%H_%M_%S')
    old_file_name = 'HAProxy.conf' + '_' + ctime
    new_file_name = 'HAProxy.conf.new'
    os.rename('HAProxy.conf', old_file_name)
    os.rename(new_file_name, 'HAProxy.conf')


def get_backend_dict():
    """
    获取backend和记录并存到字典里
    :return: dict 返回一个字典
    """
    backend_dict = {}
    with open('HAProxy.conf', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('backend'):
                key = line.split()[1]
                backend_dict[key] = []
            if line.startswith('server'):
                backend_dict[key].append(line)
    return backend_dict


def updated_backend_show(record_title):
    """
    显示添加或删除记录之后的节点和记录信息
    :return: None
    """
    updated_backend_dict = get_backend_dict()
    print('backend %s' % record_title)
    for record in updated_backend_dict[record_title]:
        print('\t%s' % record)
    print('\n')

def get_backend_record():
    """
    获取backend记录，并显示！
    :return: None
    """
    while True:
        backend = input('请输入backend(b/back 返回　q/quit 退出):')
        backend_dict = get_backend_dict()
        if backend in backend_dict:
            print('backend', backend)
            for record in backend_dict[backend]:
                print('\t%s' %record)
            print('\n')
        elif backend == 'q' or backend == 'quit':
            sys.exit(0)
        elif backend == 'b' or backend == 'back':
            break
        else:
            print('\033[31m您输入的backend不存在,请重新输入!\n\033[0m')


def add_backend_record():
    """
    增加一条backend记录，如果用户输入的backend是否在配置文件里面存在，如果存在，则在这个backend下面添加一条记录，
    不存在则添加bakcend节点和记录.
    :return: None
    """
    while True:
        record = input('请输入要新加的记录(返回:b/back　退出:q/quit  帮助:h/help):')
        try:
            record_dict = json.loads(record)
        except:
            if record == 'q' or record == 'quit':
                sys.exit(0)
            elif record == 'b' or record == 'back':
                break
            elif record == 'h' or record == 'help':
                print('\033[34m格式:{"backend":"www.oldboy.org","record":{"server":"192.168.1.243","weight": 20,"maxconn": 30}}\033[0m')
                continue
            else:
                print('\033[31m格式不正确，请参照帮助信息!\n\033[0m')
                continue

        if 'backend' not in record_dict or 'record' not in record_dict:
            print('\033[31m输入格式不正确，请查看帮助信息!\n\033[0m')
            continue
        if 'server' not in record_dict['record'] or 'weight' not in record_dict['record'] or 'maxconn' not in \
                record_dict['record']:
            print('\033[31m输入格式不正确，请查看帮助信息!\n\033[0m')
            continue
        #拼接一条server记录
        record_str = '\t' + 'server' + ' ' + record_dict['record']['server'] + ' ' + record_dict['record']['server'] + \
                     ' ' + 'weight' + ' ' + str(record_dict['record']['weight']) + ' ' + 'maxconn' + ' ' + \
                     str(record_dict['record']['maxconn']) + '\n'
        record_title = record_dict['backend']
        #获取所有backend和所有记录
        backend_dict = get_backend_dict()
        server_exist = False
        # 判断如果用户输入的backend是否在配置文件里面存在，如果存在，则在这个backend下面添加一条记录，不存在则添加bakcend节点和记录
        if record_title in backend_dict:
            records = backend_dict[record_title]
            for r in records:
                if record_dict['record']['server'] in r:
                    print('\033[31m server已经存在,不要重复增加!\033[0m')
                    server_exist = True
            if server_exist:
                continue
            with open('HAProxy.conf','r') as f1,open('HAProxy.conf.new','w') as f2:
                for line in f1:
                    f2.write(line)
                    if line.startswith('backend'):
                        if line.split()[1] == record_title:
                            f2.write(record_str)
        else:
            with open('HAProxy.conf','r') as f1,open('HAProxy.conf.new','w') as f2:
                for line in f1:
                    f2.write(line)
                backend_str = 'backend' + ' ' + record_title + '\n'
                f2.write('\n')
                f2.write(backend_str)
                f2.write(record_str)
        #将旧的配置文件改为文件名+修改时间，将新配置文件名改成正式的配置文件的名字
        file_rename()
        print('\033[32m增加记录成功!\n\033[0m')
        #显示更新后的backend节点和记录.
        updated_backend_show(record_title)


def del_backend_record():
    """
    删除一条backend记录,如果backend下所有的记录都已经被删除，那么将当前 backend也删除掉.
    :return: None
    """
    while True:
        record = input('请输入要删除的记录(返回:b/back　退出:q/quit  帮助:h/help):')
        try:
            record_dict = json.loads(record)
        except:
            if record == 'q' or record == 'quit':
                sys.exit(0)
            elif record == 'b' or record == 'back':
                break
            elif record == 'h' or record == 'help':
                print('\033[34m格式:{"backend":"www.oldboy.org","record":{"server":"192.168.1.243","weight": 20,"maxconn": 30}}\033[0m')
                continue
            else:
                print('\033[31m格式不正确,请查看帮助信息!\033[0m')
                continue

        if 'backend' not in record_dict or 'record' not in record_dict:
            print('\033[31m输入格式不正确，请查看帮助信息!\n\033[0m')
            continue
        if 'server' not in record_dict['record'] or 'weight' not in record_dict['record'] or 'maxconn' not in \
                record_dict['record']:
            print('\033[31m输入格式不正确，请查看帮助信息!\n\033[0m')
            continue
        #获取用户输入的backend域名
        record_title = record_dict['backend']
        #获取配置文件有里所有的bakcend及下面的所有记录。
        backend_dict = get_backend_dict()
        #拼接一个记录
        record_str = 'server'+' ' + record_dict['record']['server'] + ' ' + record_dict['record']['server'] + \
                     ' ' + 'weight' + ' ' + str(record_dict['record']['weight']) + ' ' + 'maxconn' + ' ' + \
                     str(record_dict['record']['maxconn'])
#        print('record_str = ',record_str)
        record_exist = False
        #判断要删除的记录是否在配置文件里，如果存在则将字典里的那条记录删除，用计算列表的长度可判断每个backend下的记录是否都已经被删除
        if record_title in backend_dict:
            for item in backend_dict[record_title]:
                if item == record_str:
                    backend_dict[record_title].remove(item)
                    record_exist = True
            with open('HAProxy.conf','r') as f1,open('HAProxy.conf.new','w') as f2:
                for line in f1:
                    line_no_blank = line.strip()
                    #判断每个backend节点下面的记录是否都被删除，如果都删除掉，则backend节点也删除掉.
                    if len(backend_dict[record_title]) == 0:
                        if line.startswith('backend'):
                            if line.split()[1] == record_title:
                                continue
                        if line_no_blank.startswith('server'):
                            if line_no_blank == record_str:
                                continue
                    else:
                        if line_no_blank.startswith('server'):
                            if line_no_blank == record_str:
                                continue
                    f2.write(line)

            #修改文件名字.
            file_rename()
            if record_exist:
                print('\033[32m删除记录成功!\033[0m')
            else:
                print('\033[31m此记录不存在!\033[0m')

            # 显示更新后的backend节点和记录.
            backend_dict = get_backend_dict()
            if record_title in backend_dict:
                updated_backend_show(record_title)
            else:
                print('此节点和记录已经删除!')
        else:
            print('\033[31m您要删除的节点[backend]不存在,请检查是否有误!\033[0m')


def main():
    while True:
        menu_start()
        num = input('请输入操作序号(q/quit 退出):')
        if num.isdigit():
            num = int(num)
            if num == 1:
                get_backend_record()
            elif num == 2:
                add_backend_record()
            elif num == 3:
                del_backend_record()
            else:
                print("\033[31m请输入正确的序号!\033[0m")
        elif num == 'q' or num == 'quit':
            sys.exit(0)
        else:
            print("\033[31m故意的是吧!!!!\033[0m")

main()