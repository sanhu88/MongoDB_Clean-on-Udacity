#!/usr/bin/env python
"""
$push is similar to $addToSet. The difference is that rather than accumulating only unique values 
it aggregates all values into an array.

Using an aggregation query, count the number of tweets for each user. In the same $group stage, 
use $push to accumulate all the tweet texts for each user. Limit your output to the 5 users
with the most tweets. 
Your result documents should include only the fields:
"_id" (screen name of user), 
"count" (number of tweets found for the user),
"tweet_texts" (a list of the tweet texts found for the user).  

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used in 
examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results will be different.

通过聚合查询查找出每个用户的推特数量。在相同的 $group 阶段，使用 $push 数出每个用户的所有推特文本数量。
仅数出推特数量在前五名的用户。

最后的文档应该仅包含以下字段：

"_id"（用户的帐号名），
"count"（用户的推文数量），
"tweet_texts"（用户的推文列表）。

只需修改“make_pipeline”函数，使其创建并返回一个聚合管道，该管道可以传递到 MongoDB 聚合函数中。
和这节课中的示例一样，聚合管道应该是一个包含一个或多个字典对象的列表。如果不熟悉语法，请参阅这节课中的示例。
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$group" : {"_id" : "$user.screen_name",
            "tweet_texts" : {"$push" : "$text"},
            "count" : {"$sum" : 1}
        }},
        {"$sort" :{"count" : -1}},
        {"$limit" : 5}
        ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    assert len(result) == 5
    assert result[0]["count"] > result[4]["count"]
    sample_tweet_text = u'Take my money! #liesguystell http://movie.sras2.ayorganes.com'
    assert result[4]["tweet_texts"][0] == sample_tweet_text
    