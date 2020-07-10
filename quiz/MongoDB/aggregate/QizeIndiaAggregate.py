#!/usr/bin/env python
"""
For this exercise, let's return to our cities infobox dataset. The question we would like you to answer
is as follows:  Which region or district in India contains the most cities? (Make sure that the count of
cities is stored in a field named 'count'; see the assertions at the end of the script.)

As a starting point, use the solution for the example question we looked at -- "Who includes the most
user mentions in their tweets?"

One thing to note about the cities data is that the "isPartOf" field contains an array of regions or 
districts in which a given city is found. See the example document in Instructor Comments below.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline 
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, the aggregation 
pipeline should be a list of one or more dictionary objects. Please review the lesson examples if you 
are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the cities collection used in 
examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results may be different.

对于这道练习，我们回到城市 infobox 数据集。我们希望你能回答以下问题：印度的哪个地区包括的城市最多？
（确保将城市计数存储在叫做“count”的字段中；请参阅脚本末尾的声明。）

首先，使用我们提出的以下示例问题的答案：谁在推特中提到的用户数最多？

对于城市数据，需要注意的一点是：“isPartOf”字段包含一个地区数组，可以在其中查找城市。
请参阅下面的讲师注释中的示例文档。

只需修改“make_pipeline”函数，使其创建并返回一个聚合管道，该管道可以传递到 MongoDB 聚合函数中。
和这节课中的示例一样，聚合管道应该是一个包含一个或多个字典对象的列表。如果不熟悉语法，请参阅这节课中的示例。

你的代码将根据我们提供的 MongoDB 实例运行。如果你想在本地机器上运行代码，
你需要安装 MongoDB 并下载和插入数据集。要了解 MongoDB 设置和数据集方面的说明，请参阅课程资料。

请注意，你在此处使用的数据集是这节课的示例中使用的城市集合的简略版本。
如果你尝试运行我们在课程示例中运行过的同一查询，结果可能不同。
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
        {"$group" : {"_id" : "$isPartOf" , 
                     "count" : {"$sum" : 1}
                     }
        },
        {"$sort" : {"count" : -1}},
        {"$limit" : 1}
        ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    print "Printing the first result:"
    import pprint
    pprint.pprint(result[0])
    assert result[0]["_id"] == "Uttar Pradesh"
    assert result[0]["count"] == 623


# sample
#  {
#     "_id" : ObjectId("52fe1d364b5ab856eea75ebc"),
#     "elevation" : 1855,
#     "name" : "Kud",
#     "country" : "India",
#     "lon" : 75.28,
#     "lat" : 33.08,
#     "isPartOf" : [
#         "Jammu and Kashmir",
#         "Udhampur district"
#     ],
#     "timeZone" : [
#         "Indian Standard Time"
#     ],
#     "population" : 1140
# }