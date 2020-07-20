#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'

你的任务是使用迭代解析处理地图文件，并找出有什么样的标记，以及有多少个，
以便了解预计在地图中的每个类别有多少数据。请填写 count_tags 函数。
它应该返回一个字典，标记是键，该标记在地图中出现的次数是值。
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tags = {}
    
        


def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    

if __name__ == "__main__":
    test()