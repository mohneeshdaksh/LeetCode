# https://leetcode.com/problems/single-number/description/

nums = [4,2,1,1,8,2,4]

answer = 0

for i in nums:
    answer ^= i

print(answer)