#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    给定一个整数数组，返回两个数字的索引，使它们加起来等于一个特定的目标。
    您可以假设每个输入都只有一个解决方案，并且不能两次使用相同的元素。
@author: xieziwei99
@Create Date: 2019/7/18
"""
from typing import List


class Solution:

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        my_dict = {}
        n = len(nums)
        complement = 0  # 可提升效率
        for i in range(n):
            complement = target - nums[i]
            # 放入keys中，才能取出对应索引
            # 若有相同的值是答案的解，如 2+2=4，则第二个值也不会放入dict.keys()中
            # 考虑[2, 2, 3, 7]，target=5，此种情况会得到[1, 2]
            # 但题目限定只有唯一解，故不多做考虑
            if complement in my_dict.keys():
                return [my_dict[complement], i]
            my_dict[nums[i]] = i


def main():
    my_lists = [
        [2, 7, 11, 15],
        [11, 2, 15, 7],
        [2, 2, 11, 7],  # 此算法下解为[1, 3]，而不是[0, 3]
    ]
    for my_list in my_lists:
        print(Solution.two_sum(my_list, 9))


if __name__ == '__main__':
    main()