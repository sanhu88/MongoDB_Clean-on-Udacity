from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

tesla_s = {
    "manufacturer" : "Tesla Motors",
    "class" : "full-size",
    "body style" : "5-door liftback",
    "production" : [2012,2013],
    "model years" : [2013],
    "layour" : ["Rear-motor","rear-wheel drive"],
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holehausen"
    }
}

db = client.examples	#database
# db.autos.insert(tesla_s)
db.autos.insert_one(tesla_s)

for a in db.autos.find():
    pprint.pprint(a)