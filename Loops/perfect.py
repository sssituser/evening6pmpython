'''
num = 6
1 + 2 + 3=>6 

'''
num = int(input('Enter a number : ')) # num =6
sum = 0
start = 1
end = num

while start<end: # 1<6-T 2<6-T 3<6-T 4<6-T5<6 6<6-F
    if num%start == 0: # 6%1==0 0==0-T 6%5==0 1==0 
        sum = sum+start # sum=6
    start=start+1 # start = 2,3,4,5,6

if sum == num: # if statement is check num
    print(f'{num} is a Perfect Number')
else:
    print(f'{num} is not a Perfect Number')

