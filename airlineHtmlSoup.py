#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json
import os

CWDPATH = os.getcwd()
DATADIR = "resource"
DATAFILE = "DataElements.html"
html_page = os.path.join(CWDPATH,(os.path.join(DATADIR, DATAFILE)))



def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    #with open(page, "r") as html: 
    #UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 3519: illegal multibyte sequence
    with open(page,'r',encoding='utf-8') as html:
      #print(type(html))
      #exit()
      soup = BeautifulSoup(html,'html.parser')
      eventvalidation = soup.find(id="__EVENTVALIDATION")["value"]
      viewstate = soup.find(id="__VIEWSTATEGENERATOR")["value"]
      data["eventvalidation"] = eventvalidation
      data["viewstate"] = viewstate
      #print(eventvalidation["value"])
      #for item in eventvalidation:
      #  print(item["value"])
        #data["eventvalidation"] = item["value"]
      #print(eventvalidation)
      #exit()
        # do something here to find the necessary values
        
        
        
        

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")

    
test()
#extract_data(html_page)