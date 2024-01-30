import mysql.connector
connect=mysql.connector(host="localhost",port="3306",user="root",password="",database="python_db")
cur=connect.cursor()
qry="select*from users"
cur.execute(qry)
rec=cur.fectchall()
print("total",cur.rowcount())