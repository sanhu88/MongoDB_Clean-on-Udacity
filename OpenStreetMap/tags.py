#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.

你的任务是进一步探索数据。

在处理数据并将其添加到数据库中之前，你应该检查每个“<标记>”的“k”值，看看是否存在潜在问题。

我们提供了 3 个正则表达式，用来检查标记的某些规律。正如在上一道测验中看到的，
我们想要更改数据模型，并将“addr:street”类型的键展开为字典，
如下所示：{"address": {"street": "Some value"}}

我们需要查看是否有此类标记，以及任何标记是否存在具有问题的字符。

请完成函数“key_type”，并得出这四大标记类别在字典中的各自数量：

“lower”，表示仅包含小写字母且有效的标记，
“lower_colon”，表示名称中有冒号0.的其他有效标记，
“problemchars”，表示字符存在问题的标记，以及
“other”，表示不属于上述三大类别的其他标记。
请参阅“process_map”和“test”函数，了解我们期望的格式。
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        for tag in element.iter('tag'):
            # pprint.pprint(tag)
            # exit()
            key_name = tag.attrib['k']

            if lower.search(key_name):
                keys['lower'] += 1
            if lower_colon.search(key_name):
                keys['lower_colon'] += 1
            if problemchars.search(key_name):
                keys['problemchars'] += 1
            else:
                keys['other'] += 1
        
       
    return keys




def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('example.osm')
    pprint.pprint(keys)
    exit()
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()