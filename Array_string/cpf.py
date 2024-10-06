flowerbed = [1,0,0,0,1,0,0]
n=2

comp = 0
count = []
flowerbed.insert(0,0)
flowerbed.append(0)
flowerbed.append(1)
for i in flowerbed:
    if i == 0:
        count.append(i)
    
    if i == 1:
        comp = comp + int((len(count) -1) / 2)
        count.clear()
           
    
print(comp)
print(flowerbed)