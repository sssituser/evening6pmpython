
'''
Write a program to find the sum of n numbers
num = 5         1 +2 +3+ 4+ 5 => sum = 15
'''
start = 1
sum = 0
num = int(input('Ener num : ')) # num = 5
while start <= num: # 1<=5-T 2<=5 3<=5 4<=5 5<=5 6<=5
    # print(start) # 1  2 3
    sum = sum + start # sum = 15
    start = start+1 # start = 2,3,4 ,5,6
print(f'Sum of {num} number is : {sum}')