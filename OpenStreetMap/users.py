#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")

你的任务是进一步探索数据。

第一项任务比较有趣，查找这一特定地区有多少唯一用户向地图做出了贡献！

函数 process_map 应该返回一组唯一的用户 ID（“uid”）
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        #pass
        for tag in element.iter('user')
        #user_name =user
    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()