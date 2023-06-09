start = int(input("Input the starting point:\t"))
end = int(input("input the ending point:\t"))
prime_numbers = []
for number in range(start, end):
    if number > 1:
        if number % 2 == 0:
            continue
        for i in range(3, (number//2)+3):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)

print(prime_numbers)