val = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(f'{i*i}\t',end=" ")
        val+=1
    print("\n")
for i in range(i-1,0,-1):
    for j in range(1,i+1):
        print(f'{i*i}\t',end="")
        val+=1
    print("\n")
  
#======================
'''
1                               1
1   4                           4   4
1   4   9                       9   9   9
1   4   9   16                  16  16  16  16
1   4   9   16  25              25  25  25  25  25
1   4   9   16                  16  16  16  16
1   4   9                       9   9   9
1   4                           4   4
1                               1

'''
