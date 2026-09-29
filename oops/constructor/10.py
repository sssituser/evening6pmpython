class Employee:
    def __init__(self,id,name,sal):
        self.eid = id
        self.ename = name
        self.esal = sal
        
    def getEmployee(self):
        print(f'Employee ID : {self.eid}')
        print(f'Employee Name : {self.ename}')
        print(f'Employee Salary : {self.esal}')
        
emp1 = Employee(111,"Ravi",6000)
emp1.ename = "sirisha"
print(f'Employee ID : {emp1.eid}')
print(f'Employee Name : {emp1.ename}')
print(f'Salary : {emp1.esal}')


        
        
    