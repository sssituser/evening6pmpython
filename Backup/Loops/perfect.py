num = int(input('Entre a number : ')) # num = 6
start = 1
count = 0
sum = 0
while start<num: # 1<6- T 2<6 3<6 4<6 5<6 6<6-F
    if num%start == 0: # 6%5==0 1==0
        print(start) # 1,2,3
        count += 1 # count = 3
        sum +=start # sum = 6
    start+=1 # start = 2,3,4,5 , 6

if count ==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not Prime number')
if sum==num:
    print(f'{num} is a Perfect number')
else:
    print(f'{num} is not Perfect number')
    