#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 
@author: xieziwei99
@Create Date: 2019/7/24
"""
from typing import List


class Solution:

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


def main():
    t = [0, 1, 2, 2, 3, 0, 4, 2]
    print(Solution.remove_element(t, 2), t)


if __name__ == '__main__':
    main()
