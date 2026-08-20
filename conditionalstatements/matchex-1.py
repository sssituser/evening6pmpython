num1 = int(input('Enter num1 : ')) # num1 = 5
num2 = int(input('Enter num2 : ')) # num2 = 2


choice = int(input("1.Add 2.Sub 3.Mul 4.Div 5.FloorDiv 6.Rem  7.Expo Enter Your choice : "))
match choice:
    case 1:
        print(f'Sum is :{num1+num2}')
    case 2:
        print(f'Sub is :{num1-num2}')
    case 3:
        print(f'Mul is :{num1*num2}')
    case 4:
        print(f'Quo is :{num1/num2}')
    case 5:
        print(f'Floor Div is :{num1//num2}')
    case 6:
        print(f'Rem is :{num1%num2}')
    case 7:
        print(f'{num1} to the power {num2} : {num1**num2}')
    case _:
        print("Invalid Choice...Enter Choice 1,2,3,4,5,6,7")