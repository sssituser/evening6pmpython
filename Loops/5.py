'''
Write a program to generate number from the given number to 1

input : 5       output : 5 4 3 2 1
input : 10      output : 10 9 8 7 6 5 4 3 2 1
-------------------------------------------------------
input : 20        output : 20 18 16 14 12 10 8 6 4 2
--------------------------------------------------------
input : 33        output : 33 30 27 24 21 18 15 12 9 6 3
---------------------------------------------------------

'''

start = int(input('Enter a number : '))
end = 1

while start >= end:
    print(start,end=" ")
    start -= 1 