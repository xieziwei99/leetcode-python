#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 最大子串和问题
@author: xieziwei99
@Create Date: 2019/8/7
"""
from typing import List


class Solution:

    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        if not [i for i in nums if i > 0]:  # 当列表为空时成立，即nums中全都不大于0时
            return max(nums)
        temp = 0
        the_max = nums[0]
        for i in range(len(nums)):
            temp += nums[i]
            if temp <= 0:
                temp = 0
            elif temp > the_max:
                the_max = temp
        return the_max

    def max_sub_array2(self, nums: List[int]) -> int:
        if not [i for i in nums if i > 0]:  # 当列表为空时成立，即nums中全都不大于0时
            return max(nums)
        return self._max_sub_array(nums, 0, len(nums) - 1)

    def _max_sub_array(self, nums: List[int], left, right) -> int:
        if left >= right:
            return nums[left] if nums[left] >= 0 else 0
        mid = (left + right) // 2
        max_left = self._max_sub_array(nums, mid + 1, right)
        max_right = self._max_sub_array(nums, left, mid - 1)
        max_mid_left, max_mid_right, temp = 0, 0, 0
        for i in range(left, mid)[::-1]:  # mid-1, mid-2, ... , left
            temp += nums[i]
            if temp > max_mid_left:
                max_mid_left = temp
        temp = 0
        for i in range(mid, right + 1):  # mid, mid+1, ... , right
            temp += nums[i]
            if temp > max_mid_right:
                max_mid_right = temp
        return max(max_left, max_right, (max_mid_left + max_mid_right))


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution.max_sub_array(nums))
    print(Solution().max_sub_array2(nums))


if __name__ == '__main__':
    main()
