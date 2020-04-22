from bs4 import BeautifulSoup
import os
CWDPATH = os.getcwd()
DATADIR = "resource"
DATAFILE = "DataElements.html"
html_file = os.path.join(CWDPATH,(os.path.join(DATADIR, DATAFILE)))

def options(soup,id):
    option_values =[]
    carrier_list = soup.find(id =id)
    for option in carrier_list.find_all('option'):
    	option_values.append(option['value'])
    return option_values

def print_list(lable,codes):
	print(f"\n {lable}")
	for c in codes:
		print(c)

def main():
	#soup = BeautifulSoup(open(article_file))
	file_text = open(html_file,'r',encoding='utf-8')
	#soup = BeautifulSoup(file_text,'html.parser')
	soup = BeautifulSoup(file_text,'lxml') #WORK SAME 

	codes = options(soup,'CarrierList')
	print_list('Carriers : ',codes)

	codes = options(soup,'AirportList')
	#print_list('Airports',codes)

main()