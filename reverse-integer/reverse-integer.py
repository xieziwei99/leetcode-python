#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    给定一个 32 位带符号整数，使整数顺序变反
    如 123 -> 321
    若反转后的结果超出 32 位带符号整数的范围，则返回 0
@author: xieziwei99
@Create Date: 2019/7/18
"""


class Solution:

    @staticmethod
    def reverse(x: int) -> int:
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        minus = True if x < 0 else False
        x_list = list(str(abs(x)))
        i = len(x_list) - 1
        while 0 == x_list[i]:
            x_list.pop(i)
            i -= 1
        x_list.reverse()
        ret = -int(''.join(x_list)) if minus else int(''.join(x_list))
        return 0 if ret < -2 ** 31 or ret > 2 ** 31 - 1 else ret


def main():
    x = 1534236469
    print(Solution.reverse(x))


if __name__ == '__main__':
    main()
