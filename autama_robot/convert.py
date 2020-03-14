# -*- coding:utf-8 -*-
__version__ = '3.0.3'
"""
@author :   JianqiangHao
@date   :   2020-03-07
"""
import sys
from xlrd import open_workbook # xlrd用于读取xld

workbook = open_workbook(r'location.xls')  # 打开xls文件
sheet_name= workbook.sheet_names()  # 打印所有sheet名称，是个列表
sheet = workbook.sheet_by_index(0)  # 根据sheet索引读取sheet中的所有内容
count_nrows = sheet.nrows  #获取总行数
count_nocls = sheet.ncols  #获得总列数
line_value = sheet.row_values(0)
for i in range(0, count_nrows):
    row = sheet.row_values(i)
    row[10] = row[10].replace("'", "")

    sql = "INSERT INTO `address_info` (`id`, `name`, `parent_id`, `short_name`, `level_type`, `city_code`, `zip_code`," \
          " `merger_name`, `lng`, `lat`, `pin_yin`) VALUES (%s,'%s', %s,'%s',%s, '%s', '%s', '%s',%s, %s,'%s');" % \
          (row[0],row[1],row[2],row[3],int(row[4]),row[5],row[6],row[7],row[8],row[9], row[10])
    print(sql)
