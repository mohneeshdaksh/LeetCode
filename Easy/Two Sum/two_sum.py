# https://leetcode.com/problems/two-sum/description/

nums = [2,7,11,15]

target = 9
output = []

for n in range(len(nums)):
    for m in range(n + 1, len(nums)):
        sum = nums[n] + nums[m]
        if sum == target:
            output.append(n)
            output.append(m)
            break

print(output)

# Need to work on Runtime