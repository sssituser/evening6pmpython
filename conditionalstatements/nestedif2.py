age  = int(input('Enter Age : ')) # 18  21 16 40
if age>17: # 18>17-T 21>17-T 16>17-F 40>17
    if(age<21): # 18<21-T 21<21-F 40<21
        print("You can vote but can't marry")
    else:
        print("You can vote and You can marray")
else:
    print("Your can't  vote")
