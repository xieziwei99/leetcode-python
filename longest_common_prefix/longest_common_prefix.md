#### 问题描述

- 编写一个函数来查找字符串数组中最长的公共前缀字符串。
- 如果没有公共前缀，返回一个空字符串 “”。
- 假设所有输入字符串都是小写 a-z



#### 解法1

- 很 eazy



#### 代码1

```python
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
```