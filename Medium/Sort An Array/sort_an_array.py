
from typing import List

nums = [5,2,3,1]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            combined_arr = []
            p1, p2 = 0,0
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    combined_arr.append(arr1[p1])
                    p1 += 1
                else:
                    combined_arr.append(arr2[p2])
                    p2 += 1
            combined_arr += arr1[p1:]
            combined_arr += arr2[p2:]
            return combined_arr
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            else:
                mid = len(arr) // 2
                first_half = arr[:mid]
                second_half = arr[mid:]

                sorted_left = merge_sort(first_half)
                sorted_right = merge_sort(second_half)

            return merge(sorted_left, sorted_right)
        
        return merge_sort(nums)
    
if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    sol = Solution()
    print(sol.sortArray(nums))