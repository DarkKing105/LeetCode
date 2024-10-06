chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars.sort()

s=str()
a=''

for index, value in enumerate(chars):
    if value in s:
        a+=1
    if value not in s:
        if a == 1:
            pass
        else:
            s = s+str(a)
        s = s+value
        a=1
    if index  == len(chars) -1:
        s = s+str(a)
        chars = list(s)


print(chars)

