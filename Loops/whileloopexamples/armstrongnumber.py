'''
num = 153  1cube + 5cube+ 3cube => 153
num = 1634 1pow4+6pow4+3pow4+4pow4 => 1634
1.power value
2.Separate the digit
3.find digitpower and sum
6.compare orinal number
'''
num = int(input('Enter a number : '))
copy = num
count = 0
while num>0:
    digit = num%10
    count = count+1
    num//=10     
num=copy
sum = 0
while num>0: 
    digit =num%10 
    sum = sum + digit**count 
    num = num//10 
if copy==sum:
    print(f'{copy} is Armstrong number')
else:
    print(f'{copy} is not an Armstrong number')
