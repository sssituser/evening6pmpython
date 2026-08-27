'''
Create a Console application which reads a number, 
and generates the number from 1 to given number ?

Example : input :5     Ans: 1 2 3 4 5
          input :10    Ans: 1 2 3 4 5 6 7 8 9 10
'''
num = int(input('Enter num : '))# num = 5
start = 1
end = num

while start <= end :#1<=5 - T 2<=5-T 3<=5-T 4<=5 5<=5-T 6<=5-F
    print(start) # 1 2 3 4 5
    start = start+1 # start = 2 start = 3 start = 4 start  = 5 start = 6