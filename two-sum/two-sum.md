#### 问题描述

- ​给定一个整数数组，返回两个数字的索引，使它们加起来等于一个特定的目标。
- 您可以假设每个输入都只有一个解决方案，并且不能两次使用相同的元素。



#### 解题思路1

1. 创建一个 my_dict
2. 遍历提供的数组 nums
   - 对第 i 个 num，在 my_dict 中若已存在与其之和为 target 的数，则找到解
   - 若不存在，则将 nums[i] 存入 my_dict.keys() 中，对应值为 i



#### 方法1

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        n = len(nums)
        complement = 0	# 可提高性能
        for i in range(n):
            complement = target - nums[i]
            # 放入keys中，才能取出对应索引
            # 若有相同的值是答案的解，如 2+2=4，则第二个值也不会放入dict.keys()中
            # 考虑[2, 2, 3, 7]，target=5，此种情况会得到[1, 2]
            # 但题目限定只有唯一解，故不多做考虑
            if complement in my_dict.keys():
                return [my_dict[complement], i]
            my_dict[nums[i]] = i
```

