candies = [12,1,12]
extraCandies = 10
#make a list result with len(candies) and append all true
#large no. in list candies is 5 and for true each kids should have 5 or greater tha 5 candies, that means lesser than equal to 4 is false
#so i will minus 4 with extra candies 3 which is 1 and check in list if any kids has 1 candies and take their index number and append false to that index


result = []
for i in range(0,len(candies)):
    result.append(True)

large = max(candies)
less_candies = large - extraCandies

false_list = []
for x in range(len(candies)):
    for i in range(0,less_candies):
        if candies[x] == i: 
            del result[x]
            result.insert(x, False)



print(result)

