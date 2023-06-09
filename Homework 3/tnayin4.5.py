n = 0
first_num = int(input("enter the first number:\t"))
last_num = int(input("import the last number:\t"))
if first_num < last_num:
    for i in range(first_num,last_num + 1):
        if i % 7 == 0:
            n += 1
    print("the number of numbers is even ",n)
else:
    print("an error occurred")