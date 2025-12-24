# https://leetcode.com/problems/apple-redistribution-into-boxes/description/

apple = [5,5,5]
capacity = [2,4,2,7]
capacity.sort()

total_apple = 0
for i in apple:
    total_apple += i

total_boxes = 0
total_boxes_capacity = 0
for j in range(len(capacity)-1, -1, -1):
    total_boxes_capacity += capacity[j]
    total_boxes += 1
    if total_boxes_capacity >= total_apple:
        print(total_boxes)
        break