# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# c
# c at
# a - a t
# l != t
# a
# l
# b
# u
# t
# .
# .
# c - c at
# a - a t
# t - t
# return


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_index = 0

        found_index = -1

        for i in range(len(haystack) - len(needle) + 1):
            matched = True
            if haystack[i] == needle[needle_index]:
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        matched = False
                        break
                if matched:
                    found_index = i
                    return found_index
        return found_index

haystack = "ca"
needle = "cat"

solution = Solution()
occurrence_index = solution.strStr(haystack, needle)
print(occurrence_index)