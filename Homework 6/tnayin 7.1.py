A = []
B = []
for i in range(20):
    if i <= 9:
        a = int(input(f"input {i+1} number for List A:\t"))
        A.append(a)
    else:
        b = int(input(f"input {i+1} number for List B:\t"))
        B.append(b)
print(A,B)
print("1.1")
A = set(A)
B = set(B)
print(A,B)
print("1.2")
if A == B:
    print(True)
else:
    print(False)
print("1.3")
C = A.union(B)
print(C)
print("1.4")
D = A.intersection(B)
print(D)
print("1.5")
E = A.difference(B)
print(E)
E = B.difference(A)
print(E)

