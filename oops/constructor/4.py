class Employee:
    def __init__(self,eid:int,ename:str,esal:int):
        self.eid = eid
        self.ename = ename
        self.esal =esal
    def getemployee(self):
        print(f'Employee ID     : {self.eid}')
        print(f'Employee Name   : {self.ename}')
        print(f'Employee Salary : {self.esal}')
print("=====================Employe-1 object===============")
emp1 = Employee(111,'kiran',90000)
emp1.getemployee()
print("=====================Employe-2 object===============")
emp2 = Employee(112,'Raj',95000)
emp2.getemployee()

print(emp2.eid)