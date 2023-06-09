Str = input("input string:\t")
if len(Str) % 2 != 0:
    Str1 = (len(Str) - 3) // 2
    print(Str[Str1:-Str1])
else:
    print("the number of symbols in the word is even")