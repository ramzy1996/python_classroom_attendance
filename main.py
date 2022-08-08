from attendance import addAttendance
import db
from delete import delete
from fetch import fetchAllData
from insert import insert
from update import update

con = db.con


while True:
    print("\n")
    print("1.Insert Record")
    print("2.Fetch All Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Add Attendance")
    print("6.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    elif choice == 2:
        fetchAllData(False)
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        addAttendance()
    elif choice == 6:
        quit()
    else:
        print("Invalid Option...!!!")
