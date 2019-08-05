#### 问题描述

- 给定数组 nums 和值 val，删除该值的所有实例并返回新的长度。
- 不要为另一个数组分配额外的空间，您必须使用O(1)额外内存修改输入数组。
- 元素的顺序可以改变。在新的长度之外留下什么并不重要。



#### 解法1

- 向右遍历，遇到相等的，则将该值所在位置赋为数组最后一个元素



#### 代码1

```python
from typing import List


class Solution:

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
```