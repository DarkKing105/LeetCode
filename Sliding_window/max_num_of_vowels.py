s = "zpuerktejfp"
k = 3
v = ['a', 'e', 'i', 'o', 'u']

#ans = 0
#a=0
#t = 0
#for i in s:
#    if i in v:
#        for x in s[a:a+k]:
#            if x in v:
#                t+=1
#                if t > ans:
#                    ans = t
#        t = 0
#        if ans == k:
#            break
#    a+=1

#print(ans)

ans = 0
t=0
index = 0

for i in s[0:k]:
    if i in v:
        ans+=1
    if t == k or ans==k:
        print(ans)
        break



for i in s[k:len(s)]:
    t = max(ans,t)
    if i in v:
        ans+=1
    if s[index] in v:
        ans-=1
    index+=1
    t = max(ans,t)

print(t) 