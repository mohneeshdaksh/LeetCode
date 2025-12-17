# https://leetcode.com/problems/pascals-triangle-ii/description/

#     [1]
#    [1,1]
#   [1,2,1]
#  [1,3,3,1, 1]
# [1,4,6,4,1]

rowIndex = 1

row = [1]

for i in range(rowIndex):
    row.append(1)
    for j in range(len(row) - 2, 0, -1):
        row[j] = row[j] + row[j-1]

print(row)