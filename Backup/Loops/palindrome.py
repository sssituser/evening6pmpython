num = int(input('Enter a number : ')) # num = 456
rev = 0  # rev = 0
copy = num # copy = 456
while num!=0: # 456! = 0  45!=0  4!=0 0!=0 -F
    digit = num%10 # digit = 456%10 digit = 6 d = 4%10 d = 4
    rev = rev*10+digit # rev = 654
    num=num//10 # num = 456//10 num = 45//10 num = 4//10 num = 0
if copy==rev:
    print(f'num = {copy} reverse = {rev} is a Palindrome numbr')
else:
    print(f'reverse = {rev} num = {copy}  is not a Palidrome number ')