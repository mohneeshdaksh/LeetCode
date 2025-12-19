# https://leetcode.com/problems/contains-duplicate/description/

nums = [1,2,4,3]

# nums = [1,2,3]

seen = set()

contains_duplicate = False

for i in nums:
    if i not in seen:
        seen.add(i)
    else:
        contains_duplicate = True

print(contains_duplicate)