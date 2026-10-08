# import mysql.connector as mysql
# con = mysql.connect(host='localhost',user='root',password='root',database='eve6db')
# cur = con.cursor();
# eid = int(input("Enter Employee ID : "))
# ename = input("Enter Employee Name : ")
# esal =int(input('Enter Employee Salary : '))
# cur.execute("insert into tbl_employee values(%s,%s,%s)",(eid,ename,esal))
# con.commit()
# print("Record Inserted Successfully...")

# import mysql.connector as mysql
# con = mysql.connect(host='localhost',user='root',password='root',database='eve6db')
# cur = con.cursor();
# eid = int(input("Enter Employee ID : "))
# ename = input("Enter Employee Name : ")
# esal =int(input('Enter Employee Salary : '))
# cur.execute("update tbl_employee set ename = %s, esal = %s where eid = %s",(ename,esal,eid))
# con.commit()
# print("Record Updated Successfully...")

import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='eve6db')
cur = con.cursor();
eid = int(input("Enter Employee ID : "))
cur.execute("delete from tbl_employee where eid = %s",(eid,))
con.commit()
print("Record Deleted Successfully...")