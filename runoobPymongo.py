#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

#x = mycol.insert_one(mydict)
# print(x)
# print(x.inserted_id)
y = mycol.update({"name":{"$regex" : "Joe"}},{"$set" : {"shipDate" : "2020-06-18"}},multi = True)
print(y)

# z = mycol.insert_many(mylist)
# print(z.inserted_ids)

mylist_id = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

# inser_with_id = mycol.insert_many(mylist_id)
# print(inser_with_id.inserted_ids)

# for x in mycol.find():
#   print(x)

for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }).limit(3):
  print(x)

myquery = { "name": { "$gt": "H" } }
 
mydoc = mycol.find(myquery).limit(3)
for x in mydoc:
  print(x)


for x in mycol.find({ "name": { "$regex": "^T" } }).limit(3):
  print(x)

newvalues = { "$set": { "alexa": "123" } }
x = mycol.update_many(myquery, newvalues)

print("*****alexa sort :")
for x in mycol.find().sort("alexa", -1):
  print(x)

print("*****multi_delete :")
multi_delete = mycol.delete_many(myquery)
 
print(multi_delete.deleted_count, "个文档已删除")

delete_all = mycol.delete_many({})
 
print(delete_all.deleted_count, "个文档已删除")
mycol.drop()