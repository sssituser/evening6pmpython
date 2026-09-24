'''
Types of Variables :
        college:str  class variable or static varibles
        sid,sname,smarks,college are local variables
        ======non static variables or Instance variables========
        self.sid
        self.sname
        self.smark 
        =================static methods============
        setstudent() method declared with self keyword hence it is called
        as static method
        getstudent() is non static method(Instance method)
    static members can be accessed using classname
    non static members can be accessed using object      
'''
class Student:
    college:str  # static variable or class variable
    def setstudent(self,sid,sname,smarks,college): # sid, sname, smarks local variables
        self.sid = sid # self.sid is non static variable or Instance variable
        self.sname = sname # self.sname is a non static variable or Instance variable
        self.smarks = smarks # self.smarks is a non static variable or """"""
        Student.college = college
        print("Data Assigned")
        
    def getstudent(self):# getstudent is a non static method(Instance methodd)
        print(f'Student Id    : {self.sid}')
        print(f'Student Name  : {self.sname}')
        print(f'Student Marks : {self.smarks}')
        print(f'College Name  : {Student.college}')
        
#Student.setstudent(111,'abc',600,"Loyola")     
s1 = Student()
s1.setstudent(111,'kiran',6000,'Naryana') 
s1.getstudent()  