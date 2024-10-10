nums = [0,1,1,1,0,1,1,0,1]
zero = 0
left = 0
res = 0
ans = 0

if 0 not in nums:
    print(len(nums) - 1)
else:
    nums.append(0)
    nums.insert(0,0)

    for i in range(len(nums)):
        if nums[i]==0:
            zero+=1
        
        while zero>2:
            ans = (i-left) - 2
            if nums[left] == 0:
                zero-=1
            left+=1
        res = max(res,ans)

    print(res)