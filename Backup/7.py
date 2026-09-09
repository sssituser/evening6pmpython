'''
Write a program to find the factorial of a give number
 num = 5       1*2*3*4*5 => fact = 120
'''
# Generate the number 1 2 3 4 5 
# multiply the numbre 1*2*3*4*5
start = 1
num = int(input('Enter a number: ')) # num = 5
fact = 1
while start <= num: # 1<=5-T 2<=5 3<=5 4<=5 5<=5 6<=5
    print(start) # 1 ,2, 3,4,5
    fact = fact * start # fact = 120
    start = start + 1 # start=  2,3,4,5,6
print(f'Factorial of {num} is {fact}')
