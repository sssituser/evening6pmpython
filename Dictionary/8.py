'''
Write a program to display
    1. Only Unique elements from the given list
    2. only duplicate elements
'''
li =[12,12,34,56,78,90,90,78,67,68,98,98,98]
di={}
for element in li:
    if di.__contains__(element):
        val = di[element]
        di[element]=val+1
    else:
        di[element]=1 
print(di)

print("Displaying unique elements")
for k in di.keys():
    if di[k]==1:
        print(k,di[k])
print("Displaying duplicate elements")
for k in di.keys():
    if di[k]==2:
        print(k,di[k])
print("Displaying Triplecate elements")
for k in di.keys():
    if di[k]==3:
        print(k,di[k])
