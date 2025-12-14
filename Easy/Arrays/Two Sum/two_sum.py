# https://leetcode.com/problems/two-sum/description/

nums = [2,7,11,15]

target = 9

seen = {}

for i, num in enumerate(nums):
    required = target - num
    if required in seen:
        print([seen[required], i])
        break
    
    seen[num] = i

# Need to work on Runtime