#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:07:11 2020

@author: eric
"""
import openpyxl

path ="/media/eric/GLIESE/outil/python/github/mygithub/openpyxl/data3.xlsx"

workbook=openpyxl.load_workbook(path)

sheet = workbook.active #workbook.get_sheet_by_name("Sheet1)

rows = sheet.max_row
cols = sheet.max_column

print(rows)
print(cols)

for r in range(1, rows+1):
    for c in range(1,cols+1):
        print(sheet.cell(row=r, column=c).value, end="    ")
    print()    