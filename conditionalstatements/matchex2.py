choice = input("IIT  NEET  CLAT Enter Your choice : ")
match choice:
    case "IIT":
        print('You have choosen Eng.')
    case "NEET":
        print('You have Choosen Med.')
    case "CLAT":
        print('You have choosen LLB.')
    case _:
        print("Invalid choice : ")
