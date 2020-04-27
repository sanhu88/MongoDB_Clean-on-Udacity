#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".请完成“extract_airports()”函数，使其返回机场代码列表，
并删除任何组合内容，例如“All”。

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
请参阅上述标签中的“options.html”文件，了解实际网站的缩减版。test() 声明是基于给定的文件。
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrier_list = soup.find(id ='AirportList')
        for option in carrier_list.find_all('option'):
            if (len(option['value']) == 3 and option['value'] !='All'):
                data.append(option['value'])
        	
        	    

    return data


def test():
    data = extract_airports(html_page)
    #print(data)
    #exit()
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()