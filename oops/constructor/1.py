class Employee:
    def __init__(self):
        print("Hi Iam Constuctor without parameters")
        self.eid = 111
        self.ename = "kiran"
        self.esal =  50000
    def getemployee(self):
        print(f'Employee ID : {self.eid}\tEmployee Name : {self.ename}\tSalary : {self.esal}')
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
emp1.getemployee()
emp2.getemployee()
emp3.getemployee()
