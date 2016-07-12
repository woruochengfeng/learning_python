#!/usr/bin/env python3
# Author: Zhangxunan
import re


# 计算乘除的函数
def mul_div(exp):
    """
    计算乘除
    :param exp: 接收一个计算列表值
    :return:计算乘除后的表达式
    """

    val = exp[0]
    res = re.search('\d+\.*\d*[*/]+[+\-]?\d+\.*\d*', val)
    # 如果val中不存在乘除运算符，则return
    if not res:
        return
    content = re.search('\d+\.*\d*[*/]+[+\-]?\d+\.*\d*', val).group()
    # 判断以*为分隔符，如果大于1则表示存在*运算，否则不存在
    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)

    before, after = re.split('\d+\.*\d*[*/]+[+\-]?\d+\.*\d*', val, 1)
    # 将字符串拼接起来
    new_str = "%s%s%s" % (before, value, after)
    exp[0] = new_str
    mul_div(exp)


# 计算加减的函数
def add_sub(exp):
    """
    计算加减
    :param exp: 接收一个列表值
    :return:返回计算后的表达式
    """
    while True:
        if '+-' in exp[0] or '++' in exp[0] or '-+' in exp[0] or '--' in exp[0]:
            exp[0] = exp[0].replace('+-', '-')
            exp[0] = exp[0].replace('++', '+')
            exp[0] = exp[0].replace('-+', '-')
            exp[0] = exp[0].replace('--', '+')
        else:
            break
    if exp[0].startswith('-'):
        exp[1] += 1
        exp[0] = exp[0].replace('-', '&')
        exp[0] = exp[0].replace('+', '-')
        exp[0] = exp[0].replace('&', '+')
        exp[0] = exp[0][1:]
    val = exp[0]

    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    # 如果val中不存在加减运算符，则return
    if not mch:
        return

    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = re.split('\d+\.*\d*[+\-]{1}\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    exp[0] = new_str
    add_sub(exp)


def calculation(exp):
    """
    计算表达式
    :param exp:表达式
    :return: 最终结果
    """
    expression = [exp, 0]
    # 处理乘除函数
    mul_div(expression)
    # 处理加减函数
    add_sub(expression)
    if divmod(expression[1], 2)[1] == 1:
        result = float(expression[0])
        result *= -1
    else:
        result = float(expression[0])
    return result


# 递归去除括号,并返回最终结果
def remove_brackets(exp):
    """
    去括号，用到递归
    :param exp: 表达式
    :return:返回最终结果
    """
    if not re.search('\(([+\-*/]*\d+\.*\d*){2,}\)', exp):
        final_result = calculation(exp)
        return final_result
    brackets = re.search('\(([+\-*/]*\d+\.*\d*){2,}\)', exp).group()

    before, nothing, after = re.split('\(([+\-*/]*\d+\.*\d*){2,}\)', exp, 1)

    # 去掉括号
    brackets = brackets.strip("()")
    print('之前：', exp)
    # 计算加减的函数乘除的函数
    result = calculation(brackets)
    print('%s=%s' % (brackets, result))
    # 将字符串拼接起来
    expression = "%s%s%s" % (before, result, after)
    print('之后：', expression)
    print('*'*40)
    return remove_brackets(expression)


def main():
    # expression = "8*12-(6-(5*6-2)/77+2)*(3-7)+8"
    # 将空格替换成空
    expression = input('请输入表达式:')
    expression = re.sub('\s*', '', expression)
    result = remove_brackets(expression)
    print(result)
    print('eval计算结果:', eval(expression))


if __name__ == "__main__":
    main()
