import os
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
#soup =  BeautifulSoup(r.text,'lxml')	
soup =  BeautifulSoup(r.text,'html5lib')	#html5lib 需要安装，速度慢，兼容性好
eventvalidation = soup.find(id="__EVENTVALIDATION")["value"]
viewstate = soup.find(id="__VIEWSTATE")["value"]
viewstategenerator = soup.find(id="__VIEWSTATEGENERATOR")["value"]
#print(f'viewstategenerator: {viewstategenerator}')
#exit()

new = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "ONT",
                          'CarrierList': "AA",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATEGENERATOR": viewstategenerator,
                          "__VIEWSTATE": viewstate
                    })
with open('ONT-AA-ariline.html','w') as f:
	f.write(new.text)
