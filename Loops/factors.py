num = int(input('Enter a number : '))
start = 1
end = num

while start <= end:
    if num%start == 0:
        print(start)
    start = start+1
