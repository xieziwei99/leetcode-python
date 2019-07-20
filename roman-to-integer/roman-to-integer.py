#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 给定一个罗马数字，把它转换成整数。输入保证在1到3999之间。
@author: xieziwei99
@Create Date: 2019/7/20
"""


class Solution:

    def __init__(self):
        self.my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def roman_to_int(self, s: str) -> int:
        ret = 0
        temp = []
        for i in range(len(s)):
            if not temp:  # 若temp为空
                temp.append(s[i])
            else:
                out = temp.pop()
                if out + s[i] in self.my_dict.keys():
                    ret += self.my_dict[out + s[i]]
                else:
                    ret += self.my_dict[out]
                    temp.append(s[i])
        if temp:
            ret += self.my_dict[temp.pop()]
        return ret

    def roman_to_int2(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n - 1):
            if self.my_dict[s[i]] >= self.my_dict[s[i + 1]]:
                ret += self.my_dict[s[i]]
            else:
                ret -= self.my_dict[s[i]]
        ret += self.my_dict[s[-1]]
        return ret


def main():
    print(Solution().roman_to_int('MCMXCIV'))
    print(Solution().roman_to_int2('MCMXCIV'))


if __name__ == '__main__':
    main()
