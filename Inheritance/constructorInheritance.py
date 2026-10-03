class Dept:
   def __init__(self,deptid,deptname,depthead,deptloc):
        self.deptid = deptid
        self.depname = deptname
        self.depthead = depthead
        self.deptloc = deptloc
   def showdept(self):
       print(f'Dept ID   : {self.deptid}')
       print(f'Dept Name : {self.depname}')
       print(f'Dept Head : {self.depthead}')
       print(f'Dept Location : {self.deptloc} ')
class Employee(Dept):
   def __init__(self, deptid, deptname, depthead, deptloc,empid,empname,empsal):
       super().__init__(deptid, deptname, depthead, deptloc)
       self.empid = empid
       self.empname = empname
       self.empsal = empsal
   def showemployee(self):
       print(f'Employee Id     : {self.empid}')
       print(f'Employee Name   : {self.empname}')
       print(f'Employee Salary : {self.empsal}')
    
emp = Employee(12,"HR","Ravi","Hyd",111,"Raj",80000)
emp.showemployee()
emp.showdept()
