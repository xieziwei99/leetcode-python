#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    n=1时输出字符串1；
    n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；
    n=3时，由于上次字符是11，有2个1，所以输出21；
    n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。
    依次类推，写个countAndSay(n)函数返回字符串。
@author: xieziwei99
@Create Date: 2019/8/6
"""


class Solution:

    @staticmethod
    def count_and_say(n: int) -> str:
        if n == 1:
            return '1'
        else:
            temp = list(Solution.count_and_say(n - 1))
            temp.reverse()
            old = temp.pop()
            cnt = 1
            ret = ''
            while temp:
                new = temp.pop()
                if new == old:
                    cnt += 1
                else:
                    ret += str(cnt) + old
                    old = new
                    cnt = 1
            ret += str(cnt) + old
            return ret


def main():
    print(Solution.count_and_say(6))


if __name__ == '__main__':
    main()
