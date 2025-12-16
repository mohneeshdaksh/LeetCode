# https://leetcode.com/problems/plus-one/description/

digits = [9,9,9]

if all(d == 9 for d in digits) == True:
    for n in range(len(digits)):
        digits[n] = 0
    digits.insert(0, 1)

else:
    for n in range(len(digits) - 1, -1, -1):

        if digits[n] == 9:
            digits[n] = 0

        else:
            digits[n] += 1
            break

print(digits)