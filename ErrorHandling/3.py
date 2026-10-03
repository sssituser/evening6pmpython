class InvalidAgeException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        print("Invalid Age Exception...") 
              
while True:
    try:
        age = int(input('Enter Age : '))
        if age<0 or age>=150:
            raise InvalidAgeException("Hi Iam In If block since age is Invalid")
        
        print("Entered Age is Valid.....")
    except InvalidAgeException as ix:
        
        print(f"Age Must be >=0 and <150 : {ix} ....")
    except ValueError:
        print("Enter Only Numbers with out decimals values")