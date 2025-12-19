# https://leetcode.com/problems/majority-element/description/

nums = [2,2,1,1,1,2,2]

# nums = [1]

# nums = [3,1,3,2,3,2,3]

# nums = [2,3,3,2,2]

majority_element = nums[0]
max_count = 1

for current_element in nums[1:]:
    if current_element == majority_element:
        max_count += 1
    else:
        max_count -= 1
        if max_count == 0:
            majority_element = current_element
            max_count += 1

print(majority_element)