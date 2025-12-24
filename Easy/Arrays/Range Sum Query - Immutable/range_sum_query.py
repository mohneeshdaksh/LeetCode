# https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum

nums = [-2, 0, 3, -5, 2, -1]

range_sum = NumArray(nums)

first_sum = range_sum.sumRange(0, 3)
print(first_sum)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)