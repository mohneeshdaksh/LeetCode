# https://leetcode.com/problems/roman-to-integer/description/

s = "I"

roman = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}


i = 0

integer = 0


while i < len(s):
    if i != (len(s) - 1) and roman[s[i]] < roman[s[i+1]]:
        integer += (roman[s[i+1]] - roman[s[i]])
        i = i+2
    else:
        integer += roman[s[i]]
        i += 1
print(integer)