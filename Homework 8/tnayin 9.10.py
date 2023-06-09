import random
l = []
number = int(input("input the count of numbers"))
for i in range(number):
    l.append(random.randint(0,200))
print(l)
pos1 = int(input("input pos1 - ")) - 1
pos2 = int(input("input pos2 - ")) - 1
n = l[pos1]
l[pos1] = l[pos2]
l[pos2] = n
print(l)