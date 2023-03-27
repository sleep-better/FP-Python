# -*- coding: UTF-8 -*-
"""
    @project:FP-Python
    @Author:sleep-better
    @date:2023/3/24 21:59
"""

# Question_URL="https://leetcode.cn/problems/longest-substring-without-repeating-characters/"

from itertools import chain
from util import fst, snd, find
from functools import reduce


# 1
def get_longest_01(s):
    now_consider = ''
    old_longest = ''
    for i in s:
        if i not in now_consider:
            now_consider += i
        else:
            if len(now_consider) > len(old_longest):
                old_longest = now_consider
            now_consider = now_consider[now_consider.index(i) + 1:] + i
    return max(len(now_consider), len(old_longest))


# 2
def filter_func(s):
    return len(s) == len(set(s))


def get_longest_10(s):
    def window(a, b):
        return update_length(create_new(fst(a), b), snd(a))

    def update_length(a, b):
        return a, max(len(a), b)

    def create_new(a, b):
        return a + b if filter_func(a + b) else a[a.index(b) + 1:] + b

    return snd(reduce(window, s, ('', 0)))


# 3
def get_str_by_len(s, length):
    return map(lambda x: s[x:x + length], range(len(s) - length + 1))


def get_str_by_all_len(s):
    return map(lambda x: get_str_by_len(s, x), reversed(range(1, len(s) + 1)))


def get_all_substring(s):
    return chain(*get_str_by_all_len(s))


def get_longest_substring_by_func(func, s):
    return len(find(func, get_all_substring(s)))


def get_longest_20(s):
    return get_longest_substring_by_func(filter_func, s)


if __name__ == '__main__':
    string = 'pwwkew'
    print(get_longest_01(string))
    print(get_longest_10(string))
    print(get_longest_substring_by_func(filter_func, string))
    print(get_longest_20(string))
