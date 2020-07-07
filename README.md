# MongoDB_Clean-on-Udacity

-----

> 课程详情 [link](https://www.udacity.com/wiki/ud032#datasets-used-in-this-course)

## 1 数据提取基础

### 1-3~4 评估数据指向

* 我们不应该信任任何处理前的数据，可能会存在错误
* 需要验证关于数据值、数据类型已经数据模型（shape）的假设
* 需要找出数据中的错误（error）和异常值（outliers）
* 需要确定数据是否缺少值
* 确保数据支持我们要进行的研究



### 1-7~9 使用python 读取CSV数据

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

json.loads 用于解码 JSON 数据

Json的数据建模的细节：

* 各项数据可能会有不同的字段 - itmes may have different fields
* 可能会有嵌套对象 - may have nested objects
* 可能嵌套数组 - may have nested arrays

[Json教程](https://www.w3school.com.cn/json/index.asp)

jason返回unicode的汉字时

~~~python
print (json.dumps(data, indent=indent, sort_keys=True,ensure_ascii=False)) #,ensure_ascii=False
~~~

~~~
python 原始类型向 json 类型的转化对照表：

Python				JSON
dict				object
list, tuple			array
str, unicode		string
int, long, float	number
True				true
False				false
None				null
#来自https://www.runoob.com/python/python-json.html
~~~



## 2 XML

### 2-3 XML的设计原则

XML目的：

* 不依赖平台的数据传输 Data Transfer
* 方便的读写代码 Easy to read/write code
* 数据可以验证 Data Validation
* 方便人工阅读 Human Readable
* 支持多种应用 Support a wide varirty apps

XML 拥有一套标准好处：

* 好处之一，很多程序(比如python)有很强悍(robust)的分析器，
* 可以让开发者专注于自身应用，无需编写特定解析器的数据格式
* 免费使用，是“免费”软件，不是“自由”软件

XML 设计原则：

* 可以构建数据库来支持特定的查询
* 可以转化成其他格式，而不会有信息丢失
* XML更注重于内容，而不是表格或者外观

### 2-4~ XML 实践基础

* 语法 syntax

  1. 由XML 元素构成，标记对
  2. <tag k ='' value='' /> 创建空元素

* Json几乎可以完美的映射到python的字典

  ~~~
  使用 JSON 函数需要导入 json 库：import json。
  
  json.dumps	将 Python 对象编码成 JSON 字符串
  json.loads	将已编码的 JSON 字符串解码为 Python 对象
  ~~~

* 解析XML,接续XML到文件树

  ~~~python
  import xml.etree.ElementTree as ET
  import pprint
  
  ~~~
~~~python
tree = ET.parse('example.xml')
  root = tree.getroot()

  for child in root:
      print(child.tag)
~~~

  ~~~python
 #接上
  title = root.find('./fm/bibl/title')	#Xpatch 语法
  title_text = ''
  for p in title:
      title_text += p.text
  
      
  for a in root.findadd('./fm/bibl/aug/au'):
      email = a.find('email')
      if email is not None:
          print(email.text)
  
  ~~~

  ### 2-8 XML练习-提取数据

课后答案：

~~~python
def get_author(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text

        authors.append(data)

    return authors
~~~

自己写的，考虑到None值，但是没有处理

~~~python
def get_authors(root):
	authors =[]
	for author in root.findall('./fm/bibl/aug/au'):
		data = {
			'fnm':author.find('fnm').text,
			'snm':author.find('snm').text,
			'email':author.find('email').text
		}
		authors.append(data)
	return authors
~~~

### 2-9 XML练习-处理属性

对于有子属性的标签

~~~xml
<insr iid="I3"/>
<insr iid="I4"/>
~~~

要获取子标签的text，需要使用 .attrib["iid"] 。来获取

~~~python
insr = author.findall('./insr')
        for i in insr:
        	data["insr"].append(i.attrib["iid"])
~~~

### 2-10~ 机场数据获取

数据来源

> https://www.transtats.bts.gov/Data_Elements.aspx?Data=2

步骤分解：

1. 创建用于保存航空公司和机场名称的list
2. HTTP去下载所有数据
3. 解析parse 数据文件

### 2-15 提取实体

~~~python
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
	print_list('Carriers',codes)

	codes = options(soup,'AirportList')
	print_list('Airports',codes)

main()
~~~

### 2-16 构建http请求

网页的查询操作以通过按钮提交

~~~html
<form method="post" action="./Data_Elements.aspx?Data=2" id="form1">
~~~

* 请求网址

  /Data_Elements.aspx?Data=2 也就是本身

* 请求方式

  post

### 2-17~18 如何传递参数进行查询

在浏览器开发者工具的 Network 工具栏

会看到 Header里 的Form Data 除了已知的参数传入外，还有其他几个比如：

**__EVENTTARGET** / **__EVENTARGUMENT**/ **__VIEWSTATE** / **__VIEWSTATEGENERATOR** / **__EVENTVALIDATION** / **CarrierList** / **AirportList** / **Submit**

### 2-19 构建带参数的请求

* 一些表单元素被隐藏，没有显示在用户界面

  ~~~html
  <div class="aspNetHidden">
  <input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
  <input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
  <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/……">
  </div>
  
  <div class="aspNetHidden">
  
  	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="8E3A4798">
  	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/……">
             
  ~~~

* 查找eventvalidation 和 viewstate

  答案

  ~~~python
  def extract_data(page):
      data = {"eventvalidation": "",
              "viewstate": ""}
      with open(page, "r") as html:
          soup = BeautifulSoup(html, "lxml")
          ev = soup.find(id="__EVENTVALIDATION")
          data["eventvalidation"] = ev["value"]
  
          vs = soup.find(id="__VIEWSTATE")
          data["viewstate"] = vs["value"]
  
      return data
  ~~~

  我的写法

  ~~~python
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
  ~~~

  

### 2-20 请求中断

如果用get的一些隐藏参数去post查询，一般会被网站拦截

~~~python
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
~~~

### 2-21 抓取一些经验

* 查看浏览器如何发出请求(wireshark)
* 在代码中模拟 emulate in code
* 换种方法查看http请求
* 继续迭代循环操作模拟请求

### 2-22 抓取解法

* 使用会话

  ~~~python
  s = requests.Session()
  ~~~




## 3 数据清洗

### 3-1~3 什么是数据清洗

是一个不断迭代处理的过程 iterative ，处理数据中的outlier 或者不同地域的约定，比如US的日期格式是 08/24/2019 但是UK的是24/08/2019

### 3-4 脏数据的来源

* 只要人参与就存在脏数据的可能
* 用户输入错误 use entry errors
* 编码标准较低，或者没有被严格执行
* 不同的数据结构表 schema
* 遗留系统 legacy
* 系统的进化扩容和升级 evolve
* 不唯一的标识符 Identifiers
* 数据转换中产生的错误
* 程序或者程序员错误
* 数据在传输和储存发生的物理错误

### 3-5~6 数据质量

五大度量标准：

* 有效性 validity ，数据是否符合数据模式或者其他约束条件，比如年龄不能为负数
* 精度，准确性 accuracy ，比如数据集中的地址是否都真实存在？需要一些黄金标准
* 完整性 completeness 是否包含所有记录？
* 数据内部的一致性 consistency ，是否匹配其他记录
* 统一性 uniformity ，比如数据单位是否一致

###   3-7 数据清理蓝图

1. 审核数据 audit
   * 编写验证规则步骤检查数据
   * 创建数据质量报告
   * 运行统计分析，检查异常值
2. 制定数据清理计划
   * 确定脏数据产生的各项原因
   * 定义一组操作来纠正修复数据
   * 进行测试
3. 执行数据清理计划
   * 运行操作集来整理数据
4. 人工纠正
5. 循环迭代 1-4步

### 3-8 蓝图清洗数据实例

芝加哥街道类型名称统计

留意结果中有些时候纯数字部分，不是接待类型

资料[下载地址](http://cn-static.udacity.com/DAND_file/chicago_illinois.osm.bz2)，解压后很大1.7G

代码部分

~~~python
#!/usr/bin/env python
          # -*- coding: utf-8 -*-
          import xml.etree.cElementTree as ET
          from collections import defaultdict
          import re	#regular expression

          osm_file = open("chicago.osm", "r")

          street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
          street_types = defaultdict(int)

          def audit_street_type(street_types, street_name):
              m = street_type_re.search(street_name)
              if m:
                  street_type = m.group()

                  street_types[street_type] += 1

          def print_sorted_dict(d):
              keys = d.keys()
              keys = sorted(keys, key=lambda s: s.lower())
              for k in keys:
                  v = d[k]
                  print "%s: %d" % (k, v) 

          def is_street_name(elem):
              return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

          def audit():
              for event, elem in ET.iterparse(osm_file):
                  if is_street_name(elem):
                      audit_street_type(street_types, elem.attrib['v'])    
              print_sorted_dict(street_types)    

          if __name__ == '__main__':
              audit()
~~~

### 3-9~12 validity 审查有效性

* 关注单独字段的值：必填项，唯一值
* 交叉字段约束（外键），开始日期必须在结束日期前，数据类型的指定
  * 特殊的正则表达式约束 ，邮编，邮箱地址

审核有效性是，确定对个别字段的施加约束，并检查字段符合这些约束条件。

https://wiki.dbpedia.org/ 城市数据下载为csv文件，邮编项会有不同的书写格式；时区项，分夏令时和非夏令时，也可能包含HTML代码。

交叉约束，以人口密度为例，进行数学计算有效性检查。

习题中，图书馆中的图书实例，应该借出人信息和库存数进行交叉有效性约束。

### 3-13~14 accuracy 审查准确率

准确率的难度很高，需要黄金标准。

以城市所属国家为例，选用ISO-3316 两位大写字母代替国家。



以下为代码片段：

~~~python
client = MongoCliebt('mongodb://localhost:27017')
db = client.examples

def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)
        
def audit_country(input_file):
    for row in input_file:
        country = row['country_label']
        country = country.strip()
        if (country == 'null') or (country == ''):
            countinue
        if db.countries.find({'name' : country}).count() != 1:
            print(f'Not found: {country}')
            
if __name__ = '__main__':
    input_file = csv.DictReader(open('cities.csv'))
    skip_line(input_file,2)
    audit_country(input_file)
    
~~~



代码match ISO 代码后，一些国家的字段值不在ISO内的原因：

1. 使用数组，一个城市对应多个地区（重名现象）
2. 列的漂移
3. 用正则表达式来修复，比如下划线连接了单词
4. 语言或者政治原因（对应办法是，只使用确定的有效的国家）

### 3-15 completeness 完整性检查

1. 你无法确定你不知道的领域的知识
2. 发现整个记录缺失的情况，而不是某个记录缺失了部分字段
3. 参照参考数据来判断

### 3-16~17 consistency  一致性审查

当两个输入项相互矛盾时，就会出现不一致性。

1. 比如输入两个收货地址：
   * 哪一个地址是最近输入的？
   * 哪种收集方法更可靠？

解决一致性问题的关键是确定哪个数据源最肯能是正确的。并可能通过从我们最信任的记录复制出数据。

案例使用不同时期，美国公司使用不同股票符号唯一码的问题，代码可以分配给不同的公司，但是需要明确的记录更改时间，以及对应的更改公司。测试问题是，欧洲一个国家加入欧元区的前后，交易记录的汇率名称一致性审查。

### 3-18 uniformity 统一性（均匀性）审查

使用相同单位的所有值

一下代码测试城市的纬度，默认是浮点数坐标

~~~python
minval = -90
maxval = 90

def audit_float_field(v, counts):
    v = v.strip()
    if v == 'NULL':
        counts['nulls'] += 1
    elif v == '':
        counts['empties'] += 1
    elif is_array(v):
        counts['arrary'] += 1
    elif not is_number(v):
        print(f'Found non number:{v}')
    else:
        v = float(v):
            if not ((minval < v) and (v < maxval)):
                print(f'Found put of range value : {v}')
                
~~~

但是可能数据集中包含 度分秒的坐标方式：

~~~
34 25 00 N
~~~

使用了不同的单位，如果直接导入，会产生dirty data

### 3-19 more about correcting

* 删除修正印刷（笔误）错误
* 对已知的实体，验证我们的数据。交叉多次验证核对
* 对数据进行添加相关信息，提升数据完整度
* harmonizing 调整数据，比如把街道、路缩写扩充成全程，当然也可以选择全部用简称
* 改变数据集的编码方式，国家双字母换成三字母表示

### 练习

Keeping the value with most significant digits makes the most sense, since it most likely comes from the most reliable source.

保留最有效数字的值最有意义，因为它最有可能来自比较可靠的来源。

#### 4

explore thedata and mark the fields that you think also should be processed in a similar way as 'areaLand'(changed from an array to a single value):

* populationTotal and areaMetro
* Name can not really be checked for correctness like that! Some places can even officially have names in different languages!
* "postalCode" can not be processed like that. Look at the contents of the field (just print out all the values for the field)! There are so many variations that so simplified approach of cleaning would not work well on this field.

#### Python日期计算

~~~python
import datetime
def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    end_date = ''
    n = int(time.split(' ')[0])
    time_range = time.split(' ')[1]
    start_date_time = datetime.datetime.strptime(start_date,"%Y/%m/%d")
    if time.count('day'):
        end_date = start_date_time + datetime.timedelta(days=n)
    if time.count('week'):
        end_date = start_date_time + datetime.timedelta(weeks=n)
    
    # Replace this with your code!
    end_date = end_date.strftime("%Y-%m-%d")
    return end_date
    print(end_date)

    


if __name__ == "__main__":
    
    print(which_date('2016/02/10','35 days'))
    print(which_date('2015/01/17','1 week'))
~~~



#### SQL 和 MongoDB

* [SQL vs. NoSQL: 有何区别？](http://www.sitepoint.com/sql-vs-nosql-differences) 正片文章写得简单详实，值得翻译



## 4 MongoDB

### 4-1 介绍

* 对于数据分析程序有重要意义
* No-SQL 数据库，通常叫做文档数据库 document database
  * 不是PPT/PDF/DOC的文档存储
  * 文档，是指关联数组 associative array，如JSON 对象，php的数组，python的字典，ruby的散列表
* 允许存储层次数据结构，为独立的项目或文件

### 4-2 数据建模

将数据转化成JSON格式的嵌套样式，比如特斯拉的车型包含设计师（first name ，last name，也可以直接是一行字符串），多个安装工厂等。

~~~json
{
    "manufacturer" : "Tesla Motors",
    "class" : "full-size",
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holzhausen"
    }
    "production" : "[2012,2013]"
}
~~~

> MongoDB documents can contain lists and nested dictionaries like JSON objects and Python dictionaries.

### 4-3 为何使用MongoDB

1. 灵活的模式 flexible schema，更容易处理扁平格式数据
2. 面向程序员 oriented toward programmers，熟悉的数据格式；支持流行语言的驱动程序
3. 灵活的部署方式 flexible deployment
4. 设计面向大数据 designed for big data,良好的扩展性
5. 聚合框架 aggregation framework 利于高效分析数据

官网下载 https://www.mongodb.com/download-center/community

安装python数据驱动

~~~python
python -m pip install pymongo
~~~

练习

~~~python
"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code on MongoDB outside of our classroom,
please see the Instructor comments at the bottom of this page for link.

你的任务是成功地运行练习，看看 pymongo 是如何运行的，并了解可以如何轻松地开始使用 pymongo。

在这道练习中，你不需要更改任何内容，但是你可以根据需要更改 add_city 函数中的城市名称。

你的代码将根据我们提供的 MongoDB 实例运行。
"""

def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert({"name" : "Chicago"})
    
def get_city(db):
    return db.cities.find_one()

def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db

if __name__ == "__main__":
    # For local use
    # db = get_db() # uncomment this line if you want to run this locally
    add_city(db)
    print get_city(db)
~~~

~~~python
{u'_id': ObjectId('5ece6eaed40ce162f32dc6a5'), u'name': u'Chicago'}

{'_id': ObjectId('5ee0e4ca2102c2d949f17070'), 'name': 'Beijing'}
~~~

### 4-4 特性一  Flexible Schema 灵活的模式

1. 数据输入项缺少，或者缺少字段
2. 数据存在多层迭代 literations

以名人信息为例，有人不止一个配偶或者孩子，有些人没有孩子

以城市信息为例，增加了时区字段

MongoDB 用灵活的模式，来适应这种变化

> All of these are valid models for the infobox data! But it's also important to keep in mind that when you are designing your data collections, that you choose a schema that makes it easy to work with.

### 4-5 PyMongo

~~~
\mongodb-win32-x86_64-2012plus-4.2.7\bin> .\mongod.exe --dbpath D:\MongoDB_data
~~~

用于连接数据库和操作数据

程序构架

<img src="README.assets/image-20200528223153204.png" alt="image-20200528223153204" style="zoom:50%;" />

BSON = bit encoding json

~~~
db.cities.find().pretty()
~~~

~~~python
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

tesla_s = {
    "manufacturer" : "Tesla Motors",
    "class" : "full-size",
    "body style" : "5-door liftback",
    "production" : [2012,2013],
    "model years" : [2013],
    "layour" : ["Rear-motor","rear-wheel drive"],
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holehausen"
    }
}

db = client.examples	#database
db.autos.insert(tesla_s)

for a in db.autos.find():
    pprint.pprint(a)
~~~

### 4-6 使用字段在MongoDB中查询

~~~python
from pymongo improt MongoClient
import pprint

clinet = MongoClinet("mongodb://localhost:27017")

db = cliengt.examples

def find():
    autos = db.autos.find({"class" : "full-size"} )
    for a in autos:
        pprint.pprint(a)
        
if __name__ == '__main__':
    find()
~~~

练习题

~~~python
#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
"""

def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche.
    query = {"manufacturer" : "Porsche"}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db(db_name):
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    # For local use
    return db.autos.find(query)


if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print "Printing first 3 results\n"
    import pprint
    for car in results[:3]:
        pprint.pprint(car)
~~~

### 4-7 多字段查询

~~~python
...
def find():
    autos = db.autos.find({"class" : "full-size","manufacturer" : "Tesla Motors"} )
    for a in autos:
        pprint.pprint(a)
~~~

### 4-8 投影查询

也就是设置显示结果的字段

~~~python
...
def find():
    query = {"class" : "full-size","manufacturer" : "Tesla Motors"}
    projecttion = {"_id":0,"production":1}
    autos = db.autos.find(query,projecttion)
    for a in autos:
        pprint.pprint(a)
~~~

_id 如果不赋值0 ，默认自带。

### 4-9 插入数据 insert

~~~python
...
for a in autos:
    db.myautos.insert_one(a)
...
~~~

3.9 https://api.mongodb.com/python/current/tutorial.html#bulk-inserts

~~~python
>>> new_posts = [{"author": "Mike",
...               "text": "Another post!",
...               "tags": ["bulk", "insert"],
...               "date": datetime.datetime(2009, 11, 12, 11, 14)},
...              {"author": "Eliot",
...               "title": "MongoDB is fun",
...               "text": "and pretty easy too!",
...               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
>>> result = posts.insert_many(new_posts)
>>> result.inserted_ids
[ObjectId('...'), ObjectId('...')]
~~~



### 4-10 mongoimport

CMD下操作 直接导入json文件到MongoDB

[官方手册](https://docs.mongodb.com/manual/reference/program/mongoimport/#examples)

~~~bash
mongoimport -d examples -c myautos2 --file autos.json
~~~



### 4-11 运算符 operators 和范围查询 range queries

运算符用于条件筛选，比如大于小于等

~~~mysql
$gt 大于
$lt 小于
$gte
$lte
$ne 不等于
~~~

多个条件

~~~python
query = {"model years" : {"$gte" : 2012 , "$lte" : 2016}}
autos = db.autos.find(query)
~~~

字符串也可以筛选，X开头的城市

~~~python
query = {"name" : {"$gte" : "X" , "$lt" : "Y"}}
cities = db.cities.find(query)
~~~

按日期筛选

~~~python
query = {"foundingDate" : {"$gt" : datetime(1837,1,15) , "lte" : datetime(1840,2,15)}}
~~~

测试题，请记住，2000 年不属于 21 世纪！

### 4-12 exists 字段

类似于Having ，搜索存在这个字段的记录

~~~mongodb
> show databases
admin     0.000GB
config    0.000GB
examples  0.000GB
local     0.000GB
> use examples
switched to db examples
> db.cities.find()
{ "_id" : ObjectId("5ee0e4ca2102c2d949f17070"), "name" : "Beijing" }
{ "_id" : ObjectId("5ee0e54c3798cbe215ef7cfe"), "name" : "Shanghai" }
{ "_id" : ObjectId("5ee0e822a12b7a5f0dca37bb"), "name" : "Shanghai" }
> db.cities.find({"name" : {"$exists" : 1}}).count()
~~~

美化输出

~~~
> db.cities.find({"name" : {"$exists" : 1}}).pretty()
~~~

### 4-13 正则运算符 regex

~~~
> db.cities.find({"name" : {"$regex" : "ha"}}).pretty()
~~~

首字母大小写不敏感

~~~
db.cities.find({"name" : {"$regex" : "[sS]ha"}}).pretty()
~~~

包含两个其中一个单词

~~~
db.cities.find({"name" : {"$regex" : "[sS]ha|^[Bb]"}}).pretty()
~~~

也可以结合投影查询来筛选显示结果

官方资料：

* MongoDB的[regex部分](https://docs.mongodb.com/manual/reference/operator/query/regex/)
* Python 3.8 的[https://docs.python.org/3.8/howto/regex.html](https://docs.python.org/3.8/howto/regex.html)

### 4-14 使用标量查询数组

默认查询，MongoDB会遍历数组字段内的内容，只要有符合项，就会作为显示结果。

### 4-15 $in 运算符

~~~
db.autos.find({"model years" : {"$in" : [2013,2014]}}).pretty()
~~~

### 4-16 $all 运算符

~~~
db.autos.find({"model years" : {"$all" : [2013,2014]}}).pretty()
~~~

$all 表示对应的字段，至少包含所有筛选的条件

### 4-17 点表示嵌套

~~~
db.autos.find({"designer.firstname":{"$regex": "Fra"}}).pretty()
~~~

~~~
db.autos.find({"dimesions.weight" : {"$gt" : 5000}})
query = {"dimensions.width" : {"$gt" : 2.5}}
~~~

### 4-18 更新记录 save

* save 如果有对应的结果就会更新，如果没有对应的_id就会创建一个新的
* findOne 返回匹配结果的第一个
* **findOne()方法不支持pretty()方法**

~~~
> auto["updateDate"] = "2020-06-18"
2020-06-18
> db.autos.save(auto)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
~~~

~~~python
 DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
~~~

~~~
update_many() got an unexpected keyword argument 'multi'
~~~



~~猜测版本问题，脚本save没有更新~~

> 缩进问题，造成main在函数内部

### 4-19 设置与复位 update

~~~
auto = db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"$set" : {"shipDate" : "2020-06-19"}})
~~~



$set

~~~
 db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"$set" : {"shipDate" : "2020-06-19"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
~~~



$unset 逆向删除

~~~
db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"$unset" : {"shipDate" : ""}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
~~~

> 留意update部分更新时要加set运算符

不要用以下

~~~
db.autos.update({"designer.firstname":{"$regex": "Fra"}},{"shipDate" : "2020-06-19"})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
~~~

会让对应的记录更新成

~~~
{ "_id" : ObjectId("5ee0e880a0b58fad5b46ea7c"), "shipDate" : "2020-06-19" }    ikes: 100 })
~~~

### 4-20 多项更新 multi

multi 更新所有匹配记录

~~~
db.autos.update({"designer.firstname":{"$regex" : "Fra"}},{$set:{"updateDate" : "2020-06-19"}},{multi : true})
> db.autos.update({"designer.firstname":{"$regex" : "Fra"}},{$set:{"updateDate" : "2020-06-19"}},{multi : true})
WriteResult({ "nMatched" : 2, "nUpserted" : 0, "nModified" : 2 })
~~~

### 4-21 删除文档 remove dorp

dorp() 是直接删掉整个collection，包括索引等

remove() 可以添加条件

~~~
> db.autos.find({"title" : {"$exists" : 0}}).count()
3
> db.autos.find({"title" : {"$exists" : 1}}).count()
1
~~~



~~~
db.autos.remove({"title" : {"$exists" : 1}})
WriteResult({ "nRemoved" : 1 })
~~~

### 4-22 菜鸟pymongo

#### 查看数据库名称

~~~python
>>> dblist = myclient.list_database_names()
>>> dblist
['admin', 'config', 'examples', 'local']
~~~

#### 插入

~~~python
import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['runoobdb']
mycol = mydb["sites"]
 
mydict = { "name": "Google", "alexa": "1", "url": "https://www.google.com" }
 
x = mycol.insert_one(mydict)
print(x.inserted_id)
~~~

print(x.inserted_id) 获取ID

##### 多条

~~~python
...
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
z = mycol.insert_many(mylist)
print(z.inserted_ids)
~~~



~~~python
[ObjectId('5ef01f53668cecb733b6694b'), ObjectId('5ef01f53668cecb733b6694c'), ObjectId('5ef01f53668cecb733b6694d'), ObjectId('5ef01f53668cecb733b6694e'), ObjectId('5ef01f53668cecb733b6694f')]
~~~

##### 也可以插入时指定ID

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["site2"]
 
mylist = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]
 
x = mycol.insert_many(mylist)
 
# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
~~~

~~~
[1, 2, 3, 4, 5]
~~~

#### 查询

find 和 find_one 方法来查询集合中的数据，它类似于 SQL 中的 SELECT 语句

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
for x in mycol.find():
  print(x)
~~~

##### 投影查询

~~~python
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
  print(x)
~~~

> 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
>
> Projection cannot have a mix of inclusion and exclusion.

##### 条件查询

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
myquery = { "name": "RUNOOB" }
 
mydoc = mycol.find(myquery)
 
for x in mydoc:
  print(x)
~~~

读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 **{"$gt": "H"}** :

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
myquery = { "name": { "$gt": "H" } }
 
mydoc = mycol.find(myquery)
 
for x in mydoc:
  print(x)
~~~

##### 正则表达式

 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 **{"$regex": "^R"}** 

~~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
 
myquery = { "name": { "$regex": "^R" } }
 
mydoc = mycol.find(myquery)
 
for x in mydoc:
  print(x)
~~~~

##### LIMIT

~~~
myresult = mycol.find().limit(3)
~~~

#### 更新

**update_one()** 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段 "$set": 

**update_many()** 更新多条记录

~~~
...
myquery = { "alexa": "10000" }
newvalues = { "$set": { "alexa": "12345" } }
 
mycol.update_one(myquery, newvalues)
 
# 输出修改后的  "sites"  集合
for x in mycol.find():
  print(x)
~~~



~~~
myquery = { "name": { "$regex": "^F" } }
newvalues = { "$set": { "alexa": "123" } }
 
x = mycol.update_many(myquery, newvalues)
~~~

讲解save 和update 的[博文](https://www.iteye.com/blog/chenzhou123520-1637629)

#### 结果排序 **sort**

**sort()** 方法第一个参数为要排序的字段，第二个字段指定排序规则，**1** 为升序，**-1** 为降序，默认为升序

~~~
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
 
mydoc = mycol.find().sort("alexa", -1)
 
for x in mydoc:
  print(x)
~~~

#### 删除

**delete_one()** 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据

**delete_many()** 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据

**delete_many()** 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档

**drop()** 方法来删除一个集合

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
myquery = { "name": "Taobao" }
 
mycol.delete_one(myquery)
 
# 删除后输出
for x in mycol.find():
  print(x)
~~~

删除多个

~~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["sites"]
 
myquery = { "name": {"$regex": "^F"} }
 
x = mycol.delete_many(myquery)
 
print(x.deleted_count, "个文档已删除")
~~~~

~~~python
print("*****multi_delete :")
multi_delete = mycol.delete_many(myquery)
 
print(multi_delete.deleted_count, "个文档已删除")
~~~

mycol.delete_many({})

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
 
x = mycol.delete_many({})
 
print(x.deleted_count, "个文档已删除")
~~~

这个时候还存在 sites 这个集合

~~~
> show collections
sites
~~~



drop（）

~~~python
#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
 
mycol.drop()
~~~

sites 的集合已经不存在了

~~~
> show collections
> 
~~~

### W3C

https://www.w3cschool.cn/mongodb/

## 5 分析数据

### 5-1 聚合框架

内置自带的分析工具 aggregation framework

以推特数据为例：

~~~json
{
    "_id" : ObjectId("5dsds55csdf"),
    "text" : "something interesting ...",
    "entities" : {
        "user_mentions" : [
            {
            "screen_name" : "Somebody_else",
            ...
        	}
    	],
        "urls" : [],
        "hashtags" : []
    },
    "user" : {
        "friends_count" : 544,
        "screen_name" : "somebody",
        "followers_count" : 100,
        ...
    },
       
}
~~~



找出发推最多的用户，步骤：

1. 按照发推的用户进行分组
2. 统计每个用户的发推数量
3. 找出发推最多用户（按照发推数量倒序排序，找出最上方的用户）

~~~python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.twitter

def most_tweets():
    result = db.tweets.aggregate([
        {"$group" : {"_id" : "$user.screen_name","count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}}
    ]
    )
    return result

if __name__ = '__mian__':
    result = most_tweets()
    pprint.pprint(result)
~~~

pymongo 对查询语句，引号必须加，要求严格。命令行查询，引号不用加很多都可以：

~~~json
result = db.sites.aggregate([
    	{$group : {_id : "$name", num_tutorial : {$sum : 1}}},
    	{$sort : {num_tutorial : -1}}
    	])
~~~

~~~json
{ "_id" : "RUNOOB", "count" : 2 }
{ "_id" : "Taobao", "count" : 2 }
{ "_id" : "Facebook", "count" : 2 }
{ "_id" : "Zhihu", "count" : 1 }
{ "_id" : "知乎", "count" : 1 }
{ "_id" : "QQ", "count" : 1 }
{ "_id" : "Github", "count" : 1 }
{ "_id" : "Google", "count" : 1 }
>
~~~

管道，pipline（流水线），也就是查询语句。每个阶段接受一部分文件输入，然后生成一系列文件输出。

### 5-2 聚合管道

利用运算符，构成不同的阶段来实现所要的结果

~~~python
 result = db.tweets.aggregate([
        {"$group" : {"_id" : "$user.screen_name","count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}}
    ]
    )
~~~

测试，使用组

数据demo：

~~~json
{
    "_id" : ObjectId("5304e2e3cc9e684aa98bef97"),
    "text" : "First week of school is over :P",
    "in_reply_to_status_id" : null,
    "retweet_count" : null,
    "contributors" : null,
    "created_at" : "Thu Sep 02 18:11:25 +0000 2010",
    "geo" : null,
    "source" : "web",
    "coordinates" : null,
    "in_reply_to_screen_name" : null,
    "truncated" : false,
    "entities" : {
        "user_mentions" : [ ],
        "urls" : [ ],
        "hashtags" : [ ]
    },
    "retweeted" : false,
    "place" : null,
    "user" : {
        "friends_count" : 145,
        "profile_sidebar_fill_color" : "E5507E",
        "location" : "Ireland :)",
        "verified" : false,
        "follow_request_sent" : null,
        "favourites_count" : 1,
        "profile_sidebar_border_color" : "CC3366",
        "profile_image_url" : "http://a1.twimg.com/profile_images/1107778717/phpkHoxzmAM_normal.jpg",
        "geo_enabled" : false,
        "created_at" : "Sun May 03 19:51:04 +0000 2009",
        "description" : "",
        "time_zone" : null,
        "url" : null,
        "screen_name" : "Catherinemull",
        "notifications" : null,
        "profile_background_color" : "FF6699",
        "listed_count" : 77,
        "lang" : "en",
        "profile_background_image_url" : "http://a3.twimg.com/profile_background_images/138228501/149174881-8cd806890274b828ed56598091c84e71_4c6fd4d8-full.jpg",
        "statuses_count" : 2475,
        "following" : null,
        "profile_text_color" : "362720",
        "protected" : false,
        "show_all_inline_media" : false,
        "profile_background_tile" : true,
        "name" : "Catherine Mullane",
        "contributors_enabled" : false,
        "profile_link_color" : "B40B43",
        "followers_count" : 169,
        "id" : 37486277,
        "profile_use_background_image" : true,
        "utc_offset" : null
    },
    "favorited" : false,
    "in_reply_to_user_id" : null,
    "id" : NumberLong("22819398300")
}
~~~

quiz核心部分

~~~python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$group" : {"_id" : "$source","count" : {"$sum" : 1}}},{"$sort" : {"count" : -1}}]
    return pipeline

def tweet_sources(db, pipeline):
    return [doc for doc in db.tweets.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = tweet_sources(db, pipeline)
    import pprint
    pprint.pprint(result[0])
    assert result[0] == {u'count': 868, u'_id': u'web'}
~~~

### 5-3 聚合运算符

1. $project 投影，可以穿透到想要的字段,对查询结果进行再次运算起别名
2. $macth 匹配筛选
3. $group
4. $sort
5. $skip 比如跳过文件最开始的一部分
6. $limit 与skip相反，只截取到哪个位置
7. $unwind 展开运算符，讲数组分组，比如推文的标签，展开后发给下一个处理阶段

#### $macth

macth 是匹配过滤运算，与find语法类似

~~~python
import pprint
from pymongo import MongoClient

client = MogoClient("mongo://localhost:27017")
db = client.examples

def highest_ratio():
    result = db.teweets.aggregate([
        {"$match" : {"user.friends_count" : {"$gt" : 0},
                     "user.followers_count" : {"$gt" : 0}} 
        },
        {"$project" : {"ratio" : {"$divide" : ["user.followers_count","user.friends_count"]},
                       	"screen_name" : "$user.screen_name"
                      }
        },
        {"$sort" : {"ratio" : -1}},
        {"$limit" : 1}
    ])
    return result

if __name__ = "__main__":
    result = highest_ratio()
    pprint.pprint(result)
~~~

~~~bash
 db.autos.aggregate([{"$match" : {"shipDate" : "2020-06-19"}}])
{ "_id" : ObjectId("5ee0e880a0b58fad5b46ea7c"), "shipDate" : "2020-06-19" }
>
~~~

#### $project

使用注意事项：

1. 利用投影来包含源文件中的字段
2. 每次只能处理一个文件
3. 利用投影在进行数据构型
4. 可以插入计算值，比如比例值
5. 重命名字段
6. 可以进行大规模的数据构型，创建包含子文件的字段

还有官方其他的操作符，比如一个月的第几天，一周的第几天

官方[地址](http://docs.mongodb.org/manual/reference/operator/aggregation/project/#pipe._S_project)