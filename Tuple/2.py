t=(56,78,90,23,45,67,22,44,44)
print(len(t)) # 9
print(max(t)) # 90
print(min(t)) # 22
print(sum(t)) # 

print(t.count(44)) #2
print(t.count(22)) # 1
print(t.__len__()) # 9
print(t.__contains__(90))
print(t.__contains__(91))
print(t.index(56))

# print(t[0:3])
# print(t[::-1])
# print(sum(t))
