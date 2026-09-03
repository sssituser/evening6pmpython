li =[67,45,"abc"]
print(li) #67,45,abc
res = li.__add__(["kiran",7.8,True])
print(li) # 67,45,abc,kiran,7.8,True
print(res)
li.append(56)
print(li)