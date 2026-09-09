'''
Write a program to generate number from 1 given number
num = 10
1,3,5,7,9,   
num = 20
1, 3 5 7 9 11 13 15 17 19 

'''
start = 1
num = int(input('Enter a value : ')) # num = 10

while start <=   num: # 3<= 10 -T 5<=10-T 7<=10 9<=10 11<=10
    print(start) # 1 3 5 7 9
    start = start+2 # start = 3,5,7 9 11