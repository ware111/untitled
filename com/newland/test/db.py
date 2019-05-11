import mysql.connector as conn
from sys import version

input("输入编号：\n")


c = conn.connect(user='root',password='123')
cur = c.cursor(True)
cur.execute('use a')
cur.execute('select * from a')
# cur.execute('create table abc(id int primary key)')
cur.execute('update a set id=10 where id=1')
c.commit()
# for data in cur.fetchall():
#     print(data)
#     print(cur.rowcount)



