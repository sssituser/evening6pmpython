s1 = {1,2,3,4,5}
s2 = {'a','b','c',1,2,10+9j}
# s3 = s1.union(s2)
s3 = s1|s2
print(s1)
print(s2)
print(s3)
#s4 = s1.intersection(s2)
s4 = s1 & s2
print(s4)
#s5 = s1.difference(s2)
s5 = s1-s2
print(s5)