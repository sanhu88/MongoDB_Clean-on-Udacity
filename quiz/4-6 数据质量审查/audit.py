#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

在此习题集中，你将处理城市 infobox 数据，对数据进行审核，然后想出清理方法并清理数据。
在第一道练习中，请审核数据集中某些特定字段中的数据类型。
值类型可以是：
-    NoneType，如果值是字符串“NULL”或空字符串“”
-    列表，如果值以“{”开头
-    整型，如果值可以转型为整型
-    浮点型，如果值可以转型为浮点型，但是无法转型为整型。
例如，“3.23e+07”应该被当做浮点型，因为可以转型为浮点型，但是int('3.23e+07') 
将抛出 ValueError
-    “str”，表示其他所有值


The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}

audit_file 函数应该返回一个字典，其中包含字段名称和可以在该字段中找到的类型集。例如
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}


The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

type() 函数返回的是类型对象，描述了提供给该函数的参数。你还可以使用对象示例创建类型对象，
例如 type(1.1) 表示浮点型：具体示例请参阅下面的测试函数。


Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.

注意，cities.csv 文件的前三行（标题行之后）不是实际的数据点。在处理数据类型时，
不应该包含这些行的内容。确保在代码中包含相关功能，以便跳过或检测出这些行。

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE


    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
