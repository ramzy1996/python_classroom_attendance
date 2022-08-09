from tabulate import tabulate
import db

con = db.con


def viewAllStudentsAttendance():
    res = con.cursor()
    sql = "SELECT attendance.date, students.student_no, students.fname, students.lname, attendance.attendance from attendance inner join students on students.student_no = attendance.student_no"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=[
        "DATE", "STUDENT NO", "FIRST NAME", "LAST NAME", "ATTENDANCE"]))
