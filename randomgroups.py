"""
Created on Thu Jul  4 09:14:37 2019

@author: llado
"""

import random
import xlrd 
import numpy as np

random.seed()

# Load students list
loc = ("MAIA3LABS.xlsx") 
wb = xlrd.open_workbook(loc) 
#how many students in each group
numEl = [3,3,2,2,3]

j = 1
for k in range(0,2):
    print ("Lab Group %d:" % (k+1))
    listmaia = wb.sheet_by_index(k) 
    alumnes = []
    for i in range(listmaia.nrows): 
        # print(listmaia.cell_value(i, 0)) 
        alumnes.append(listmaia.cell_value(i, 2)+" "+listmaia.cell_value(i, 1))
    for i in numEl:
        try:    
            selected = random.sample(alumnes,i)
            alumnes = [x for x in alumnes if x not in selected]
            print('Group %d: %s' % (j, selected))
            j +=1
            #print(random.sample(alumnes,numEl[i]))
            input()
        except ValueError: 
            pass
          
    print('end')
