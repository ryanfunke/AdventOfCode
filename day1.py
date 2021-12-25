############
## PART 1 ##
############

f = open("C:/Users/Ryan/PycharmProjects/AdventOfCode/Day1/day1.txt", "r")

# Reading data from Input on the Webpage
contents = f.readlines()
finalData = []

# Counters to help navigate through the data lists
largerCounter = 0
i = 1

# Storing data from the input file to a list
for item in contents:
    finalData.append(int(item.strip()))

# Calculating length of the list to allow for future looping through and data comparison
size = len(finalData)

# Looping through the data list to update the counter of whether the last entry was smaller than the current
# entry or not.
while i < size:
    if finalData[i] > finalData[i - 1]:
        largerCounter = largerCounter + 1
    i += 1

print(largerCounter)

############
## PART 2 ##
############

# Declaration of variables
threeSums = []
j = 2
k = 0
largerSumsCounter = 0


while j < size:
    newSum = finalData[j] + finalData[j - 1] + finalData[j - 2]
    threeSums.append(newSum)
    j += 1

threeSumsSize = len(threeSums)

while k < threeSumsSize:
    if threeSums[k] > threeSums[k - 1]:
        largerSumsCounter = largerSumsCounter + 1
    k += 1

print(largerSumsCounter)