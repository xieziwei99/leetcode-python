#### 问题描述

- 罗马数字由七种不同的符号表示: I、V、X、L、C、D和M

- ```
  Symbol       Value
  I             1
  V             5
  X             10
  L             50
  C             100
  D             500
  M             1000
  ```

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 

- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 

- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

- 给定一个罗马数字，把它转换成整数。输入保证在1到3999之间。



#### 解法1

1. 将 13 种字面搭配存储起来：

   ``` python
   {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
   ```

2. 构建栈

   1. 每次读取传入字符串的一个字符
   2. 遍历传入字符串 s ，判断栈是否为空
      - 若为空，则直接将字符压入栈，结束此次循环
      - 若不为空，则从栈中弹出一个字符 c，与当前字符 i 组合成 ci（如 ‘IV’ ），判断其是否在字典中
        - 若在字典中，则将 ci 的值加入结果中，结束此次循环
        - 若不在，则将 c 的值加入结果中，将 i 压入栈，结束此次循环
   3. 遍历结束后，若栈不为空，则将栈弹出字符 c，将 c 的值加入结果中
   4. 返回结果



#### 代码1

```python
class Solution:

    def __init__(self):
        self.my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

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
```



#### 解法2

1. 将 7 个 symbol-value 存储
2. 从左至右遍历传入的 s
   1. 若第 i 个比后一个（第 i + 1个）小，则从结果 ret 中减去第 i 个的值 s[i]
   2. 若第 i 个比第 i + 1个大，则 ret += s[i]
3. return



#### 代码2

```python
class Solution:

    def __init__(self):
        self.my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

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
```

