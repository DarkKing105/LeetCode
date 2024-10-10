nums = nums = [-1,-1,-1,1,1,1]
'''
l_sum = 0
r_sum = 0

for i in range(len(nums)):
    r_sum = r_sum + nums[i]
    print(r_sum,l_sum)

for x in range(len(nums)):
    r_sum = r_sum - nums[x]
    if r_sum == l_sum:
        print(x)
        break
    l_sum = l_sum + nums[x]

if l_sum != r_sum:
    print(-1)

'''

sumLeft = [0]

for i in range(len(nums)):
    x = sumLeft[i] + nums[i]
    sumLeft.append(x)

max = sumLeft[len(sumLeft) - 1]

for i in range(len(nums)):
    sumRight = max - sumLeft[i+1]
    if sumLeft[i] == sumRight:
        print(i)
        break
    if i+1 == len(nums) and sumLeft[i] != sumRight:
        print(-1)

    
