numsList = [12,45,67,89,55,13,66,89]
print(numsList[0],numsList[1],numsList[5])
print(numsList[-2],numsList[-4])
print(len(numsList))
# len is function which can be used to count the elements present in sequential data or string
print(numsList)
# displaying the list elements using +ve index
for i in range(len(numsList)):
    print(f'{i}---->{numsList[i]}')
    
