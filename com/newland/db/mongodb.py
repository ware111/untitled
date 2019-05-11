import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['yibai']
names = myclient.list_database_names()
# mycol = db['abc']
# content = {'a':1,'b':2,'c':3}
# mycol.update(content,content)
# mycol.delete_one()
# x = mycol.find_one()
db['abc'].insert({'a':1,'b':2})
db.drop_collection('abc')
print(db['abc'].find_one({'a':1}))



