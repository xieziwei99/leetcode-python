#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 给定一个非空的数字数组，表示一个非负整数，让其加上1并返回
    Input: [1,2,3]
    Output: [1,2,4]
@author: xieziwei99
@Create Date: 2019/8/9
"""
from typing import List


class Solution:

    """
    对传入数组有更改
    """
    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        i = len(digits) - 1
        flag = 1
        while i >= 0 and flag == 1:
            temp = digits[i] + flag
            digits[i] = temp % 10
            i -= 1
            flag = temp // 10
        if i == -1 and flag == 1:
            digits.insert(0, 1)
        return digits


def main():
    print(Solution.plus_one([9, 9, 9]))


if __name__ == '__main__':
    main()
