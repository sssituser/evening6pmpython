'''
Write  a program to read two number and
find the which is number max

'''
num1 = int(input('Enter num1 : ')) # num1 = 5
num2 = int(input('Enter num2 : ')) # num2 = 2
if num1>num2:
    print(f'num1  = {num1} is big')
    
if num2>num1:
    print(f'num2 = {num2} is big')
    
if num1 == num2:
    print(f'{num1} and {num2} are equal')