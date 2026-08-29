'''
Write aa program to check given number is strong or not
num = 145   1!+4!+5! => 1+24+120 => 145 
'''
num = int(input('Enter a number : '))
sum = 0
copy = num
while num>0: # num = 145>0-T 14>0-T 1>0 0>0
    digit = num%10 # digit = 5 digit = 4 digit = 1
    start = 1
    fact = 1
    while start<=digit:
        fact = fact * start
        start = start+1
    sum = sum + fact
    num = num//10 # num = 145//10 num = 14//10 num = 1//10 num = 0
if copy == sum:
    print(f'{copy} is a strong number')
else:
    print(f'{copy} is not a strong number')