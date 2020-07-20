#!/usr/bin/env python
"""
Use an aggregation query to answer the following question. 

Which Region in India has the largest number of cities with longitude between
75 and 80?

Please modify only the 'make_pipeline' function so that it creates and returns
an aggregation pipeline that can be passed to the MongoDB aggregate function.
As in our examples in this lesson, the aggregation pipeline should be a list of
one or more dictionary objects. Please review the lesson examples if you are
unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you
want to run this code locally on your machine, you have to install MongoDB,
download and insert the dataset. For instructions related to MongoDB setup and
datasets please see Course Materials.

Please note that the dataset you are using here is a different version of the
cities collection provided in the course materials. If you attempt some of the
same queries that we look at in the problem set, your results may be different.

请使用聚合查询回答以下问题。

印度的经度在 75 到 80 之间的地区中，哪个地区包含的城市数量最多？

只需修改“make_pipeline”函数，使其创建并返回一个聚合管道，
该管道可以传递到 MongoDB 聚合函数中。
和这节课中的示例一样，聚合管道应该是一个包含一个或多个字典对象的列表。
如果不熟悉语法，请参阅这节课中的示例。

你的代码将根据我们提供的 MongoDB 实例运行。如果你想在本地机器上运行代码，
你需要安装 MongoDB 并下载和插入数据集。要了解 MongoDB 设置和数据集方面的说明，请参阅课程资料。

请注意，你在此处使用的数据集与课程资料中提供的城市集合版本不同。
如果你尝试运行我们在习题集中运行过的同一查询，结果可能不同。

提示：如果你必须在一个字段匹配多个要求，你需要把所有条件放入同一个词典，例如：

{"$match": {'field': {'$cond1': val1, '$cond2': val2} ... }}
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ 
     {"$match" : {"country" : "India"}},
         {"$unwind" : "$isPartOf"},
          {"$match" : {"lon" :{"$gte" : 70, "$lte" : 80}}},
        
        {"$group" : {"_id" : "$isPartOf" , 
                     "count" : {"$sum" : 1}
                     }},
        {"$sort" : {"count" : -1}},
        {"$limit" : 1}
    ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result[0])
    assert len(result) == 1
    assert result[0]["_id"] == 'Tamil Nadu'
    assert result[0]["count"] == 424
