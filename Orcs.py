
orcs_heights = input().split()
grimmorhus_heights = input().split()

def get_different_height(height, array):
    different_heights = 0
    for i in array:
        if height != i:
            different_heights += 1
    return different_heights

for height_index in range(len(grimmorhus_heights)):

    grim_height = grimmorhus_heights[height_index]
    
    same_height_left = 0
    different_height_right = get_different_height(grim_height, orcs_heights)
    #different_height_right = len(orcs_heights) - orcs_heights.count(grim_height)
    points = 0

    for orc_height in orcs_heights:
        if orc_height == grim_height:
            same_height_left += 1
        else:
            different_height_right -= 1
        
        points = max(same_height_left * different_height_right, points)

    if (height_index == len(grimmorhus_heights) - 1):
        print(points, end='') 
    else:
        print(points, end=' ')    