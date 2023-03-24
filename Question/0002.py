# -*- coding: UTF-8 -*-
"""
    @project:FP-Python
    @Author:sleep-better
    @date:2023/3/23 22:00
"""

# Question_URL = "https://leetcode.cn/problems/add-two-numbers/"
from functools import reduce

from util import fst, get_value, snd


# 标准命令式
def get_add_two_number_01(lst1, lst2):
    result = []
    carry = 0
    for i in range(max(len(lst1), len(lst2))):
        number1 = lst1[i] if i < len(lst1) else 0
        number2 = lst2[i] if i < len(lst2) else 0
        carry, b = divmod(number1 + number2 + carry, 10)
        result.append(b)
    if carry:
        result.append(carry)
    return result


# 递归
def fst_value(lst):
    return fst(lst) if lst else 0


def get_add_two_number_10(lst1, lst2, carry=0):
    if not lst1 and not lst2:
        if carry == 0:
            return []
        else:
            return [carry]
    x, y = divmod(fst_value(lst1) + fst_value(lst2) + carry, 10)
    return [y] + get_add_two_number_10(lst1[1:], lst2[1:], x)


# 函数式
def get_value_default_0(data, i):
    return get_value(data, i) if i < len(data) else 0


def get_add_two_number_20(lst1, lst2):
    def add_two_number_by_index(lst1, lst2):
        def inner(result, i):
            return reduce(lambda x, y: [fst(result) + [y], x],
                          divmod(get_value_default_0(lst1, i) + get_value_default_0(lst2, i) + snd(result), 10))

        return inner

    return reduce(lambda x, y: x + [y] if y else x,
                  reduce(add_two_number_by_index(lst1, lst2), range(max(len(lst1), len(lst2))), [[], 0]))


if __name__ == '__main__':
    list1 = [9, 9, 9, 9, 9, 9, 9]
    list2 = [9, 9, 9, 9]
    print(get_add_two_number_01(list1, list2))
    print(get_add_two_number_10(list1, list2))
    print(get_add_two_number_20(list1, list2))
