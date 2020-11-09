index=0
start=0
s = "abcdefdac"

for a in range(len(s) - 1):
    x = a+1
    if str(s[a]) > str(s[x]):
        index = str(s[start:x])
        print(index)
        break


