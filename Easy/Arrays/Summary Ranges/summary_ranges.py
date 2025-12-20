# https://leetcode.com/problems/summary-ranges/description/

nums = [0,2]

summary_ranges = []

start_range = 0

for current_index in range(1, len(nums)):
    if nums[current_index] != nums[current_index - 1] + 1:
        if current_index - 1 == start_range:
            summary_ranges.append(f"{nums[current_index - 1]}")
        else:
            summary_ranges.append(f"{nums[start_range]}->{nums[current_index - 1]}")
        start_range = current_index
if current_index == len(nums)-1:
    if current_index == start_range:
        summary_ranges.append(f"{nums[current_index]}")
    else:
        summary_ranges.append(f"{nums[start_range]}->{nums[current_index]}")

print(summary_ranges)
        