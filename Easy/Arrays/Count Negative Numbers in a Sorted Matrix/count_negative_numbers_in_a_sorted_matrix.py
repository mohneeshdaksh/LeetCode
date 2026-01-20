# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

#grid = [[4,3,2,1],[3,2,1,1]]

count = 0

for i in grid:
    for j in i:
        if j < 0:
            count += 1

print(count)