number = int(input("input number for check"))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += i
if sum == number: 
    print(number, " number is perfect")
else:
    print(number, " number is not perfect")