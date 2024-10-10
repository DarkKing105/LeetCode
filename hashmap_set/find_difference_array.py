nums1 = [1,2,3]
nums2 = [2,4,6]

nums1_hash = set(nums1)
nums2_hash = set(nums2)

res1 = []
res2 = []

for i in nums1_hash:
    if i not in nums2_hash:
        res1.append(i)
        
for i in nums2_hash:
    if i not in nums1_hash:
        res2.append(i)
        
print([res1,res2])