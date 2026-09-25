class Employee:
    def setemployee(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID     : {self.eid}')
        print(f'Employee Name   : {self.ename}')
        print(f'Employee Salary : {self.esal}')
        
print("================Employee-1 Object==============")
emp1 = Employee()
emp1.setemployee(111,'kiran',50000)
emp1.getemployee()

print("================Employee-2 Object==============")
emp2 = Employee()
emp2.setemployee(112,'Raj',70000)
emp2.getemployee()

print("================Employee-3 Object==============")
emp3 = Employee()
emp3.setemployee(113,'Ram',70000)
emp3.getemployee()
print("==========================Employoees=============")
emp1.getemployee()
emp2.getemployee()
emp3.getemployee()