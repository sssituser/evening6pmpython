import mysql.connector as mysql
con = mysql.connect(host="localhost",user="root",password='root',database='eve6db')
cur = con.cursor();
def checkrecords():
    cur.execute("select * from tbl_Employee")
    recs= cur.fetchall()
    if recs:
        return True
    else:
        return False
def checkrecord(id):
    cur.execute("select * from tbl_Employee where eid = %s",(id,))
    rec= cur.fetchone()
    if rec:
        return True
    else:
        return False
    
while True:
    con = mysql.connect(host="localhost",user="root",password='root',database='eve6db')
    cur = con.cursor();
    choice = int(input("1.Add\n2.Delete\n3.Update\n4.FindAll\n5.Find\nEnter Your choice : "))
    match choice:
        case 1:
            eid = int(input('Enter Employee Id : '))
            ename = input('Enter Employee Name : ')
            esal = int(input("Enter Employee Salary : "))
            cur.execute("insert into tbl_employee values(%s,%s,%s)",(eid,ename,esal))
            con.commit()
            con.close()
        case 2:
           if(checkrecords()):
               
                eid = int(input('Enter Employee Id : '))
                if(checkrecord(eid)):
                    cur.execute("delete from tbl_employee where eid = %s",(eid,))
                    con.commit()
                    con.close()
                    print("Record Deleted Successfully")
                else:
                    print(f'{eid} Record Not Present')
           else:
               print("Records not found to Delete")
        case 3:
            if(checkrecords()):
                eid = int(input('Enter Employee Id : '))
                if(checkrecord(eid)):
                    ename = input('Enter Employee Name : ')
                    esal = int(input("Enter Employee Salary : "))
                    cur.execute("update tbl_employee set ename = %s,esal = %s where eid = %s",(ename,esal,eid))
                    con.commit()
                    con.close()
                    print("Record Updated Sucessfully")
                else:
                    print(f'{eid} Record is not Available to update')
            else:
                print("No Records Available to update")
        case 4:
            cur.execute("select * from tbl_employee")
            recs = cur.fetchall()
            if recs:
                print("EmpId\tEmpName\tEmpSal")
                for rec in recs:
                    print(rec)    
            else:
                print("Records not found")
            con.close()
        case 5:
            if checkrecords():
                eid = int(input('Enter Employee Id : '))
                cur.execute("select * from tbl_employee where eid = %s",(eid,))
                rec = cur.fetchone()
                if rec:
                    print(rec)
                else:
                    print("Record Not Found With The Given Id ")
            else:
                print("Records Not Available")
                