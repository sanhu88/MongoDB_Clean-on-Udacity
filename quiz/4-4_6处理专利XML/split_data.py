#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.
# 问题是庞大的文件实际上不是有效的 XML，因为它有几个根元素和 XML 声明。
# 实际上是多个相连的 XML 文档构成的。一种解决方法是将文件拆分为多个文档，
# 并将这些文档处理为有效的 XML 文档。
'''

import xml.etree.ElementTree as ET
import pprint
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    n =0
    tree = ET.ElementTree(filename)
    pprint.pprint(tree)
    exit()
    for child in tree.find('encoding'):
        print(child)
        n+=1
    
    print(n)
    exit()

    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()