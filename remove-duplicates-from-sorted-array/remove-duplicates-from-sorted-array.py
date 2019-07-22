#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 给定一个已排序的数组号，删除重复项，使每个元素只出现一次，并返回新的长度。
@author: xieziwei99
@Create Date: 2019/7/22
"""
from typing import List


class Solution:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


def main():
    my_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution.remove_duplicates(my_list), my_list)


if __name__ == '__main__':
    main()
