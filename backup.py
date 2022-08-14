from attendance import addAttendance
import db
from delete import delete
from fetch import fetchAllData
from insert import insert
from student_attendance import selectedStudentAttendance
from update import update
from view_attendance import viewAllStudentsAttendance

con = db.con


while True:
    print("\n")
    print("1.Insert Student")
    print("2.Fetch All Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Add Attendance")
    print("6.View Students Attendance")
    print("7.View Attendance By Student")
    print("8.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    elif choice == 2:
        fetchAllData()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        addAttendance()
    elif choice == 6:
        viewAllStudentsAttendance()
    elif choice == 7:
        selectedStudentAttendance()
    elif choice == 8:
        quit()
    else:
        print("Invalid Option...!!!")
