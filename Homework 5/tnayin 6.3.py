number = int(input("import numbers count:\t"))
L = []
for i in range(number):
    s = int(input(f"input {i} number:\t"))
    L.append(s)
print(L)
sum = 1
for n in L:
    sum *= n
print(sum)