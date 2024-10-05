nums = [3,1,3,4,3]
k=6
#nums  = [i for i in nums if i<99]
#x = 0
#print(nums)
#while True:
#    if len(nums) == 0:
#        break
#    a = max(nums)
#    nums.remove(a)
#    b = k - a
#    if b in nums:
#        x+=1
#    try:
#        nums.remove(b)
#        print(nums)
#    except ValueError:
#        pass
    



#print(x)
nums.sort()

x = 0
y = len(nums) - 1
z = 0

while x < y:
    a = nums[x]
    b = nums[y]
    c=a+b

    if c == k:
        z+=1
        x+=1
        y-=1
    elif k>c:
        x+=1
    else:
        y-=1
        
    

print(z)
