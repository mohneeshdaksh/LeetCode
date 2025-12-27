# https://leetcode.com/problems/length-of-last-word/description/

# Running the loop in reverse direction 
# Capture first non-space character


# Solution 1:

# class Solution:
#     def lengthOfLastWord(self, s:str) -> int:

#         word_length = 0

#         found = False

#         for i in range(len(s) - 1, -1, -1): 
#             if not s[i].isspace() and found == False:
#                 for j in range(i, -1, -1):
#                     if not s[j].isspace():
#                         word_length += 1
#                         if j==0:
#                             found = True
#                             break 
#                     else:
#                         found = True
#                         break
#             else:
#                 if found == True:
#                     break
#         return word_length

# s = " Hell Hello "

# solution = Solution()
# last_word_length = solution.lengthOfLastWord(s)
# print(last_word_length)


# Solution 2

class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        s = s.strip()
        words = s.split()
        return len(words[-1])

s = "ohHell  Yeah  "
solution = Solution()
last_word_length = solution.lengthOfLastWord(s)
print(last_word_length)