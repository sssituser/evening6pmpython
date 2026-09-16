s = {10,34,67,89,50,66}
print(s)
# for i in s:
#     print(i,end="  ")
# element =int(input('Enter Element : '))
# s.add(element)
# print(s)
# print(f"deleted elment is {s.pop()}")
# print(s)
s.remove(67)
print(s)
# s.remove(100)# This will give keyerror, since the elmen is not present i the set.
s.discard(100)
print(s)
s.clear()
print(s)