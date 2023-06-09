Str = input("input string:\t")
n = int(input("input number for delete index"))
Str1, Str = Str[:n-1], Str[n:]
print(Str1 + Str)