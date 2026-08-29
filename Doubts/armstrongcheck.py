'''
    153 = 1cube+5cube+3cube = > 153%10=>
    2  = 2pow1=> 2
    1634 = 1pow4+6pow4+3pow4+4pow4=>1634
    1. Read number
    2. count the digits
    3. Separate the digit
    4. Find the Powervalue of the digits
    6. Sum of the powervalues
    7. Compare given number with sum if both are
    equal given num is armstrong or else not an Arm
   
'''
num = int(input('Enter a number : ')) # num = 153
copy = num # copy = 153
sum = 0
count = 0
while num>0 : #  153>0-T 15>0-T 1>0-T 0>0-F
    digit = num%10 # d = 153%10 d = 3 d = 15%10 d  = 5 d = 1%10 d = 1
    count = count+1 # count = 1 count = 2 count = 3
    num = num//10 # num = 153//10 num = 15//10 num = 1//10 num = 0
num  = copy   # num = 153
while num>0 : # 153>0 - T 15>0-T 1>0-T 0>0-F
    digit = num%10 # d = 153 % 10 d = 3 d = 15%10 d = 5 d = 1%10 d = 1
    sum = sum + digit**count # sum = 153
    num = num//10 # num = 153//10 num =15//10 num = 1//10 num = 0
if copy == sum:
    print(f'{copy} is an Armstrong number')
else:
    print(f'copy is not an Armstrong number ')