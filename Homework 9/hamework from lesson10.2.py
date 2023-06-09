def function(start,end,number):
    if start > end:
        step = -1
    else:
        step = 1
    if number in range(start,end,step):
        return (f"{number} э ({start},{end})")
    else:
         return (f"{number} э ({start},{end})")
    
number = int(input("input number:\t"))
start = int(input("input first number:\t"))
end = int(input("input last number:\t"))
print(function(start,end,number))