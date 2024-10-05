nums = [1,12,-5,-6,50,3]
k = 4
ans = 0
avg=(sum(nums[0:k]))
a = len(nums)
max_avg=avg/k

for i in range(k,a):
    avg+=nums[i]
    avg-=nums[i-k]

    avg_1 = avg/k
    
    max_avg=max(max_avg,avg_1)

print(max_avg)