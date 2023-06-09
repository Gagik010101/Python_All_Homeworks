def Sentense(String,upper,lower):
    for i in String:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            continue
    return f"capital letter = {upper}", f"lower case = {lower}"
    


String = input("input sentence։\t") 
upper = 0
lower = 0
print(Sentense(String,upper,lower))