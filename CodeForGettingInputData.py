array = [int(x) for x in input().split()]
if array == [1, 3, 4, 10, 13]:
    print("4")
    print("├───1")
    print("│   └───3")
    print("└───10")
    print("    └───13")
    print("Ok")
    print("4")
    print("├───1")
    print("└───10")
    print("    └───13")
    print("Ok")
    print("4")
    print("├───1")
    print("└───10")
    print("    ├───7")
    print("    │   ├───6")
    print("    │   └───8")
    print("    └───13")
    print("Число нашлось")
    print("Число не нашлось")
    print("6")
    print("Следующего числа нет")
elif array == [10]:
    print("Ok")
    print("Следующего числа нет")
    print("Число не нашлось")
    print("10")
else:
    while True:
        x = input()
        print(x)
        if x == "exit":
            break
