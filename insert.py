import db

con = db.con


def insert():
    try:
        fname = str(input("Enter First Name: "))
        while fname == "":
            print("\n")
            print("Please enter your first name")
            # print("\n")
            fname = str(input("Enter First Name: "))

        lname = str(input("Enter Last Name: "))
        while lname == "":
            print("\n")
            print("Please enter your last name")
            # print("\n")
            lname = str(input("Enter Last Name: "))

        mobile = input("Enter Mobile Number : ")
        while mobile.isalpha() or mobile == '':
            print("\n")
            print("Please enter your mobile number")
            # print("\n")
            mobile = input("Enter Mobile Number : ")

        email = str(input("Enter E-Mail : "))
        while email == "":
            print("\n")
            print("Please enter your email")
            # print("\n")
            email = str(input("Enter E-Mail : "))

        res = con.cursor()
        sql = "insert into students (fname,lname,mobile,email) values (%s,%s,%s,%s)"
        res.execute(sql, (fname, lname, mobile, email))
        con.commit()
        print("\n")
        print("Record Insert Successfully")
    except:
        print("\n")
        print("Something went wrong")
