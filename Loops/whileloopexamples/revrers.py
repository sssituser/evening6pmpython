num = int(input('Enter a number  : ')) # num = 123

count = 0
reverse = 0
while num>0: 
    digit = num%10 
    reverse = reverse*10+digit 
    num=num//10  
print(f'Reverse of a given number is : {reverse}')



