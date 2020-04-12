#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:56:57 2020

@author: eric
"""
import pandas as pd

data  = pd.DataFrame({'Fruits':["pommes","poires","oranges","peches","citrons"]})

datatoexcel = pd.ExcelWriter("fromPandas.xlsx",engine='xlsxwriter')

data.to_excel(datatoexcel,sheet_name='Sheet1')


datatoexcel.save()