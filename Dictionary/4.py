students={}
print(len(students))
while True:
    ch = int(input('1.Add\n2.Delete\n3.Update\n4.Find\n5.Find All\nEnter ur chocie :'))
    match ch:
        case 1:
            key = int(input('Enter ID : '))
            val =  input("Enter Name : ")
             # students[key] = val
            students.setdefault(key,val)
        case 2:
         if len(students)==0:
            print("Dictonary is Empty")
         else:
             key = int(input("Enter Key : "))
             students.__delitem__(key)
             print("Iteme Deleted....")
        case 3:
            if len(students)==0:
                print("No Students in the Dictonary")
            else:
                key = int(input('Enter ID : '))
                val =  input("Enter Name : ")
                students[key]=val
                print("Student UPdated")
        case 4:
            
            if(len(students)==0):
                print("Students Not Available")
            else:
               key = int(input('Enter ID : '))
               if(students.__contains__(key)):
                   print(f"{key}  {students[key]}")
               else:
                   print("No Student Available with the given key")
        
        case 5:
            if len(students)==0:
                print("No Students Available")
            else:
                for k in  students.items():
                    print(k)
        case __ :
            print("Invalid choice...")    
    
        