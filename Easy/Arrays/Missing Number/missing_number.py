# https://leetcode.com/problems/missing-number/description/

nums = [3,0,1]
n = len(nums)

# Solution 1
# number_tracker = [False] * (n+1)

# for i in nums:
#     number_tracker[i] = True
# for j in range(len(number_tracker)):
#     if number_tracker[j] == False:
#         print(j)

# # Solution 2


# expected_sum = n*(n+1)//2
# actual_sum = 0
# for i in nums:
#     actual_sum += i
# print(expected_sum-actual_sum)


# Solution 3

missing_number = 0

for i in range(n+1):
    missing_number ^= i

for j in nums:
    missing_number ^= j

# print(missing_number)

x = 6 ^ 3
# 110 = 1*2^2 + 1*2^1 + 0*2^0 = 6
# 011 = 1*2^1 + 1*2^0 = 3
# 101 = 4+1 = 5
# 97 = 90 + 7 = 9*10^1 + 7*10^0
print(x)