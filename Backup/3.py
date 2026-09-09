'''
Write a program to generate number from 
2 to given number
num = 10       2 4 6 8 10
num = 20       2 4 6 8 10 12 14 16 18  20
'''
start = 2
num = int(input('Enter a value : '))# num = 6
while start<=num:# 2<=6-T 4<=6-T 6<=6-T 8<=6-F
    print(start,end=" ") # 2 4 6
    start = start+2# start = 4,6,8