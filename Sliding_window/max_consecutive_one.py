nums = [0,1,0,0,1]
k=1
index=[]
zero = 0
max_one = 0
first_zero = 0

for i in range(len(nums)):
    if nums[i] == 0:
        zero+=1
        index.append(i)
    if zero==k:
        max_one = i+1
        print(max_one,i)
        zero=0
        
        
print(max_one)