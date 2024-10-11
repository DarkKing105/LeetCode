s = "erase*****"

star = 0
ans = [" "]

for i in s[::-1]:
    if i == '*':
        star+=1
        continue
    if star <= 0:
        ans.append(i)
    else:
        star-=1

print(''.join(ans[::-1]))




