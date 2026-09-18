name = input("Enter Name : ") #abbc
d = {}
for char in name:
    if d.__contains__(char):
        val = d[char]
        d[char] = val+1
    else:
        d[char]=1     # d={a:1,b:1}
for kvp in d.items():
    print(kvp)