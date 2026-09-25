class Student:
    def setstudent(self,sid,sname,smarks):
        self.sid = sid
        self.sname = sname
        self.smarks = smarks
    def getstudent(self):
        print(f"Student Id    : {self.sid}")
        print(f"Student Name  : {self.sname}")
        print(f"Student Marks : {self.smarks}")
        
        
s1 = Student() # creation of s1 object
s1.setstudent(123,"Arun",500)
s2 = Student()
s2.setstudent(234,"Ravi",650)
s3 = Student()
s3.setstudent(345,"Chetan",600)
print("Students Information is")
s1.getstudent()
s2.getstudent()
s3.getstudent()