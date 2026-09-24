class StudentResult:# Pascal Case naming convention 
    stid:int
    stuname:str
    studentmarks:int
    def setdata():
        StudentResult.stid = 111
        StudentResult.stuname = "raj"
        StudentResult.studentmarks=500
        print("Student Data Assigned")
    def showdata():
        print(f'Student Id : {StudentResult.stid}')
        print(f'Student Name : {StudentResult.stuname}')
        print(f'Student Marks : {StudentResult.studentmarks}')

StudentResult.setdata()
StudentResult.showdata()        