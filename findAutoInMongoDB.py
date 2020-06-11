from pymongo import MongoClient
import pprint

clinet = MongoClient("mongodb://localhost:27017")

db = clinet.examples

def find():
    query = {"class" : "full-size","manufacturer" : "Tesla Motors"}
    projecttion = {"_id":0}
    autos = db.autos.find(query,projecttion)
    for a in autos:
        pprint.pprint(a)
        
if __name__ == '__main__':
    find()