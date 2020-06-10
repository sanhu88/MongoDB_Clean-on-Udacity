from pymongo import MongoClient
import pprint

clinet = MongoClient("mongodb://localhost:27017")

db = clinet.examples

def find():
    autos = db.autos.find({"class" : "full-size"})
    for a in autos:
        pprint.pprint(a)
        
if __name__ == '__main__':
    find()