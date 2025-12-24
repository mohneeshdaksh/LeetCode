# https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        running = 0
        for i in nums:
            running += i
            self.prefix.append(running)

    def sumRange(self, left: int, right: int) -> int:
        print(self.prefix)
        total = (self.prefix[right+1]) - self.prefix[left]
        return total

nums = [-2, 0, 3, -5, 2, -1]

range_sum = NumArray(nums)

first_sum = range_sum.sumRange(1, 3)
print(first_sum)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)