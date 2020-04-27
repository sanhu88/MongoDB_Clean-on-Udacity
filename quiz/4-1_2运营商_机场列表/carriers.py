#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
说明
请注意函数 'make_request' 仅供为参考。实际情况中，你是无法从优达学城的网页 UI 中使用它的。
你所有的修改都应该在函数 'extract_carrier' 中。并且注意该 html 文件是基于原网页删减过的版本。

这个练习中，你的任务是获取一个包含所有航空公司的列表。在你所返回的数据中要去掉所有类似 “All U.S. Carriers” 的组合。
最终你应该返回一个含有运营商编码的列表。

如果你只想在本地查看完整的 HTML 文件，你可以从原始 TranStats 网站下载。

#任务
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.
对于这道练习，你的任务是修改“extract_carrier()”，以便获取所有航空公司列表。请在返回的数据中删除所有的组合值，
例如“All U.S. Carriers”。你应该返回一个航空公司代码列表。

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.
你只需更改“extract_carrier()”函数。上述标签中的“options.html”文件是网站实际版本的缩减版，
但是可以帮助你大概了解完整文件的样貌。

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
请注意，函数“make_request()”仅供参考。你实际上无法在优达学城的网络 UI 中使用该函数。
"""

from bs4 import BeautifulSoup
html_page = "options.html"

def options(soup,id):
    option_values =[]
    carrier_list = soup.find(id =id)
    for option in carrier_list.find_all('option'):
    	option_values.append(option['value'])
    return option_values
    
def extract_carriers(page):
    data = {}

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        data["airport"] = options(soup,'AirportList')
        data["carrier"] = options(soup,'CarrierList')
        #print(data["airport"])
        data["eventvalidation"] = [soup.find(id="__EVENTVALIDATION")["value"]]
        #print(soup.find(id="__EVENTVALIDATION")["value"])
        #exit()
        data["viewstate"] = [soup.find(id="__VIEWSTATE")["value"]]
        

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__VIEWSTATEGENERATOR",viewstategenerator),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text


def test():
    data = extract_carriers(html_page)
    print(len(data))
    #assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    test()