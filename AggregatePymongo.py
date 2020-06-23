#!/usr/bin/python3

from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.runoobdb

def most_tweets():
    result = db.sites.aggregate([
        {"$group" : {"_id" : "$name","count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}}
    ])
    # result = db.sites.aggregate([
    # 	{"$group" : {"_id" : "$name", "num_tutorial" : {"$sum" : 1}}},
    # 	{"$sort" : {"num_tutorial" : -1}}
    # 	])

    # result = db.sites
    return result

if __name__ == '__main__':
	result = most_tweets()
	pprint.pprint(result)