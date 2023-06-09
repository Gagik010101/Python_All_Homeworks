quantity = int(input("import numbers count:\t"))
L = []
for i in range(quantity):
    number = int(input(f"input {i} number:\t"))
    L.append(number)
print(L)
M = []
for n in L:
    n *= n
    M.append(n)
print(M)