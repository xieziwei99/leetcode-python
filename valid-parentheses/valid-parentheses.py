#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 括号匹配
@author: xieziwei99
@Create Date: 2019/7/21
"""


class Solution:

    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{') or not stack:    # 或栈为空
                stack.append(s[i])
            else:
                temp = stack.pop()
                if temp == '(' and s[i] == ')' or temp == '[' and s[i] == ']' or temp == '{' and s[i] == '}':
                    pass
                else:
                    return False
        return True if not stack else False


def main():
    s = "{[]}"
    print(Solution.is_valid(s))


if __name__ == '__main__':
    main()
