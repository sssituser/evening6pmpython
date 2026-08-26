num = int(input('Enter a number : ')) # num = 8
start = 1
end = num # end = 8
while start <= end: # 1<=8-T 2<=8-T 3<=8-T 4<=8-F 5<=8 6<=8 7<= 8<=8-T 9<=8-F
    if num%start == 0: #  8%5==0  3==0-F  8%6==0 2==0-F 8%7==0  1==0-F 8%8==0 0==0-F
        print(start,end="\t") # 1 2 4 8
    start = start+1 # start = 2 start = 3 start = 4 start = 5 start = 6 start = 9
