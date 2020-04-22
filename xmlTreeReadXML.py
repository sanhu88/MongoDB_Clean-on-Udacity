import os
import xml.etree.ElementTree as ET

CWDPATH = os.getcwd()
DATADIR = "resource"
DATAFILE = "exampleResearchArticle.xml"
article_file = os.path.join(CWDPATH,(os.path.join(DATADIR, DATAFILE)))

def get_root(fname):
	tree = ET.parse(fname)
	return tree.getroot()

# def get_authors(root):
# 	authors =[]
# 	for author in root.findall('./fm/bibl/aug/au'):
# 		data = {
# 			'fnm':author.find('fnm').text,
# 			'snm':author.find('snm').text,
# 			'email':author.find('email').text
# 		}
# 		authors.append(data)
# 	return authors

def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        #data["insr"].append(author.find('./insr').text)
        insr = author.findall('./insr')
        for i in insr:
        	data["insr"].append(i.attrib["iid"])
        #exit()

        # YOUR CODE HERE

        authors.append(data)

    return authors

def test():
	print('ok')
	print(article_file)
	#solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}]
	solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}]
	root = get_root(article_file)
	data = get_authors(root)
	assert data[0] == solution[0]
 	#root = get_root(article_file)
 	#data = get_authors(root)

    #assert data[0] == solustion[0]


test()