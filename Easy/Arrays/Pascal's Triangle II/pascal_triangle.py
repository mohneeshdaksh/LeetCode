# https://leetcode.com/problems/pascals-triangle-ii/description/

rowIndex = 3

numRows = rowIndex + 1

pascal_triangle = []

for current_row in range(numRows):
    pascal_triangle.append([1] * (current_row + 1))

    if current_row >= 2:
        for i in range(1, len(pascal_triangle[current_row]) - 1):
            pascal_triangle[current_row][i] = pascal_triangle[current_row - 1][i] + pascal_triangle[current_row - 1][i - 1]

print(pascal_triangle[rowIndex])