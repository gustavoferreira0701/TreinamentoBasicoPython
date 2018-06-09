from functools import reduce

listWithTwentyNumbers = range[1:20]
listSum = reduce((lambda x, y: x + y), listWithTwentyNumbers)

print("List Sum => " + str(listSum))

listLength = len(listWithTwentyNumbers)

print("List Length => " + str(listLength))

tupleFromList = tuple(listWithTwentyNumbers)

isATuple = tupleFromList is tuple

print(type(tupleFromList))

weirdList = [1, 2, 4, 2, 3, 8, 3, 5, 10, 11, 4, 40, 20, 30, 3]

weirdList.sort()

weirdList = list(set(weirdList))

print(weirdList)

multipliedByTwoList = list(map((lambda x: x*2), weirdList))

myAgedDividedByTwo = 33/2

print("My age divided by two: " + str(int(myAgedDividedByTwo)))

if myAgedDividedByTwo in weirdList:
    print("My age is inside of the list")
else:
    print("My age isn't inside of the list")

intersectionedList = list(set(weirdList).intersection(multipliedByTwoList))

print(weirdList)
print(multipliedByTwoList)
print(intersectionedList)

bigList = range[3:553]

for i in range(554):
    if i > 2:
        bigList.append(i)

print(bigList)

family_dictionary = {
    'gustavo': 33,
    'pamela': 35,
    'henrique': 61
}

familyTotalAge = reduce((lambda x:y, x + y),family_dictionary)
