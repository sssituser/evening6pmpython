'''
Write a program to find the max number among three number
'''
num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
num3 = int(input('Enter num3 : '))

max = num1
if max<num2:
    max = num2
if max<num3:
    max = num3

print(f'{max} is max')
