import os
import csv
import pprint

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
	data = []
	
	with open(datafile, "r") as f:
		r = csv.DictReader(f)
		for line in r:
			data.append(line)
			

	return data

if __name__ == '__main__':
	datafile = os.path.join(DATADIR,DATAFILE)
	parse_file(datafile)
	d= parse_file(datafile)
	pprint.pprint(d)
