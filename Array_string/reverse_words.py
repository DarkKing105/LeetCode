s = "F R  I   E    N     D      S      "
a = s.strip()
q = a.split(" ")


while True:
    for i in q:
        if i == '':
            q.remove(i)
    if '' in q:
        continue
    else:
        break

d = q[::-1]

print(" ".join(d))