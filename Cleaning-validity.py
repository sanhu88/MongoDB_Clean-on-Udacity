
"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

你的任务是检查 DBPedia 自动数据文件的“productionStartYear”并获取有效的值。应该完成以下任务：
-    检查字段“productionStartYear”是否包含年份
-    检查该年份是否在 1886 至 2014 范围内
-    将字段值转换为年份（而不是整个日期时间）
-    字段的其他部分和值应该保持不变
-    如果字段的值是如上所述范围内的有效年份，则将该行写入 output_good 文件中
-    如果字段的值不是如上所述的有效年份，则将该行写入 output_bad 文件中
-    你应该采用提供的数据读取和写入方式（DictReader 和 DictWriter），它们将会对标题进行处理。
You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).

你可以编写辅助函数来检查数据并编写文件，但是我们将仅调用包含三个参数（inputfile、output_good、output_bad）的“process_file”文件。

"""
import csv
import pprint
import os

os.chdir('resource')
# FILE_PATCH = os.getcwd()
# print(FILE_PATCH)
# exit()
INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    data_good = []
    data_bad = []
    with open(input_file, "r", encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            # validate URI value
            if row['URI'].find("dbpedia.org") < 0:
                continue

            ps_year = row['productionStartYear'][:4]
            try: # use try/except to filter valid items
                ps_year = int(ps_year)
                row['productionStartYear'] = ps_year
                if (ps_year >= 1886) and (ps_year <= 2014):
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except ValueError: # non-numeric strings caught by exception
                if ps_year == 'NULL':
                    data_bad.append(row)

    # Write processed data to output files
    with open(output_good, "w",newline='', encoding='UTF-8') as good:
        writer = csv.DictWriter(good, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in data_good:
            writer.writerow(row)

    with open(output_bad, "w",newline='', encoding='UTF-8') as bad:
        writer = csv.DictWriter(bad, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in data_bad:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()