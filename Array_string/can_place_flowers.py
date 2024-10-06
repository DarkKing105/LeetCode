flowerbed = [0,0,0]
n=2

comp = 0
count = []
for i in flowerbed:
    if i == 0:
        count.append(i)
        continue

    
    comp = comp + int((len(count) -1) / 2)
    

    if i == 1:
        count.clear()
print(comp)
try:
    if flowerbed[0] == 0 and len(flowerbed) == 1:
        comp = comp + 1
        

    if flowerbed[0] == 0 and flowerbed[1] == 0 :
        comp = comp + 1
            
    if flowerbed[-1] == 0 and flowerbed[-2] == 0 and flowerbed[-3] == 1:
        comp = comp + 1
    
except IndexError:
    pass

print(comp)
count.clear()
if comp == 0:
    for i in flowerbed[::-1]:
        if i == 0:
            count.append(i)
            print(count)

        comp = comp + int((len(count) -1) / 2)

        if i == 1:
            count.clear()

print(comp)
if comp >= n :
    print("true")
else:
    print("false")
