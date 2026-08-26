num = int(input('Enter a number : '))
start = 1
end = num
sum = 0
while start<=end:
    if num%start == 0:
        print(start,end="  ")
        sum = sum+start
    start = start+1
print(f'\n{num} factors sum is : {sum}')

