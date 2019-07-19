#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    确定整数是否是回文。当一个整数向后读取与向前读取的内容相同时，它就是一个回文数。如 121
    你能在不把整数转换成字符串的情况下解出它吗
@author: xieziwei99
@Create Date: 2019/7/19
"""


class Solution:

    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = self.how_many_digits(x)
        i, left, right = 0, 0, 0
        while left == right:
            if n - i == i - 1 or n - i == i:
                return True
            i += 1
            left = x // 10 ** (n - i)
            left %= 10
            right = x // 10 ** (i - 1)
            right %= 10
        return False

    @staticmethod
    def how_many_digits(x: int):
        ret = 0
        while x != 0:
            x //= 10
            ret += 1
        return ret

    # method 2
    @staticmethod
    def is_palindrome2(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


def main():
    print(Solution.is_palindrome2(1221))


if __name__ == '__main__':
    main()
