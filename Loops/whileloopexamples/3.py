'''
Write a program to generate number from 3 to the given number of muliples of
3.

input : 27    ouput: 3 6 9 12 15 18 21 24 27
'''
start = 3
end = int(input('Enter a  number : '))
while start <=  end:
    print(start,end=" ")
    start += 3