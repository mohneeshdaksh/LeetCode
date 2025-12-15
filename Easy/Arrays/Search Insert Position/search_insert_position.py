# https://leetcode.com/problems/search-insert-position/description/

nums = [0,2,4,6,8]

target = 9

left_pointer = 0
right_pointer = len(nums) - 1

while (left_pointer != right_pointer):
    mid = left_pointer + (right_pointer - left_pointer) // 2

    if nums[mid] > target:
        right_pointer = mid
    elif nums[mid] < target:
        left_pointer = mid + 1
    else:
        left_pointer = mid
        break

if target > nums[left_pointer]:
    print(left_pointer + 1)
else:
    print(left_pointer)


# Older Solution ---
# while True:
#     mid = left_pointer + (right_pointer - left_pointer) // 2

#     if (right_pointer - left_pointer) == 1:
#         if nums[left_pointer] != target and nums[right_pointer] != target:
#             if nums[left_pointer] > target:
#                 print(left_pointer)
#             elif nums[left_pointer] < target and nums[right_pointer] > target:
#                 print(right_pointer)
#             elif nums[right_pointer] < target:
#                 print(right_pointer + 1)
#         elif nums[left_pointer] == target:
#             print(left_pointer)
#         elif nums[right_pointer] == target:
#             print(right_pointer)
#         break
#     elif  (left_pointer == right_pointer):
#         if nums[left_pointer] == target:
#             print(left_pointer)
#         elif nums[left_pointer] < target:
#             print(left_pointer + 1)
#         else:
#             print(left_pointer)
#         break
#     elif nums[mid] > target:
#         right_pointer = mid
#     elif nums[mid] < target:
#         left_pointer = mid
#     elif nums[mid] == target:
#         print(mid)
#         break
