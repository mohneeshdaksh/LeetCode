# https://leetcode.com/problems/summary-ranges/description/

nums = []

summary_ranges = []

if nums:
    start_range = 0

    for current_index in range(1, len(nums)):
        if nums[current_index] != nums[current_index - 1] + 1:
            if current_index - 1 == start_range:
                summary_ranges.append(f"{nums[current_index - 1]}")
            else:
                summary_ranges.append(f"{nums[start_range]}->{nums[current_index - 1]}")
            start_range = current_index
    if start_range == len(nums)-1:
        summary_ranges.append(f"{nums[-1]}")
    else:
        summary_ranges.append(f"{nums[start_range]}->{nums[-1]}")

print(summary_ranges)