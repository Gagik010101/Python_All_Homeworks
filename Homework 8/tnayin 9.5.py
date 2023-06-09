n = int(input("input number:\t"))
for i in range(n+1):
    for a in range(i):
        print("*", end=" ")
    print("")
    if i == n:
        for i in range(n-1,0,-1):
            for a in range(i,0,-1):
                print("*", end=" ")
            print("")
