from tabulate import tabulate
import db
from fetch import fetchAllData

con = db.con


def addAttendance():
    # fetchAllData()
    try:
        # while True:
        res = con.cursor()
        sql = "select student_no,fname from students"
        res.execute(sql)
        result = res.fetchall()

        while True:
            print("Attendance Of ", res.rowcount, " Students y/n? ", end=' ')
            gonext = input()
            fetchAllData()
            print('\n')
            if gonext == 'y' or gonext == 'Y':
                # print(result[0][0])
                date = input("Please enter the date of attendance: ")
                # print(res.rowcount)

                print("Student Attendance Yes/No")
                i = 0
                while i < res.rowcount:
                    print(result[i][1], end=" ")
                    atd = input()
                    res1 = con.cursor()
                    sql1 = "insert into attendance (student_no,date,attendance) values (%s,%s,%s)"
                    res1.execute(sql1, (result[i][0], date, atd))
                    con.commit()
                    i += 1
                print("\n")
                print("Attendance Addedd Successfully")
                break
            elif gonext == 'n':
                break
            else:
                continue

    except:
        print("\n")
        print("Something went wrong")
