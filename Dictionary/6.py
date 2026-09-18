employees = dict()
while True:
    choice = int(input("1.Add\n2.Delete\n3.Show\n4.No of elements\n5.Find\nEnter your choice : "))
    match choice:
        case 1:
            key = int(input('Enter Key(Employee ID) : '))
            val = input('Enter Value (Employee Name): ')
            employees.setdefault(key,val)
            print('Employee Id and Name added Successfully..')
        case 2:
            if employees.__len__()==0:
                print("No Employees to delete")
            else:
               key = int(input('Enter Employee ID : '))
               if employees.__contains__(key):
                   print(f'Deleted Employee is : {employees.pop(key)}')
               else:
                   print(f"Employee is Not available with given id : {key}")
        case 3:
            if len(employees)==0:
                print("No Employees to display")
            else:
                print("==Employees Information===")
                for kvp in employees.items():
                    print(kvp)
        case 4:
            print(f"No Employees In the Company : {len(employees)}")
        case 5:
            if len(employees)==0:
                print("No Employees in the company")
            else:
                key  =int(input('Enter Employee Id : '))
                if employees.__contains__(key):
                    print(f'Employee Id : {key} Employee Name : {employees[key]}')
                else:
                    print(f"Employee is not availabe with the given : {key}")
        case _:
            print("Invalid choice...") 