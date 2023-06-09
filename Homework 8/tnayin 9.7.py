sentense = input("input your sentense:\t").lower().split()
print(sentense)
words_count = {}
for word in sentense:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
print(words_count)
for key, value in words_count.items():
    print(f"word: {key}, count: {value}")