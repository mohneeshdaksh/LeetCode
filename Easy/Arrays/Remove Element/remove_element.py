# https://leetcode.com/problems/remove-element/description

# Here we need to remove val -> 2s (if any) from nums
# Replace only when index value and val are the same 

nums = []

val = 2


k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

print(k)