# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:49:28 2020

@author: eric
"""

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from xlrd import *
import pandas as pd 
import configparser
import os.path


def createConfigfile():
    config = configparser.ConfigParser()
    config['DEFAULTS'] = {'Filename':'',
                            'SaveDirectory':'',
                            'Colonne':''}
    with open('configuration.ini','w') as configfile:
        config.write(configfile)

def readConfigfile():
    if not os.path.isfile('configuration.ini'):
        createConfigfile()

    config = configparser.ConfigParser()
    config.read('configuration.ini')
    print(config['DEFAULTS']['Filename'])
    localfilename = config['DEFAULTS']['Filename']
    localdirectory = config['DEFAULTS']['SaveDirectory']
    localcolonne = config['DEFAULTS']['Colonne']
    return localfilename, localdirectory,localcolonne

def saveConfigfile():
    localfilename = myfileName.get()
    localdirectoryname = myDirectoryName.get()
    localcolonnename = MycolonneName.get() 
    config = configparser.ConfigParser()

    config['DEFAULTS'] = {'Filename':localfilename,
                            'SaveDirectory':localdirectoryname,
                            'Colonne':localcolonnename}
    with open('configuration.ini','w') as configfile:
        config.write(configfile)

def selectFile():
    try:
        value = askopenfilename()
        myfileName.set(value)
    except ValueError:
        pass

def selectFileDirectory():
    try:
        value = askdirectory()
        myDirectoryName.set(value)
    except ValueError:
        pass        

def splitExcelFile():
    inputfile = myfileName.get()     
    xl = open_workbook(inputfile)    
    mysheetnames = xl.sheet_names()
    path = myDirectoryName.get()+'/'

    for name in mysheetnames:
        writer = pd.ExcelWriter(path+name+'.xlsx')
        parsing = pd.ExcelFile(inputfile).parse(sheet_name=name)
        parsing.to_excel(writer,name)
        writer.save()
    saveConfigfile()
    messagebox.showinfo("Splittage par onglets réussi", "Le fichier Excel a été divisé")

def splitExcelFileByValue():
    inputfile = myfileName.get()     
    xl = open_workbook(inputfile)    
    mysheetnames = xl.sheet_names()
    path = myDirectoryName.get()+'/'
    excel_path= myfileName.get()
    excel_cut= MycolonneName.get()

    df = pd.read_excel(excel_path)
    #print(df)

    #diviser
    split_values = df[excel_cut].unique()
    #print(split_values)
    #print(excel_cut)
    messagebox.showinfo("Résultat Splittage" , "Splittage par la colonne -- " + excel_cut + " -- réussi")

    for value in split_values:
        df1 = df[df[excel_cut]==value]
        #output_file = excel_cut + "_" + str(value) + '_' + excel_path
        output_file = path + excel_cut + "_" + str(value) + '_' + ".xlsx"
        df1.to_excel(output_file,index=False)
    saveConfigfile()
    messagebox.showinfo("Splittage  réussi", "Le fichier Excel a été divisé")

    #for name in mysheetnames:
    #    writer = pd.ExcelWriter(path+name+'.xlsx')
    #    parsing = pd.ExcelFile(inputfile).parse(sheet_name=name)
    #    parsing.to_excel(writer,name)
    #    writer.save()
    #saveConfigfile()
    #messagebox.showinfo("Splittage colonne réussi", "Le fichier Excel a été divisé")


root = Tk()
root.title("Splitteur de fichier Excel")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

myfileName = StringVar()
myDirectoryName = StringVar()
MycolonneName = StringVar()

tempfileName, tempdirectory,tempcolonne = readConfigfile()
myfileName.set(tempfileName)
myDirectoryName.set(tempdirectory)
MycolonneName.set(tempcolonne)

# Select file to split
#Label
ttk.Label(mainframe,text="Nom De Fichier").grid(column=1, row=1,sticky=(W))
#Entry
fileName_entry = ttk.Entry(mainframe, width = 20, textvariable = myfileName)
fileName_entry.grid(column=2, row=1,sticky=(W,E))
ttk.Button(mainframe, text="Sélectionnez un fichier", command=selectFile).grid(column=3, row=1, sticky=W)

#Select target directory
#Label
ttk.Label(mainframe,text="Répertoire de sortie").grid(column=1, row=2,sticky=(E))
fileName_entry = ttk.Entry(mainframe, width = 20, textvariable = myDirectoryName)
fileName_entry.grid(column=2, row=2,sticky=(W,E))
ttk.Button(mainframe, text="Sélectionnez le répertoire", command=selectFileDirectory).grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text="Splittez le fichier", command=splitExcelFile).grid(column=1,columnspan=3,row=3, sticky=(E,W))

#select value for split by value
ttk.Label(mainframe,text="Valeur/titre colonne de decoupe").grid(column=1, row=4,sticky=(W))
column_entry = ttk.Entry(mainframe, width = 20, textvariable = MycolonneName)
#print("t1:"+MycolonneName.get())
column_entry.grid(column=2, row=4,sticky=(W,E))
ttk.Button(mainframe, text="Splittez le fichier par colonne", command=splitExcelFileByValue).grid(column=1,columnspan=5,row=5, sticky=(E,W))
#for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()