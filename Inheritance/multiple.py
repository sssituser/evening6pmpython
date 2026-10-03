class A:
    def getnums(self):
        self.num1 = int(input('Enter num1 : '))
        self.num2 = int(input('Enter num2 : '))
    def shownums(self):
        print(f'num1 : {self.num1}   num2 :{self.num2}')
        
class B:
    def readinfo(self):
        self.eid =int(input('Enter Employee ID : '))
        self.ename = input('Enter Name : ')
        self.esal = int(input('Enter Salary'))
    def showinfo(self):
        print("===Employee Details===")
        print(f'Employee Id : {self.eid}\nEmployeeName : {self.ename}\nSalary :{self.esal}')
class C:
    def readstu(self):
        self.sid = int(input("Enter Student ID : "))
        self.sname = input("Enter Student Name : ")
        self.marks = int(input('Enter Marks : '))
    def showstu(self):
        print(f'Student Id : {self.sid}\tStudent Name : {self.sname}\tStudent Marks : {self.marks}')
class D(A,B,C):
    def sum(self):
        print(f'Sum is : {self.num1+self.num2}')
    def sub(self):
        print(f'Sub is : {self.num1-self.num2}')
res = D()
res.getnums()
res.shownums()
res.readinfo()
res.showinfo()
res.readstu()
res.showstu()
res.sum()
res.sub()

        