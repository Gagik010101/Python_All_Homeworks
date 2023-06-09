n = int(input("input number:\t"))
for i in range(n+1):
    for s in range(i):
        print(s+1, end=" ")
    print("")
for i in range(n+1):
    for s in range(i):
        print("*", end=" ")
    print("")

