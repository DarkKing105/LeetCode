nums = [0,1,0,3,12]
len_array = len(nums)
count = 0

while count < len_array:
    if nums[count] == 0:
        nums.remove(0)
        nums.append(0)
    count+=1

print(nums)
