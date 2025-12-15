# https://leetcode.com/problems/search-insert-position/description/

nums = [1,3,5,6]

target = 5

left_pointer = 0
right_pointer = len(nums) - 1


while True:
    mid = left_pointer + (right_pointer - left_pointer) // 2

    if (right_pointer - left_pointer) == 1 or (left_pointer == right_pointer):
        print("reached the end")
        break
    elif nums[mid] > target:
        right_pointer = mid
    elif nums[mid] < target:
        left_pointer = mid
    elif nums[mid] == target:
        print(nums[mid])
        break
