'''
Write a program to separate the digits of given number
num = 321      1  2  3
num= 456       6  5  4
'''
num = int(input('Enter num : ')) # num = 345
while num!=0: # 345 != 0 34!=0 3!= 0 0!=0
    digit = num%10 # digit = 345%10 digit=5 digit = 3%10
    print(digit,end=" ")
    num = num//10 # num = 345//10 num = 34//10 num = 3//10 num = 0