# https://leetcode.com/problems/add-binary/description/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        total = a+b
        total = str(bin(total))
        return total[2:]


a = "10"
b = "1"
solution = Solution()
binary_addition = solution.addBinary(a, b)
print(binary_addition)


class Solution:
    def addBinary(self, a:str, b:str) -> str:
        