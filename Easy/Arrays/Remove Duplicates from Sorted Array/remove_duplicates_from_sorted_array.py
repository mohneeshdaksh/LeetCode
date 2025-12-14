# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

nums = [0,0,1,1,1,2,2,3,3,4]

# Array is sorted in non-decreasing array
# Need to remove duplicates 
# No. of unique elements is k
# Ruturn k and first k elements of nums unique number in sorted order 

k = 0

for i in range(len(nums)):
    if nums[i] != nums[k]:
        k += 1
        nums[k] = nums[i]

print(k+1)