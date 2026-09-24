class Employee:
    empid:int
    empname:str
    empsal:float
    def show():
        print('hi this is show method from employee clss')
    def display():
        print("hi  this is display method from employee class")
        
Employee.empid = 111
Employee.empname = "kiran"
Employee.empsal = 50000
Employee.show()
Employee.display()
print(Employee.empid,Employee.empname,Employee.empsal)