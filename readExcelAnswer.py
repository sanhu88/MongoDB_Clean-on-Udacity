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

    #cv = sheet.col_values(1, start_rowx=1, end_rowx=None)  ##Udacity答案
    cv = sheet.col_values(1, start_rowx=1, end_rowx=(sheet.nrows+1))

    maxval = max(cv)
    minval = min(cv)
    #avgval = sum(cv)/ float(len(cv)) ##Udacity答案
    avgval = sum(cv)/ int(sheet.nrows-1)   ##表头减去1
    print(avgval)

    maxpos = cv.index(maxval) +1
    minpos = cv.index(minval) +1

    maxtime = sheet.cell_value(maxpos,0)
    realmaxtime = xlrd.xldate_as_tuple(maxtime,0)
    mintime = sheet.cell_value(minpos,0)
    realmintime = xlrd.xldate_as_tuple(mintime,0)

    data={
            'maxtime': realmaxtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': avgval
    }

    pprint.pprint(data)

    
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18770.166858114, 10)


test()