#### 问题描述

- 括号匹配
- 给定一个只包含字符 '('，')'，'{'，'}'，'[' 和 ']'的字符串，判断输入字符串是否有效。
- 注意，空字符串也被认为是有效的



#### 解法1

- 栈



#### 代码1

```python
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
```

