from sqlalchemy import Column, Integer, String, create_engine, exc, orm, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
import sys
from os.path import dirname
import mysql.connector
import mysql.connector


Base = declarative_base()
metadata = MetaData()
user = Table('a',metadata,Column('id', Integer, primary_key=True, autoincrement=True),Column('name',String(20)));

class Users(Base):
    # def __init__(self, name):
    #     self.name = name

    __tablename__ = 'a'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)

    def display(self):
        print('%s'%(self.id))
    # def __str__(self):
    #     s = lambda s: str(s)
    #     return ''.join(map(s, (self.name,self,id)))
# mapper(Users,user)
a = create_engine('mysql+pymysql://root:123@localhost:3306/a')
conn = a.connect()

users = user.update(values={'name':'jim'})
conn.execute(users)

# Session = orm.sessionmaker(bind=eng)
# session = Session()
# session.add(Users('tom'))
# session.commit()
# user = session.query(Users).order_by().all()
# user.id = 12
# session.delete(user)
# session.commit()
# session.close()

# a = 1
# b=2
# c=3
# print(''.join(map(lambda s:str(s),(str(1),str(2),str(3)))))