import db

con = db.con


def delete():
    try:
        student_no = input("Enter Student Number:")
        res = con.cursor()
        sql = "delete from students where student_no=%s"
        res.execute(sql, (student_no))
        con.commit()
        print("\n")
        print("Record Deleted Successfully...!!!")

    except:
        print("\n")
        print("Something went wrong")
