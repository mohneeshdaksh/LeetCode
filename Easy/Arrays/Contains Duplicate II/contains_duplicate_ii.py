# https://leetcode.com/problems/contains-duplicate-ii/description/

nums = [1,1,3,2]
k = 2

# nums = [1,2,3,1,2,3]
# k = 2

last_index = {}

contains_duplicate = False

for i in range(len(nums)):
    if nums[i] in last_index:
        if (i - last_index[nums[i]]) <= k:
            contains_duplicate = True
    last_index[nums[i]] = i
print(contains_duplicate)
