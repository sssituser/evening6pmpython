
start = 1
num = int(input('Enter a nuber : ')) # num = 0
fact = 1
while start<=num: # 1<=3 -T 2<=3-T 3<=3 4<=3-F
    print(start,end=" ") # 1 2 3
    fact =fact * start # fact = 1 fact = 2 fact = 6
    start += 1 # start = 2 start = 3 start = 4
print(f'factorial of {num} is {fact}')