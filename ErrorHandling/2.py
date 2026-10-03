while True:
    try:
        num1 = int(input('Enter num1 : '))
        num2 = int(input('Enter num2 : '))
        if num2==0: #0==0 3==0-F
            raise ZeroDivisionError("Hi  Iam In If block since num2 is zero")
        print(f'Quo is : {num1/num2}')
        
    except ValueError : # individual Except block
        print("Enter only Integers")
        
    except ZeroDivisionError as zx: # Indivi
        print(f"num2 can't be zero : {zx}")
        
    except Exception as ex: # common except
        print(f'Error occured : {ex}')
        
    finally:
        print(f'Thank You Visit Again.....')