from sqlobject import *
import mysql.connector

class Users(SQLObject):
    name=StringCol()
    age=IntCol()

class SQLObjectTest(object):
    cxn = 1
    def __int__(self):
        cxn = connectionForURI('mysql://root:123@localhost:3306/a')
        self.cxn = sqlhub.processConnection = cxn
        print(1)

    def insert(self):
        Users(name='John',age=13)

cxn = connectionForURI('mysql://root:123@localhost:3306/a')
sqlhub.processConnection = cxn

Users.createTable()
# sqls.insert()