str1 = "CXTXNCXTXNCXTXNCXTXNCXTXN"
str2 = "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"

#print(str1.find(str2))
#print(str2.count("ABABAB"))
#print(set(str2))
def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

if str1 + str2 == str2 + str1:
    x = computeGCD(len(str1),len(str2))
    print(str1[:x]) 
else:
     print("")



