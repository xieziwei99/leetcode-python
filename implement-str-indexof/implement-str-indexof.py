#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 
@author: xieziwei99
@Create Date: 2019/7/24
"""


class Solution:

    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        i, j = 0, 0
        n1, n2 = len(haystack), len(needle)
        while i < n1 and j < n2:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        return i - j if j >= n2 else -1


def main():
    haystack, needle = "BBCABCDABABCDABCDABDE", "ABCDABD"
    print(Solution.str_str(haystack, needle))


if __name__ == '__main__':
    main()
