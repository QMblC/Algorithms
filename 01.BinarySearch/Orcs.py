orcs_heights = input().split()
grimmorhus_heights = input().split()

completed = dict()
result = []

def get_different_height(height, array = orcs_heights):
    different_heights = 0
    for i in array:
        if height != i:
            different_heights += 1
    return different_heights

for height_index in range(len(grimmorhus_heights)):

    if grimmorhus_heights[height_index] in completed:
        result.append(str(completed[grimmorhus_heights[height_index]]))
        continue   

    same_height_left = 0
    different_height_right = get_different_height(grimmorhus_heights[height_index])

    points = 0

    for orc_height in orcs_heights:

        if orc_height == grimmorhus_heights[height_index]:
            same_height_left += 1
            points = max(same_height_left * different_height_right, points)
        else:
            different_height_right -= 1

        if (different_height_right < same_height_left):
            break
        
    completed[grimmorhus_heights[height_index]] = points
    result.append(str(points))
 
print(" ".join(result))