import db
from fetch import fetchAllData

con = db.con


def update():
    try:
        print("1.First Name")
        print("2.Last Name")
        print("3.Mobile")
        print("4.Email")
        option = int(input("\nWhich field you want to update?:"))
        if option == 1:
            student_no = int(input("Enter Student Number:"))
            fname = str(input("Enter Your First Name:"))

            while fname == "":
                print("\n")
                print("Please enter your first name")
                # print("\n")
                fname = str(input("Enter Your First Name:"))

            cur = con.cursor()
            sql = "UPDATE students set fname=%s where student_no=%s"
            cur.execute(sql, (fname, student_no))
            con.commit()
            fetchAllData(False)
            print("\n")
            print("Update Successfully")
        elif option == 2:
            student_no = input("Enter Student Number:")
            lname = input("Enter Your Last Name:")

            while lname == "":
                print("\n")
                print("Please enter your last name")
                # print("\n")
                lname = input("Enter Your Last Name:")

            cur = con.cursor()
            sql = "UPDATE students set lname=%s where student_no=%s"
            cur.execute(sql, (lname, student_no))
            con.commit()
            fetchAllData(False)
            print("\n")
            print("Update Successfully")
        elif option == 3:
            student_no = input("Enter Student Number:")
            mobile = input("Enter Your Mobile Number:")

            while mobile.isalpha() or mobile == '':
                print("\n")
                print("Please enter your mobile number")
                # print("\n")
                mobile = input("Enter Your Mobile Number:")

            cur = con.cursor()
            sql = "UPDATE students set mobile=%s where student_no=%s"
            cur.execute(sql, (mobile, student_no))
            con.commit()
            fetchAllData(False)
            print("\n")
            print("Update Successfully")
        elif option == 4:
            student_no = input("Enter Student Number:")
            email = input("Enter E-Mail:")

            while email == "":
                print("\n")
                print("Please enter your email")
                # print("\n")
                email = str(input("Enter E-Mail : "))

            cur = con.cursor()
            sql = "UPDATE students set email=%s where student_no=%s"
            cur.execute(sql, (email, student_no))
            con.commit()
            fetchAllData(False)
            print("\n")
            print("Update Successfully")
        else:
            print("Invalid")

    except:
        print("\n")
        print("Something went wrong")
