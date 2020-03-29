# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:09:20 2020

@author: eric
"""

import xlsxwriter
import random

workbook = xlsxwriter.Workbook("My_result.xlsx")

worksheet_data = workbook.add_worksheet("data")
worksheet_analysis = workbook.add_worksheet("analysis")

#plusieurs types d'accès
#A1
worksheet_analysis.write("A1","Spock")

#A2
worksheet_analysis.write(
    1, #ligne
    0, #colonne
    "Kirk")
#E1 a E4
worksheet_analysis.write(0,4,42)#en E1 on a 42
worksheet_analysis.write(1,4,55)
worksheet_analysis.write(2,4,68)
worksheet_analysis.write(3,4,12)
worksheet_analysis.write(4,4,"=SUM(E1:E4)")


#format 
success_cell = workbook.add_format(
    {
     "bg_color":"#00ff00",
     "border":1
     }
    )

fail_cell = workbook.add_format(
    {
     "bg_color":"#ff0000",
     "border":1
     }
    )

worksheet_analysis.write(
    5,6,"=PI()",
    success_cell
    )

#serie colonnes
worksheet_analysis.write_column(
    "B1", 
    [3,1,2,5,8,9,10]
     )

#serie lignes
worksheet_analysis.write_row(
    "A8",
    [5,4,9,7,8]
    )


#formattage conditionnel
worksheet_analysis.conditional_format(
    "B1:B8",
    {
     "type":"cell",
     "criteria":"<=",
     "value":5,
     "format":success_cell
     }
    )
xrange = range
#remplissage loop
def fill_columns(columns=[], start_cell=0,end_cell=0,worksheet=None):
    for column_name in columns:
        worksheet_analysis.write_column(
            column_name + str(start_cell)+":"+column_name+str(end_cell), #A1:A10
            random.sample(xrange(10),(end_cell - start_cell +1))
            
            )
fill_columns(
    columns=["A","B","C","D","E"],
    start_cell = 11,
    end_cell = 20,
    worksheet=worksheet_analysis
    
    )





def apply_conditional_format(columns=[], start_cell=0,end_cell=0,worksheet=None, formats=[]):
    for column_name in columns:
        worksheet.conditional_format(
            column_name + str(start_cell) + ":" + column_name + str(end_cell),
            {
                "type":"cell",
                "criteria":"<=",
                "value":5,
                "format": formats[0]
            }
        )

        worksheet.conditional_format(
            column_name + str(start_cell) + ":" + column_name + str(end_cell),
            {
                "type":"cell",
                "criteria":">",
                "value":5,
                "format": formats[1]
            }
        )
 
apply_conditional_format(
    columns = ["A", "B", "C", "D","E"],
    start_cell=11,
    end_cell = 20,
    worksheet = worksheet_analysis,
    formats=[success_cell, fail_cell]
  
    )















workbook.close()