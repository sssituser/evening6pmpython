class Employee:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def getemployee(self):
        return f'Employee ID: {self.eid}\nEmployee Name: {self.ename}\nEmployee Salary: {self.esal}\n'


emp1 = Employee(111, 'abc', 60000)
fname = input('Enter File Name : ')
file = open(fname, 'w+')
file.write(emp1.getemployee())
print("Data written successfully!")
file.close()