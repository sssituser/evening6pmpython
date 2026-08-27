num = int(input('Enter a number : ')) # num = 8 
start = 1
end = num
count = 0
while start<=end:
    if num%start == 0:
       count = count+1
    start = start+1
print(f'{num} has  {count} factors')  
 