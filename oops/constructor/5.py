class Student:
    def __init__(self,id,name):
        self.eid = id
        self.ename = name
    def getstudent(self):
        print("Hi Iam displying student id  and name with get methdo")
        print(f'Student ID :{self.eid}\tStudent Name : {self.ename}')
s1 = Student(1,'kiran')     
print(f'Student ID :{s1.eid} Name : {s1.ename}')