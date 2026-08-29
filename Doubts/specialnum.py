num = int(input('Enter a number : '))
sum = 0
mul = 1
copy = num
while num>0 :
    digit = num%10
    sum = sum+digit
    mul  =mul * digit
    num = num//10
if sum == mul:
    print(f'{copy} is a Special number')
else:
    print(f'{copy} is not a Special number')
