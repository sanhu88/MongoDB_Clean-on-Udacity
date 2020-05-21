#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.
在此习题集中，你将处理城市 infobox 数据，对数据进行审核，然后想出清理方法并清理数据。


If you look at the full city data, you will notice that there are couple of
values that seem to provide the same information in different formats: "point"
seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long". However,
we do not know if that is the case and should check if they are equivalent.
如果你查看完整的城市数据，会发现有几个值似乎提供的是同一信息，
只是格式不同：“point”似乎是“wgs84_pos#lat”和“wgs84_pos#long”的结合体。
但是，我们不知道是否是这种情况，你应该检查它们是否相等。


Finish the function check_loc(). It will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. You have to
extract the lat and long values from the "point" argument and compare them to
the "wgs84_pos# values, returning True or False.
完成函数check_loc()。它应该获得 3 个字符串：首先是“point”的值后面跟上单独的“wgs84_pos#”值。
你应该从“point”参数中提取lat和长值，并将它们与“wgs84_pos#”值对比，返回 True 或 False。


Note that you do not have to fix the values, only determine if they are
consistent. To fix them in this case you would need more information. Feel free
to discuss possible strategies for fixing this on the discussion forum.
注意，你不需要修正这些值，只需判断它们是否保持一致。要修正这些值，你需要更多信息。
欢迎在论坛上讨论如何修正这些值。


The rest of the code is just an example on how this function can be used.
Changes to "process_file" function will not be taken into account for grading.
代码的其余部分只是可以用来展示如何使用该函数的示例。
我们在打分时，不会考虑对“process_file”函数做出的更改。

"""
import csv
import pprint

CITIES = 'cities.csv'


def check_loc(point, lat, longi):
    # YOUR CODE HERE
    
    pass


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra matadata
        for i in range(3):
            l =next(reader)
        # processing file
        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            data.append(line)

    return data


def test():
    assert check_loc("33.08 75.28", "33.08", "75.28") == True
    assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False

if __name__ == "__main__":
    test()