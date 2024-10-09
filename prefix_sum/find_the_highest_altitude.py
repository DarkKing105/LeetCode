gain = [-5,1,5,0,-7]
ans = []
k = 0
ans.append(0)
ans.append(gain[0])
for i in range(len(gain)):
     j = i+1
     if j == len(gain):
          break
          
     k = k +  gain[j]
     ans.append(k)

print(ans)

