def sum_of_numbers(number):
    sum = 0
    l = []
    for i in range(number):
        lnum = int(input(f"input {i+1} number:\t"))
        l.append(lnum)
    print(l)
    for n in l:
        sum += n
    return sum


number = int(input("input number:\t"))
print(sum_of_numbers(number))
