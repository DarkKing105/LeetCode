gain = [-4,-3,-2,-1,4,3,2]
x = 0
ans = 0

for i in range(len(gain)):
    x = x + gain[i]
    ans = max(ans,x)

print(ans)
