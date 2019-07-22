#### 问题描述

- 给定一个已排序的数组号，删除重复项，使每个元素只出现一次，并返回新的长度。
- 不要为另一个数组分配额外的空间，您必须使用O(1)额外内存修改输入数组。
- 注意，输入数组是通过引用传入的，这意味着调用者也知道对输入数组的修改。



#### 解法1

- 向后遍历，相同不处理，不同放前面



#### 代码1

```python
from typing import List


class Solution:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
```