import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='eve6db')
cur = con.cursor()
cur.execute("select * from tbl_employee")
employees = cur.fetchall()
print("EmpId\tEmpName\tEmpSal")
for emp in employees:
    print(f'{emp}')
