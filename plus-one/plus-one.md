#### 问题描述

- 给定一个非空的数字数组，表示一个非负整数，让其加上1并返回

- 数组中的每个元素只包含一个数字，数字正序放置

- 可以假设整数不包含任何前导零，除了数字0本身

- 例如：

  ```sh
  Input: [1,2,3]
  Output: [1,2,4]
  Explanation: The array represents the integer 123.
  ```



#### 解题思路1

- 用一个进位描述，有则向前加1



#### 代码1

```python
class Solution:
    
    """
    对传入数组有更改
    """
    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        i = len(digits) - 1
        flag = 1
        while i >= 0 and flag == 1:
            temp = digits[i] + flag
            digits[i] = temp % 10
            i -= 1
            flag = temp // 10
        if i == -1 and flag == 1:
            digits.insert(0, 1)
        return digits
```



