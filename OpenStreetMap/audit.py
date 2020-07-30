"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected

在这道练习中，你需要完成以下两步：

审核 OSMFILE 并更改变量“mapping”，表示为了修正预期列表中相应项的错误街道类型需要做出的更改。
你必须仅为在此 OSMFILE 中发现的实际问题添加映射，而不是泛化的解决方案，因为这将取决于你要审核的特定区域。
编写 update_name 函数，实际地修正街道名称。该函数传入街道名称作为参数，应该返回修正过后的名称。
我们提供了一个简单的测试，使你能够了解我们的预期结果
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "example-street.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):

    # YOUR CODE HERE

    return name


def test():
    st_types = audit(OSMFILE)
    assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    # for st_type, ways in st_types.iteritems():
    #     for name in ways:
    #         better_name = update_name(name, mapping)
    #         print name, "=>", better_name
    #         if name == "West Lexington St.":
    #             assert better_name == "West Lexington Street"
    #         if name == "Baldwin Rd.":
    #             assert better_name == "Baldwin Road"


if __name__ == '__main__':
    pprint.pprint(audit(OSMFILE))
    exit()
    test()