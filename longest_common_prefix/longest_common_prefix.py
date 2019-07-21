#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 编写一个函数来查找字符串数组中最长的公共前缀字符串。
@author: xieziwei99
@Create Date: 2019/7/21
"""
from typing import List


class Solution:

    @staticmethod
    def two_common_prefix(x, y):
        n = min(len(x), len(y))
        common = ''
        for i in range(n):
            if x[i] == y[i]:
                common += x[i]
            else:
                break
        return common

    def longest_common_prefix(self, strs: List[str]) -> str:
        if strs:
            common = strs.pop()
        else:
            return ""
        while strs:
            common = self.two_common_prefix(common, strs.pop())
        return common


def main():
    strs = ["flower", "flow", "flight"]
    print(Solution().longest_common_prefix(strs))


if __name__ == '__main__':
    main()
