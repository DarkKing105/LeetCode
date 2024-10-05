s = "abc"
t = "ahbgdc"
i = 0
j = 0

while i<len(s) and j<len(s):
    if s[i] == t[j]:
        i+=1
    j+=1

    if i==len(s):
        print('true')