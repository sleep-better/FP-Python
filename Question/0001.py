# -*- coding: UTF-8 -*-
"""
    @project:FP-Python
    @Author:sleep-better
    @date:2023/3/23 21:20
"""
from itertools import permutations

from util import fst, snd, find


# Question_URL = "https://leetcode.cn/problems/two-sum/"


# 标准命令式
def get_need_index_01(lst, target):
    have_consider = {}
    for i, j in enumerate(lst):
        if (a := have_consider.get(target - j)) is not None:
            return [i, a]
        else:
            have_consider[j] = i


# 生成器、递归
def get_need_index_10(lst, target):
    def get_all_combination(lst):
        if len(lst) == 0:
            return None
        yield from map(lambda x: (x + lst[-1], [lst.index(x), len(lst) - 1]), lst[:-1])
        yield from get_all_combination(lst[:-1])

    return snd(find(lambda x: fst(x) == target, get_all_combination(lst)))


# 随便想想
def get_need_index_by_func(lst, func):
    def get_all_permutation(lst, number):
        yield from map(reshuffle_index_and_value, permutations(enumerate(lst), number))

    def reshuffle_index_and_value(data):
        return map(fst, data), map(snd, data)

    return list(fst(find(lambda x: func(*x[1]), get_all_permutation(lst, func.__code__.co_argcount))))


def get_need_index_20(lst, target):
    def filter_func(target):
        def inner(a, b):
            return a + b == target

        return inner

    return get_need_index_by_func(lst, filter_func(target))


if __name__ == '__main__':
    print(get_need_index_01([2, 7, 11, 15], 9))
    print(get_need_index_10([2, 7, 11, 15], 9))
    print(get_need_index_by_func([2, 7, 11, 15], lambda x, y: x + y == 9))
    print(get_need_index_20([2, 7, 11, 15], 9))
