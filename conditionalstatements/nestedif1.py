'''
Write program to check the given number is +ve and single digit

'''
num = int(input('Enter a number : ')) # 500  9 -5  10

if num>0: # 500>0-T 9>0 T -5>0-F 10>0-T
    if num<10: # 500<10-F  9<10-T 10<10-F
        print(f'{num} is +ve and single digit')
    else:
        print(f'{num} is +ve but not a single digit')
else:
    print(f'given num may be -ve or zero ')
    