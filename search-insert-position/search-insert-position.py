#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 给定一个排序好的数组和一个目标值，如果找到目标，返回索引。如果没有，返回按顺序插入的索引所在的位置。
@author: xieziwei99
@Create Date: 2019/8/5
"""
import math
from typing import List


class Solution:

    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        low, high, mid = 0, len(nums) - 1, 0
        while low <= high:
            mid = math.floor((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


def main():
    my_list = [1, 3, 5, 6]
    print(Solution.search_insert(my_list, 5))


if __name__ == '__main__':
    main()
