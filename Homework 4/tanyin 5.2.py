Str = input("input string:\t")
if len(Str) > 3:
    if Str[-1:-4:-1] == "gni":
        print(Str + "ly")
    else:
        print(Str + "ing")
else:
    print(Str)