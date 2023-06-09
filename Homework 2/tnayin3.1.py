num = int(input("input number:\t"))
if num % 2 == 0:
    print(num," number is even\t")
    if num % 3 == 0:
        print("the number is divisible by 2 and 3")
elif num % 3 == 0:
    print(num," number is odd and divisible by 3")
else:
    print("the number is clear")

