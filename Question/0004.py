# -*- coding: UTF-8 -*-
"""
    @project:FP-Python
    @Author:sleep-better
    @date:2023/5/15 23:29
"""

# Question_URL = "https://leetcode.cn/problems/median-of-two-sorted-arrays/"

import statistics
from itertools import chain


def find_median_sorted_arrays_01(nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)
    if length % 2 != 0:
        return nums[len(nums) // 2]
    else:
        return (nums[length // 2] + nums[length // 2 + 1]) / 2


def find_median_sorted_arrays_02(*args):
    return statistics.median(chain(*args))


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(find_median_sorted_arrays_01(nums1, nums2))
    print(find_median_sorted_arrays_02(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrays_01(nums1, nums2))
    print(find_median_sorted_arrays_02(nums1, nums2))
