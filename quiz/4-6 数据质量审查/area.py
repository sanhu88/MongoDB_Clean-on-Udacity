#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.
在此习题集中，你将处理城市 infobox 数据，对数据进行审核，然后想出清理方法并清理数据。


Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.
因为在上一道测验中，你已经决定针对“areaLand”字段保留哪个值，你现在知道该如何操作了。

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
完成函数 fix_area()。它将获得字符串输入，并需要返回表示面积值的浮点值或 None。
你需要更改fix_area 函数。你可以使用其他函数，但是对 process_file 的更改不会计入评估范围。
代码的其余部分只是用来展示可以如何使用该函数的示例。
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):

    # YOUR CODE HERE
    if area =='NULL' or area =='' or area.count('{'):
        area ='None'
    else:
        area = float(area)

    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []


    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            #l = reader.next()
            #Since Python 2.6 you should use next(foo) instead of foo.next().
            l= next(reader)

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print ("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()