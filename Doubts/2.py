s = "SSSIT"
print(s[0],s[1],s[2],s[3],s[4])
print(s[-1],s[-2],s[-3],s[-4],s[-5])

# [start:end:step]
print(s[0:2])
print(s[:-3:-1])
print(s[::-1])

print(s.__getitem__(4))
print(f'no of charcters in in :{len(s)}')