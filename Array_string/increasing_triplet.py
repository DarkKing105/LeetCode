nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])
print(sorted_indices)
def triplet(a):
    for x in range(0, len(a)):
        i = a[x]
        try:
            j = a[x+1]
            k = a[x+2]
        except IndexError:
            j = 0
            k = 0
            pass

        if i < j < k:
            return True
            break



x = triplet(nums)
y = triplet(sorted_indices)
print(x,y)
if x == True or y == True:
    print('true')
else:
    print('false')