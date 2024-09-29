
nums = [1,2,3,4]
result = []

for index, item in enumerate(nums):
    copy = nums[:]
    del copy[index]
    total = 1
    for x in copy:
        total *= x
    result.append(total)

print(result)