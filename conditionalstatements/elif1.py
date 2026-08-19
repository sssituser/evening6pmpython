num1 = int(input('Enter num1 :')) # 10 30 100
num2 = int(input('Enter num2 :')) # 20 15 100

if num1>num2: #10>20-F   30>15 100>100 -F
    print(f'{num1} is max') # 30 is max
elif num2>num1: # 20>10-T  100>100-F
    print(f'{num2} is max') #  20 is max
else:
    print('Both are equal')
