## https://leetcode.com/problems/palindrome-number/description/

input = 12121

inputInText = str(input)

newStack = []

for i in inputInText:
    newStack.append(i)

for i in inputInText:
    if i == newStack[-1]:
        newStack.pop()

if len(newStack) == 0:
    print(True)
else:
    print(False)
