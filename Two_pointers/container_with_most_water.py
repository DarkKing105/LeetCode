height = [4,3,2,1,4]
b=0
for i in range(len(height)):
    l = height[i]
    for x in range(i+1, len(height)):
        y = min(l,height[x])
        z = (x-i)*y
        if z>b:
            b=z
print(b)