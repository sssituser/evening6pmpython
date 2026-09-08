s = "welcome"
for i in range(len(s)):
     print(f'{s[i]}=>{i}',end=" ")
print()

for i in range(-1,-len(s)-1,-1): 
    print(f'{s[i]}==>{i}',end=" ")
print()

for i in range(-(len(s)),0,1):# range(-7,0,1)
    print(f'{s[i]}=>{i}',end=" ")
print()