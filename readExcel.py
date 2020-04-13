#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""
import os
import pprint
import xlrd
from zipfile import ZipFile

CWDPATH = os.getcwd()
DATADIR = "resource"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"
datafile = os.path.join(CWDPATH,(os.path.join(DATADIR, DATAFILE)))


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cosatmax = 0
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    #print (sheet.nrows)
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    coast = sheet.col_values(1, start_rowx=1, end_rowx=(sheet.nrows+1))
    cv = sheet.row_values(1, start_colx=1, end_colx=(sheet.ncols+1))
    print(cv)
    cosatmax = max(sheet.col_values(1, start_rowx=1, end_rowx=(sheet.nrows+1)))
    print (cosatmax)
    #print (type(coast))
    datacolumn = coast.index(cosatmax)
    print (datacolumn)
    #print (type(datacolumn))
    exceltimecolum = sheet.col_values(0, start_rowx=1, end_rowx=(sheet.nrows+1))
    exceltime = max(sheet.col_values(0, start_rowx=1, end_rowx=(sheet.nrows+1)))
    # print (sheet.row_values(2, start_colx=1, end_colx=4))

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    #exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    
    print (exceltimecolum[datacolumn])
    #pprint.pprint(exceltimecolum)
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    print (xlrd.xldate_as_tuple(exceltime, 0))
    print (xlrd.xldate_as_tuple(exceltimecolum[datacolumn], 0))
    maxtime= xlrd.xldate_as_tuple(exceltimecolum[datacolumn], 0)
    print (round(cosatmax,10))
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    data['maxtime']=maxtime
    data['maxvalue']=cosatmax
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18770.166858114, 10)


test()