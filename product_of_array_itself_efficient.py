nums = [1,2,3,4]
res = [1] * (len(nums))

prefix = 1
for i in range(len(nums)):
    print(res)
    res[i] = prefix
    prefix *= nums[i]
postfix=1
for i in range(len(nums) - 1, -1, -1):
    print(res)
    res[i] *= postfix
    postfix *= nums[i]

print(res)