def sentense(String):
    l = []
    elements = set()
    for i in String:
        elements.add(i)
    return elements


String = input("input sentense:\t")
print(sentense(String))