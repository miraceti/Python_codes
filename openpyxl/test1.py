import sys
import openpyxl
from openpyxl.styles import Font
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

#on execute en msdos : python test1.py test1.xlsx    : ceci execute le script sur le xls
script_name = sys.argv[0]
param = sys.argv[1]

print(script_name)
print(param)

for arg in sys.argv:
    print(arg)
    
#on ouvre un nouvel XLSX et en A on écrit HELLO taille 12
# workbook = openpyxl.Workbook()
# sheet = workbook.active

# load existing spreadsheet
wb = load_workbook(str(param))
ws = wb.active
cell1 = ws["A1"]
cell1.font = Font(size=12)
cell1.value = "HELLO"

#on écrit en A2 FROM taille 14 et couleur ROUGE
cell2 = ws["A2"]
cell2.font = Font(name="Arial", size=14, color ="00FF0000")
ws["A2"] =  "FROM"

#on écrit en A3 OPENPYXL taille 16 couleur VERT
cell3 = ws["A3"]
cell3.font=Font(name="Tahoma", size=16, color="00339966")
ws["A3"] = "OPENPYXLS"


#on écrit en A3 OPENPYXL taille 16 couleur VERT
cell4 = ws["B3"]
cell4.font=Font(name="Tahoma", size=16, color="00339966")
ws["B3"] = 32.56
ws["B3"].number_format ='# ##0.00 €'


ws["C3"].number_format ='# ##0.00 €'
ws["D3"].number_format ='# ### ##0.00 €'

#pour toute la colonne F
last_cell = 100
for col in range(6, ws.max_column+1):
    for row in range (1, last_cell):
      ws.cell(column=col, row=row).number_format = '# ### ##0.00 €'

ws.column_dimensions["F"].width = 20

wb.save("test1.xlsx")