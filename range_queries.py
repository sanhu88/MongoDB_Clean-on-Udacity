from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def find():
	# query = {"population" : {"$gt" : 250000}}
	query = {"model years" : {"$gte" : 2012,"$lte" : 2016}}
	# query = {"model years" : {"$gte" : 2014}}	# 0 is match
	
	# cities = db.cities.find(query)
	autos = db.autos.find(query)

	num_autos = 0
	for c in autos:
		pprint.pprint(c)
		num_autos += 1
	pprint.pprint(f"{num_autos} is match")

if __name__ == '__main__':
    find()
	