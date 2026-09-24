class Employee:
    cname : str
    def setemployee(self,eid,ename,esal,comname):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        Employee.cname = comname
    def getemployee(self):
        print(f'Employee ID  : {self.eid}')
        print(f'Employee Name: {self.ename}')
        print(f'Employee Sal : {self.esal}')
        print(f'Company Name : {Employee.cname}')

emp1 = Employee()
emp1.setemployee(111,"Raj",50000,"SSSIT")
emp1.getemployee()

emp2 = Employee()
emp2.setemployee(112,"Jeswanth",60000,"Wipro")
emp2.getemployee()

emp3 = Employee()
emp3.setemployee(113,"Kiran",80000,"TCS")
emp3.getemployee()


