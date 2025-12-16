# https://leetcode.com/problems/plus-one/description/

digits = [1,2,3]

for n in range(len(digits) - 1, -1, -1):
    if digits[n] != 9:
        digits[n] += 1
        break
    else:
        digits[n] = 0

print(digits)
