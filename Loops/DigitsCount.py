num = int(input('Enter a number : ')) # num = 145
count = 0
while num>0: # 145>0-T 14>0-T 1>0-T 0>0-F
    digit = num%10
    count = count+1 # count = 1  count = 2 count = 3
    num=num//10 # num = 145//10 num = 14//10 num = 1//10 num = 0
print(f"Digits present in the give number is : {count}")
