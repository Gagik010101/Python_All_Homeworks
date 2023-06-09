n = int(input("input number of words:\t")) # bareri qanaki nermucum
word = {}
answer = {}
for i in range(1,n+1):         # dictionary-i nermucum
    s = input(f"input {i} word:\t")
    word[i] = s
print(word)
for w in word:                 # nor dictionary-i karucum
    g = word[w]
    if g in answer:
        continue
    answer[g] = len(g)
print(answer)

