str1 = "CXTXNCXTXNCXTXNCXTXNCXTXN"
str2 = "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"

#print(str1.find(str2))
#print(str2.count("ABABAB"))
#print(set(str2))

def unique(x):
    unique =[]
    for i in x:
        if i not in unique:
            unique.append(i)
            
    uniques = ''.join(unique)
    print(uniques)
    while True:
        r_value = len(unique)
        
        try:
            unique.append(x[r_value])

        except IndexError:
            pass

        uniques_1 = ''.join(unique)

        uniques_count = x.count(uniques)
        uniques1_count = x.count(uniques_1)


        if uniques1_count > uniques_count:
            uniques = ''.join(unique)

        if uniques1_count == uniques_count:
            return uniques_1
            

        else:
            return uniques
            
        
x = ""
string1 = unique(str1)
string2 = unique(str2)

if string1 in string2:
    print(string2)
else:
    print(x)