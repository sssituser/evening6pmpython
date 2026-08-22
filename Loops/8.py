
start = 1
num = int(input('Enter number : ')) # num = 5
sum = 0
while start<=num: # 1<=5-T 2<=5-T 3<=5-T 4<=5-T 5<=5-T 6<=5-F
    print(start,end=" ") # 1 2 3 4 
    sum = sum + start # sum = 1 sum = 3 sum = 6 sum = 10 sum = 15
    start = start+1 # start = 2 start = 3 start = 4 start = 5 start = 6
print(f'Sum of the above number {sum}')