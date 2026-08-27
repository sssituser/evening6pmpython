num = int(input('Enter a number : '))
start =1
end =num
count = 0
while start<=end:
    if num%start==0:
        count += 1
    start += 1
if count== 2:
    print(f'{num} is a Prime number')
else:
    print(f'{num} is not a Prime number')


    -121
    
    121-