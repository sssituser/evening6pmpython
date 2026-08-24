num = int(input('Enter a number : '))
count = 0
sum = 0
while num>0:
    digit = num%10
    print(digit,end=" ")
    count=count+1
    sum = sum+digit
    num=num//10
avg = sum/count
print(f'Sum : {sum} Count: {count} Average is :{avg}')

