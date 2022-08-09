from tabulate import tabulate
import db
from fetch import fetchAllData

con = db.con


def selectedStudentAttendance():
    fetchAllData()
    print("\n")
    student_no = input("Enter Student Number:")
    res = con.cursor()
    sql = "SELECT attendance.date, attendance.attendance from attendance join students on students.student_no = attendance.student_no where students.student_no = "+student_no+""
    res.execute(sql)
    result = res.fetchall()
    if res.rowcount > 0:
        res1 = con.cursor()
        sql1 = "SELECT fname, lname, mobile,email from students where student_no = "+student_no+""
        res1.execute(sql1)
        result1 = res1.fetchall()
        print("\n")
        print("First Name    -> ", result1[0][0])
        print("Last Name     -> ", result1[0][1])
        print("Mobile Number -> ", result1[0][2])
        print("Email         -> ", result1[0][3])
        print("\n")
        print(tabulate(result, headers=[
            "DATE", "ATTENDANCE"]))
    else:
        print("Please select a valid student number..")
