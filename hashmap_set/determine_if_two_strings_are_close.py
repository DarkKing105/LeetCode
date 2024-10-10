word1 = "cabbba"
word2 = "abbccc"

'''
if len(word1) != len(word2):
    print('false')

else:
    w1 = sorted(set(word1))
    w2 = sorted(set(word2))

    if w1 == w2:
        print('true')
    else:
        print('false')
'''

occur1 = {}
occur2 = {}

for i in word1:
    if i in occur1:
        occur1[i] +=1
    else:
        occur1[i] = 1
for i in word2:
    if i in occur2:
        occur2[i] +=1
    else:
        occur2[i] = 1

if sorted(occur1.keys()) != sorted(occur2.keys()) or set(occur1.values()) != set(occur2.values()) and sorted(occur1.values()) != sorted(occur2.values()):
    print('false')
else:
    print('true')

