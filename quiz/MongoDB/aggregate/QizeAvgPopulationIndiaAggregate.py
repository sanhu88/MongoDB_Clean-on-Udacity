#!/usr/bin/env python
"""
In an earlier exercise we looked at the cities dataset and asked which region in India contains 
the most cities. In this exercise, we'd like you to answer a related question regarding regions in 
India. What is the average city population for a region in India? Calculate your answer by first 
finding the average population of cities in each region and then by calculating the average of the 
regional averages.

Hint: If you want to accumulate using values from all input documents to a group stage, you may use 
a constant as the value of the "_id" field. For example, 
    { "$group" : {"_id" : "India Regional City Population Average",
      ... }

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used 
in examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results will be different.

在上一道练习中，我们查看了城市数据集，并询问印度的哪个地区包含的城市最多。在这道练习中，我们想请你回答另一个关于印度地区的相关问题。印度各个地区的平均人口数量是多少？你需要首先计算每个地区城市的平均人口数量，然后计算地区的平均人口数量。

提示：如果你想使用所有输入文档中的值汇集到一个群组阶段中，可以使用常量作为“_id”字段的值。例如：
{ "$group" : {"_id" : "India Regional City Population Average", ... }
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match" : {"country" : "India"}},
    {"$group" : {"_id" : "$name", "cities" : {"$addToSet" : "$isPartOf"}}},
    #{"$project" : {"_id" : "$name","population" : "$population","city":"$isPartOf"}},
    {"$limit" : 1}
    ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    assert abs(result[0]["avg"] - 201128.0241546919) < 10 ** -8
    import pprint
    pprint.pprint(result)
