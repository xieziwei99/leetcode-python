#### 问题描述

- 确定整数是否是回文。当一个整数向后读取与向前读取的内容相同时，它就是一个回文数。如 121
- 你能在不把整数转换成字符串的情况下解出它吗



#### 解法1

- 若输入 x 是负数，则返回 False
- 若为非负数
  1. 算出 x 的长度 n
  2. 截取左边第一个与右边第一个比较
     1. 若相等，则重复步骤 2，直至左边与右边是同一个数字，或相差 1，此时 return True
     2. 若不等，return False



#### 代码1

``` python
class Solution:

    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = self.how_many_digits(x)
        i, left, right = 0, 0, 0
        while left == right:
            if n - i == i - 1 or n - i == i:	# 左边与右边是同一个数字，或相差1时，停止
                return True
            i += 1
            left = x // 10 ** (n - i)
            left %= 10				# 取得左边第i个
            right = x // 10 ** (i - 1)
            right %= 10				# 取得右边第i个
        return False

    @staticmethod
    def how_many_digits(x: int):
        ret = 0
        while x != 0:
            x //= 10
            ret += 1
        return ret
```



#### 解法2（优于1）

> 参考别人成果所得

- 若输入 x 是负数，或者最后一位是0（0本身除外），则返回 False
- 直接取出 x 的后半段数字并反转
  - 例如 1221
    - 1221 % 10 = 1， 0 * 10 + 1 = **1**， 1221 // 10 = **122**
    - 122 % 10 = 2， 1 * 10 + 2 = **12**（rev）， 122 // 10 = **12**（x）
  - 再例如 12321
    - 12321 % 10 = 1， 0 * 10 + 1 = **1**， 12321 // 10 = **1232**
    - 1232 % 10 = 2， 1 * 10 + 2 = **12**， 1232 // 10 = **123**
    - 123 % 10 = 3， 12 * 10 + 3 = **123**（rev）， 123 // 10 = **12**（x）
- 如何判断截取到了 x 的中间？
  - 显然是当 x <= rev 时停止



#### 代码2

```python
class Solution:

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
```