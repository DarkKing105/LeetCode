nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k=3


zero = 0
l = 0
max_one = 0
for i in range(len(nums)):
    if nums[i] == 0:
        zero+=1
    while zero > k:
        if nums[l] == 0:
            zero-=1
        l+=1
        
    ans = i-l+1
    max_one = max(ans, max_one)
        
print(max_one)
  
  

 