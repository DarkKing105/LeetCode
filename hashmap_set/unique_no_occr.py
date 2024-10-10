arr = [1,2]
'''
s = set(arr)
occur = []

for i in s:
    x=[x for x in arr if x==i] 
    occur.append(len(x))

occur_set = set(occur)
if len(occur) == len(occur_set):
    print('true')
else:
    print('false')
'''

occurences = {}

for num in arr:
    if num in occurences:
        occurences[num] += 1
    else:
        occurences[num] = 1


seen = set()

for key in occurences:
    print(occurences)
    if occurences[key] in seen:
        print('false')
    else:
        seen.add(occurences[key])

print('true')