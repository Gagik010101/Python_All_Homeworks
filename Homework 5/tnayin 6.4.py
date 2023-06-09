number = int(input("import numbers count:\t"))
L = []
for i in  range(number):
    n = int(input(f"input {i} number:\t"))
    L.append(n)
print(L)
for index in range(len(L)):
    if L[index] == 20:
        L[index] = 200
        break
    else:
        print("The number 20 was not found in the list")
print(L)

