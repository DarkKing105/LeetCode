#make a lsit of vowels
#check vowels in s list, append in vowel_s list and append index of the vowels in index list from
#now construct a reverse word with above list


s = "Ice CreAm"
vowels = ['a','e','i','o','u']
vowels_s = []
index = []
for i in range(len(s)):
    if s[i].lower() in vowels:
        vowels_s.append(s[i])
        index.append(i)

finalstring = list(s[:])

c = 0
vowels_back = vowels_s[::-1]
for i in index:
    del finalstring[i]
    finalstring.insert(i, vowels_back[c])
    c+=1

final_str = ''.join(finalstring)
print(final_str)
