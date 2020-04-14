# MongoDB_Clean-on-Udacity

-----

## 1 数据提取基础

### 1-3~4 评估数据指向

* 我们不应该信任任何处理前的数据，可能会存在错误
* 需要验证关于数据值、数据类型已经数据模型（shape）的假设
* 需要找出数据中的错误（error）和异常值（outliers）
* 需要确定数据是否缺少值
* 确保数据支持我们要进行的研究



### 1-7~9 使用python 读取数据

> 不适用程序直接打开，因为过大的文件程序软件无法处理

~~~python
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
# 
# 你的任务是逐行阅读输入 DATAFILE 文件，对于前 10 行（不包括标题），
# 根据“,”拆分每行，然后为每行创建一个字典，
# 键是字段的标题，值是该字段在该行中的值。
# 函数 parse_file 应该返回一个字典列表，
# 文件中的每个数据行是一个列表项。
# 字段名称和值不应该包含多余的空白，例如空格或换行字符。
# 你可以使用 Python 字符串方法strip() 删除多余的空白。
# 对于这道练习，你只需解析前 10 行数据，
#所以返回的列表应该有 10 项！
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
	data = []
	with open(datafile, "r") as f:

		header = f.readline().split(',')
		counter = 0
		for line in f:
			if counter == 10:
				break
			fields = line.split(',')
			entry = {}
#返回 enumerate(枚举) 对象。
			for i,value in enumerate(fields):
				entry[header[i].strip()] = value.strip()
			data.append(entry)
			counter +=1

	return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    # print(d)
    # exit()
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    assert d[0] == firstline
    assert d[9] == tenthline
    print( d[0] == firstline)
    print( d[9] == tenthline)

    
test()

~~~

留意数据中是否存在分隔符的数据单元。

CSV模块 [官网3.8](https://docs.python.org/3.8/library/csv.html)

~~~python
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
~~~

~~~json
 [{'BPI Certification': '',
  'Label': 'Capitol(US)[C]',
  'RIAA Certification': '6xPlatinum',
  'Released': '6 December 1965',
  'Title': '',
  'UK Chart Position': '-',
  'US Chart Position': '1'},
 {'BPI Certification': '',
  'Label': 'Capitol(US)',
  'RIAA Certification': '2xPlatinum',
  'Released': '15 June 1966',
  'Title': 'Yesterday and Today',
  'UK Chart Position': '-',
  'US Chart Position': '1'},
 {'BPI Certification': 'Platinum',
  'Label': 'Parlophone(UK)',
  'RIAA Certification': '',
  'Released': '5 August 1966',
  'Title': 'Revolver',
  'UK Chart Position': '1',
  'US Chart Position': '-'},
 {'BPI Certification': '',
  'Label': 'Capitol(US)[C]',
  'RIAA Certification': '5xPlatinum',
  'Released': '8 August 1966',
  'Title': '',
  'UK Chart Position': '-',
  'US Chart Position': '1'},
 {'BPI Certification': '3xPlatinum',
  'Label': 'Parlophone(UK), Capitol(US)',
  'RIAA Certification': '11xPlatinum',
  'Released': '1 June 1967',
  'Title': "Sgt. Pepper's Lonely Hearts Club Band",
  'UK Chart Position': '1',
  'US Chart Position': '1'},
 {'BPI Certification': 'Platinum',
  'Label': 'Parlophone(UK), Capitol(US)',
  'RIAA Certification': '6xPlatinum',
  'Released': '27 November 1967',
  'Title': 'Magical Mystery Tour',
  'UK Chart Position': '31[D]',
  'US Chart Position': '1'},
 {'BPI Certification': 'Platinum',
  'Label': 'Apple(UK), Capitol(US)',
  'RIAA Certification': '19xPlatinum',
  'Released': '22 November 1968',
  'Title': 'The Beatles',
  'UK Chart Position': '1',
  'US Chart Position': '1'},
 {'BPI Certification': 'Silver',
  'Label': 'Apple(UK), Capitol(US)',
  'RIAA Certification': 'Platinum',
  'Released': '13 January 1969',
  'Title': 'Yellow Submarine',
  'UK Chart Position': '3',
  'US Chart Position': '2'},
 {'BPI Certification': '2xPlatinum',
  'Label': 'Apple(UK), Capitol(US)',
  'RIAA Certification': '12xPlatinum',
  'Released': '26 September 1969',
  'Title': 'Abbey Road',
  'UK Chart Position': '1',
  'US Chart Position': '1'},
 {'BPI Certification': 'Gold',
  'Label': 'Apple(UK),United Artists(US)',
  'RIAA Certification': '4xPlatinum',
  'Released': '8 May 1970',
  'Title': 'Let It Be',
  'UK Chart Position': '1',
  'US Chart Position': '1'}]
~~~

### 1-10 XLRD excel 文件读取

~~~python
import xlrd
~~~

xlrd 可以处理xls和xlsx格式的表格

xlrd的索引index是0开始

还有一个 xlwt 的模块，用于创建excel文件

~~~python
 def parse_file(datafile):
        worksheet = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)
        
        data = [[sheet.cell_value(r,col)
                	for col in range(sheet.ncols)
                		for r in range(sheet.nrows)]]
        
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                if row == 50:
                    print(sheet.cell_value(row,col))
                    
        sheet.cell_type(3,2) #2 代表是浮点数
        sheet.cell_value(3,2)
~~~

#### 安装

~~~python
pip install xlrd
~~~

~~~python
cell_value(行数，列数) #先肉row再列col
~~~

#### 获取所有数据

~~~python
workbook = xlrd.open_workbook(datafile)
sheet = workbook.sheet_by_index(0)
sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
~~~

#### 一列或一行

~~~python
#一列
cv = sheet.col_values(1, start_rowx=1, end_rowx=None)  ##Udacity答案
cv = sheet.col_values(1, start_rowx=1, end_rowx=(sheet.nrows+1))

#一行
cv = sheet.row_values(1, start_colx=1, end_colx=(sheet.ncols+1))
~~~

tips

* 文件结尾注意xls和xlsx

### 1-11_16 JSON

对应python里的字典{}

Json的数据建模的细节：

* 各项数据可能会有不同的字段 - itmes may have different fields
* 可能会有嵌套对象 - may have nested objects
* 可能嵌套数组 - may have nested arrays

[Json教程](https://www.w3school.com.cn/json/index.asp)

jason返回unicode的汉字时

~~~python
print (json.dumps(data, indent=indent, sort_keys=True,ensure_ascii=False)) #,ensure_ascii=False
~~~

