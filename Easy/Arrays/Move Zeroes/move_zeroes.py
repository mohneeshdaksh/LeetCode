# https://leetcode.com/problems/move-zeroes/description/

nums = [0,1,0,3,11]

write_index = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[write_index] = nums[i]
        write_index += 1
while(write_index < len(nums)):
        nums[write_index] = 0
        write_index += 1

print(nums)