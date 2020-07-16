import sqlite3


con =sqlite3.connect('MY_company.db')
cObj = con.cursor()


cObj.execute("CREATE TABLE if not exists employeeee(id INTEGER PRIMARY KEY,name TEXT,salary REAL ,department TEXT,position TEXT)")
con.commit()

def insert_value(id,name,salary,department,position):
    cObj.execute("INSERT INTO employeeee VALUES(?,?,?,?,?)",(id,name,salary,department,position))
    con.commit()


def Update_department(department,id):
    cObj.execute("update employeeee set department = ?where id = ?",(department,id))
    con.commit()

def sql_fetchall():
    Obj.execute("select * from employeeee")
    result = cObj.fetchall()
    print(result)

def DELETE_all():
    cObj.execute("DELETE FROM employeeee")
    cObj.commit()


insert_value(4,"vidw",4559,"web","developer")
#cObj.execute("select * from employeeee")
#result = cObj.fetchall()
#print(result)
#cObj.execute("DELETE FROM employeeee")
#cObj.commit()



con.close()
#cObj.close()
