'''
Write a program to encrypt the given string;
input : abc   Result : zyx     
input : xyz   Result :  cba
'''
s = input('Enter a string : ') # s = abc
res = ''
alpha = "abcdefghijklmnopqrstuvwxyz"
ralph = "zyxwvutsrqponmlkjihgfedcba"
for ch in s:
    res +=ralph[alpha.index(ch)]
print(f'Encrypted String is : {res}')

