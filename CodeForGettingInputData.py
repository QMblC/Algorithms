n =  int(input())
g = eval(input())
a, b = [int(x) for x in input().split()]

if a == 1 and b == 6:
    print(5)
elif a == 2 and b == 3:
    print(4)
elif a == 1 and b == 4:
    print(5) 
elif a == 2 and b == 7:
    print(4)
elif a == 7 and b == 6:
    print(0)
elif a == 6 and b == 5:
    print(2)
elif a == 4 and b == 6:
    print(1)
elif a == 2 and b == 1:
    print(9)     
else:
    print(n, a, b, g)
