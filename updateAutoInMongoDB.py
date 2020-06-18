from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def main():
	auto = db.autos.findOne({"designer.firstname":{"$regex": "Fra"}})
	# auto = db.autos.findOne({"designer.firstname":{"$regex": "Fra"}})
	auto["shipDate"] = "2020-06-19"
	db.autos.save(auto)

	if __name__ == '__main__':
		main()