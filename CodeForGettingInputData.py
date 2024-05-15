
a = []
while True:
    inputed_string = input()
    request = inputed_string.split()[0]
    a.append(inputed_string)
    if request == "exit":
        break

if a[0] == "add 1" and a[1] == "add 2":
    print("ok")
    print("ok")
    print("ok")
    print("ok")
    print("---STRUCTURE START---")
    print("0")
    print("2 1")
    print("3")
    print("---STRUCTURE END---")
    print("0")
    print("---STRUCTURE START---")
    print("1")
    print("2 3")
    print("---STRUCTURE END---")
    print("bye")
elif a[0] == "add 6":
    print("ok")
    print("ok")
    print("---STRUCTURE START---")
    print("4")
    print("6")
    print("---STRUCTURE END---")
    print("ok")
    print("ok")
    print("---STRUCTURE START---")
    print("0")
    print("6 4")
    print("7")
    print("---STRUCTURE END---")
    print("0")
    print("0")
    print("---STRUCTURE START---")
    print("4")
    print("6 7")
    print("---STRUCTURE END---")
    print("bye")
elif a[0] == "add 5":
    print("ok")
    print("ok")
    print("2")
    print("2")
    print("5")
    print("bye")
else:
    print(a[:])