class Student:
    def __init__(self):
        self.__stid = 111
        self.__stname = "ravi"
        self.__marks = 500
    def showstudent(self):
        print(self.__stid)
        print(self.__stname)
        print(self.__marks)
s1 = Student()
s1.showstudent()
print("Student ID :",s1.__stid)
print("Student Name :",s1.__stname)
print("Student ID :",s1.__marks)