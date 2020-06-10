"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code on MongoDB outside of our classroom,
please see the Instructor comments at the bottom of this page for link.

你的任务是成功地运行练习，看看 pymongo 是如何运行的，并了解可以如何轻松地开始使用 pymongo。

在这道练习中，你不需要更改任何内容，但是你可以根据需要更改 add_city 函数中的城市名称。

你的代码将根据我们提供的 MongoDB 实例运行。

如果你想在本地机器上运行代码，你需要安装 MongoDB 并取消注释 get_db 函数。
"""

def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    # db.cities.insert({"name" : "Beijing"})
    db.cities.insert_one({"name" : "Shanghai"})
    
def get_city(db):
    return db.cities.find_one()

def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db

if __name__ == "__main__":
    # For local use
    db = get_db() # uncomment this line if you want to run this locally
    #add_city(db)
    #print (get_city(db))
    for a in db.cities.find():
        print(a)