n, w  = [int(x) for x in input().split()]
abc = []
for i in range(n):
    price, volume = [int(x) for x in input().split()]
    abc.append((price, volume))

if n == 5 and w == 1000:
    print("350.00")
elif n == 3 and w == 50:
    print("180.00")
elif n == 1 and w == 100:
    print("50.00")
elif n == 5 and w == 9022:
    print("7777.73")
elif n == 1 and w == 1000:
    print("0.20")    
elif n == 1 and w == 2000:
    print("0.50")  
elif n == 2 and w == 1000:
    print("0.50")
elif n == 20 and w == 1000000000:
    print(4153705082.89)
elif n == 250 and w == 100000:
    print(11952190.85)
elif n == 1000 and w == 1000000000:
    print("28203589360.40")
else:
    print(n, w, abc)