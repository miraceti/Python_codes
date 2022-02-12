from fileinput import filename
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree


myfile = "testlien.xlsx"
mylien1 ="modeleP.xlsx"
mylien2 ="modeleP1.xlsx"
mydir1 = "D:\\eric\\python\\perso\\xls\\lien"
mydir2 = "D:\\eric\\python\\perso\\xls\\lien2"

wb = load_workbook(filename=myfile)

#activation de la feuille
ws = wb["EN COURS"]
ligne = 27
cellule = ws["G"+ str(ligne)]

print(cellule.value)

################################### sol1
print("\nexists = ", mylien1)
ex10 = os.path.exists(mylien1)
print(ex10)

print("\nexists= ", mylien2)
ex11 = os.path.exists(mylien2)
print(ex11)

################################### sol2
print("\nisdir = ", mydir1)
ex20 = os.path.isdir(mydir1)
print(ex20)

print("\nisdir = ", mydir2)
ex21 = os.path.isdir(mydir2)
print(ex21)

################################### sol3
print("\nisfile = ", mylien1)
ex20 = os.path.isfile(mylien1)
print(ex20)

print("\nisfile = ", mydir1)
ex21 = os.path.isfile(mydir1)
print(ex21)

################################### sol4 existe ?
print("\nexists = ", mylien1)
ex20 = Path(mylien1).exists()
print(ex20)

print("\nexists = ", mylien2)
ex21 = Path(mylien2).exists()
print(ex21)

print("\nexists = ", mydir1)
ex22 = Path(mydir1).exists()
print(ex22)

print("\nexists = ", mydir2)
ex23 = Path(mydir2).exists()
print(ex23)

################################### sol5 fichier?
print("\nis_file = ", mylien1)
ex20 = Path(mylien1).is_file()
print(ex20)

print("\nis_file = ", mylien2)
ex21 = Path(mylien2).is_file()
print(ex21)

print("\nis_file = ", mydir1)
ex22 = Path(mydir1).is_file()
print(ex22)

print("\nis_file = ", mydir2)
ex23 = Path(mydir2).is_file()
print(ex23)


################################### sol6 repertoire
print("\nis_dir = ", mylien1)
ex20 = Path(mylien1).is_dir()
print(ex20)

print("\nis_dir= ", mylien2)
ex21 = Path(mylien2).is_dir()
print(ex21)

print("\nis_dir = ", mydir1)
ex22 = Path(mydir1).is_dir()
print(ex22)

print("\nis_dir = ", mydir2)
ex23 = Path(mydir2).is_dir()
print(ex23)


df = pd.DataFrame(ws.values)
print(df[6][13])
print(df[6][14])

print(ws["G28"].hyperlink)
print(ws["G28"].hyperlink.display)

mylien5 = ws["G28"].hyperlink.display
################################### sol1
print("\nexists = ", mylien5)
ex50 = os.path.exists(mylien5)
print(ex50)

mylien6 = ws["G29"].hyperlink.display
################################### sol1
print("\nexists = ", mylien6)
ex60 = os.path.exists(mylien6)
print(ex60)

rows = ws.max_row
columns = ws.max_column
max = rows + 1
i=3
while i < max:
    print("\nLigne : "+ str(i))
    
    ti = ws["G"+str(i)].hyperlink
    print("ti : "  + str(ti))
    
    if ti == None :
        print('PAS DE LIEN')
        c =ws.cell(row=i, column=8)
        c.value = "PAS DE LIEN"
    else:
        mylien6 = ws["G"+str(i)].hyperlink.display
        print("exists = ", mylien6)
        ex60 = os.path.exists(mylien6)
        print(ex60)
        if ex60:
            c =ws.cell(row=i, column=8)
            c.value = "LIEN OK"
        else:
            c =ws.cell(row=i, column=8)
            c.value = "LIEN CASSE"
            
    i+=1
    
wb.save("Out_Liens.xlsx")