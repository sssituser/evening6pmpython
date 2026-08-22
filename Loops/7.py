'''
num = 5   gen = 1 2 3 4 5
'''

start = 1
num = int(input('Enter a number : ')) # 5
while start  <=  num: # 1<= 5 - T 2<=5-T 3<=5 4<=5-T 5<=5-T 6<=5 -F
    print(start,end=" ") # 1 2 3 4 5
    start =start+ 1 # start = 2 start = 3 start = 4 start = 5 start = 6