orcs_heights = "1 1 2 2 2 2 1 1 1".split()
grimmorhus_heights = "1 2 1".split()

def get_different_height(array, height):
    different_heights = 0
    for i in array:
        if height != i:
            different_heights += 1
    return different_heights


for grim_height in grimmorhus_heights:

    same_height_left = 0
    different_height_right = get_different_height(orcs_heights, grim_height)
    points = 0

    for orc_height in orcs_heights:
        if orc_height == grim_height:
            same_height_left += 1
        else:
            different_height_right -= 1
    
        points = max(same_height_left * different_height_right, points)

    print(points, end=' ')    