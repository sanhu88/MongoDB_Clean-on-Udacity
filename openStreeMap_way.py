import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

#osm_file = open('chicaogo_tail.osm','r',encoding='UTF-8')
osm_file = open('./OpenStreetMap/Downtown-map.osm','r',encoding='UTF-8')

# street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
# street_types = defaultdict(set)
street_types = defaultdict(set)

expected = ['Expressway','street','Avenue','Boulevard','Drive','Court','Place','大道','东莞','路']
#expected = []
def audit_street_type(street_types,street_name):
	m = street_type_re.search(street_name)
	if m:
		street_type = m.group()
		if street_type not in expected:
			street_types[street_type].add(street_name)

def print_sorted_dict(d):
	keys = d.keys()
	keys =  sorted(keys,key=lambda s:s.lower())
	for k in keys:
		v = d[k]
		print(f'{k} : {v}')

def is_street_name(elem):
	#return(elem.attrib['k'] == 'addr:stree')
	# return(elem.attrib['k'] == 'name:en')
	return(elem.attrib['k'] == 'name:zh')

def audit():
	for event,elem in ET.iterparse(osm_file,events=('start',)):	#迭代解析筛选顶级标签
		if elem.tag == 'way':	# 筛选只要way的顶级标签
			for tag in elem.iter('tag'):	# 只要iter里的tag标签
				if is_street_name(tag):
					audit_street_type(street_types,tag.attrib['v'])
	pprint.pprint(dict(street_types))
	print_sorted_dict(street_types)


if __name__ == '__main__':
	audit()

