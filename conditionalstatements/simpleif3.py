'''
Write a program to read three subjects marks of a student and
check the result.
'''
sub1 = int(input('Enter Subject - 1 Marks : ')) # sub1 = 30
sub2 = int(input('Enter Subject - 2 Marks : ')) # sub2 = 90
sub3 = int(input('Enter Subject - 3 Marks : ')) # sub3 = 90
if sub1>34 and sub2>34 and sub3>34:
    print('He Got Passed in the Exam')
    
if sub1<35 or sub2<35 or sub3<35:
    print("Student got Failed")
    
    
