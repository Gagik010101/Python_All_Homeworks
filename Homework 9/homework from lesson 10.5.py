def Numbers(number):
    L = []
    l = []
    for i in range(number):
        num = int(input(f"input {i+1} number:\t"))
        l.append(num)
    print(l)
    for n in l:
        if n % 2 == 0:
            L.append(n)
    return f"even numbers {L}"

number = int(input("input quantity numbers:\t"))
print(Numbers(number))