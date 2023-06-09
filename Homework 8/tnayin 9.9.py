import random
pos = 0
neg = 0
l = []
n = int(input("input the count of numbers:\t"))
for i in range(n):
    l.append(random.randint(-100,100))
for a in l:
    if a > 0:
        pos += 1
    else:
        neg += 1
print(l)
print("pos=", pos, " neg=", neg)
