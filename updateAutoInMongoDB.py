from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def main():
	# auto = db.autos.findOne({"designer.firstname":{"$regex": "Fra"}})
	# # auto = db.autos.find_one({"designer.firstname":{"$regex": "Fra"}})
	# auto["shipDate"] = "2020-06-19"
	# db.autos.save(auto)

	# auto = db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"$set" : {"shipDate" : "2020-06-19"}})
	# auto = db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"$unset" : {"shipDate" : ""}})
	# 错误用法 ：#auto = db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"shipDate" : "2020-06-19"})
	y = db.autos.update_many({"designer.firstname":{"$regex" : "Fra"}},{"$set" : {"shipDate" : "2020-06-29"}})
	print(db.autos.find_one())
	
if __name__ == '__main__':
	main()