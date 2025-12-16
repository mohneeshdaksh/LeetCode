nums1 = [2]
m = 1
nums2 = []
n = 0


index_nums1 = m - 1
index_nums2 = n - 1
write_index = (m + n) - 1

while (index_nums2 >= 0):
    if index_nums1 > -1 and (nums1[index_nums1] > nums2[index_nums2]):
        nums1[write_index] = nums1[index_nums1]
        index_nums1 -= 1
    else:
        nums1[write_index] = nums2[index_nums2]
        index_nums2 -= 1
    
    write_index -= 1

print(nums1)

# Solution 
# def is_second_array_empty(n):
#     """
#     Returns True if nums2 has no elements (n == 0), otherwise False.
#     """
#     if n == 0:
#         return True
#     else:
#         return False


# def get_last_valid_index_nums1(m):
#     """
#     Returns the index of the last real element in nums1 (m - 1).
#     """
#     return (m - 1)


# def get_last_valid_index_nums2(n):
#     """
#     Returns the index of the last element in nums2 (n - 1).
#     """
#     return (n - 1)


# def get_write_index(m, n):
#     """
#     Returns the index of the last position in nums1 (m + n - 1),
#     where we will write the next largest element.
#     """
#     return ((m + n) - 1)


# def should_continue_merging(index_nums2):
#     """
#     Returns True if there are still elements left in nums2 to merge.
#     We stop only when nums2 is fully placed into nums1.
#     """
#     if index_nums2 > -1:
#         return True
#     else:
#         return False


# def should_take_from_first_array(nums1, index_nums1, nums2, index_nums2):
#     """
#     Returns True if we should place nums1[index_nums1] into nums1[write_index].
#     Conceptually:
#     - If nums1 still has elements left AND nums1[index_nums1] is bigger than nums2[index_nums2],
#       then take from nums1.
#     - Otherwise take from nums2.
#     """
#     if index_nums1 >= 0 and (nums1[index_nums1] > nums2[index_nums2]):
#         return True
#     else:
#         False


# def place_value_from_nums1(nums1, index_nums1, write_index):
#     """
#     Places nums1[index_nums1] into nums1[write_index].
#     """
#     nums1[write_index] = nums1[index_nums1]
#     return (nums1[write_index])


# def place_value_from_nums2(nums1, nums2, index_nums2, write_index):
#     """
#     Places nums2[index_nums2] into nums1[write_index].
#     """
#     nums1[write_index] = nums2[index_nums2]
#     return (nums1[write_index])

# def move_left(index):
#     """
#     Moves an index one step left (index - 1) and returns it.
#     """
#     return (index - 1)


# def merge(nums1, m, nums2, n):
#     """
#     Merges nums2 into nums1 in-place so that nums1 becomes a sorted array.
#     """

#     # If nums2 has no elements, nums1 is already correct
#     if is_second_array_empty(n):
#         return

#     # Set up pointers for merging from the back
#     index_nums1 = get_last_valid_index_nums1(m)
#     index_nums2 = get_last_valid_index_nums2(n)
#     write_index = get_write_index(m, n)

#     # Keep placing elements until nums2 is fully merged
#     while should_continue_merging(index_nums2):

#         # Decide whether to take from nums1 or nums2
#         take_from_nums1 = should_take_from_first_array(nums1, index_nums1, nums2, index_nums2)
#         if take_from_nums1:
#             # Place the chosen element into nums1[write_index]
#             place_value_from_nums1(nums1, index_nums1, write_index)
#             index_nums1 = move_left(index_nums1)
#         else:
#             # Place the chosen element into nums1[write_index]
#             place_value_from_nums2(nums1, nums2, index_nums2, write_index)
#             index_nums2 = move_left(index_nums2)

#         # Move the write position left after placing an element
#         write_index = move_left(write_index)
    
#     print(nums1)

# merge(nums1, m, nums2, n)