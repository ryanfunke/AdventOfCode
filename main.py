f = open("C:/Users/Ryan/PycharmProjects/AdventOfCode/Day1/day1.txt", "r")

contents = f.readlines()
finalData = []
largerCounter = 0
i = 1

for item in contents:
    finalData.append(int(item.strip()))

size = len(finalData)

while i < size:
    if finalData[i] > finalData[i - 1]:
        largerCounter = largerCounter + 1
    i += 1

print(largerCounter)


