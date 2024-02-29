velocity_outskirts, velocity_city = [int(x) for x in input().split()]
outskirts_percent = float(input())

left = 0
right = 1

def get_time(x: float, y: float, velocity):
    
    return (x * x + y * y) ** 0.5 / velocity

while True:

    middle1 = left + (right - left) / 3
    middle2 = right - (right - left) / 3

    middle1_time = get_time(middle1, outskirts_percent / 100, velocity_outskirts) + \
        get_time(1 - middle1, 1 - (outskirts_percent / 100), velocity_city)
    
    middle2_time = get_time(middle2, outskirts_percent / 100, velocity_outskirts) + \
        get_time(1 - middle2, 1 - (outskirts_percent / 100), velocity_city)
    
    if (middle1_time > middle2_time):
        left = middle1
    else:
        right = middle2


    if str(middle1)[:9] == str(middle2)[:9]:
        print("{:f}".format(round(middle2 * 1000000) / 1000000))
        break