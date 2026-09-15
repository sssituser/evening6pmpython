t = (12,"abc",True,6+7j,[56,78],('aa',56,False),6.7)
print("Displaying the elements using +ve index")
for i in range(len(t)):
    print(f'index - {i} - > element - {t[i]}')
  
print("\n")
print("Displying the elements of tuple using -ve index")
for i in range(-len(t),0,1):
    print(f'index - {i} - > element - {t[i]}')
 
for i in range(len(t)):
    print(f'{t[i]}',end=" ")   
print("\n")
print("Displying the elements of tuple using -ve index")
for i in range(-len(t),0,1):
    print(f'{t[i]}',end=" ")
print()
for i in range(-1,-(len(t)+1),-1):
    print(t[i],end=" ")
    
    