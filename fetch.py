from tabulate import tabulate
import db

con = db.con


def fetchAllData():
    res = con.cursor()
    sql = "SELECT * from students"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    # if(dt == True):
    #     print("Attendance Of ", res.rowcount, " Students")

    print(tabulate(result, headers=[
          "STUDENT NO", "FIRST NAME", "LAST NAME", "MOBILE", "EMAIL"]))
