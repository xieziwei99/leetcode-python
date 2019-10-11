问题描述

- 给定两个非空的字符串代表两个二进制数，求他们的和，结果仍是二进制字符串



解法1

- 按照纸上的加法方法进行即可：从个位开始相加，有进位则进位

代码1

```python
class Solution:
    @staticmethod
    def add_binary(a: str, b: str) -> str:
        ret = ''
        carry_bit = 0
        # 调整使得a，b长度相同
        na, nb = len(a), len(b)
        if na < nb:
            a = '0' * (nb - na) + a
        elif na > nb:
            b = '0' * (na - nb) + b
        assert len(a) == len(b)
        i = len(a) - 1
        while i >= 0:
            temp = int(a[i]) + int(b[i]) + carry_bit
            carry_bit = temp // 2
            ret = str(temp % 2) + ret
            i -= 1
        return ret if carry_bit == 0 else str(carry_bit) + ret
```



解法2

- 将二进制数直接转为十进制，相加再转为二进制字符串返回

代码2

```python
class Solution:
    @staticmethod
    def add_binary1(a: str, b: str) -> str:
        num_a, num_b = int(a, 2), int(b, 2)
        ret = num_a + num_b
        return bin(ret)[2:]
```

