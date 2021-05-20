# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:32:49 2021

@author: ADMIN
"""
#Modules
import matplotlib
import matplotlib.pyplot 
import csv
import matplotlib.animation 
import numpy as np
import pandas as pd

#Empty datasets for the data
geology=[]
transport=[]
population=[]
best_site=[]
normalised_data=[]
final=[]

#Scroll bar values
x = 5 #Geology
y = 3 #transport
z = 2 #population


# Loading of the datasets Geology
with open('geology.txt', newline='') as g:
    reader = csv.reader(g, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for line in (reader):
        data_g=[]
        for values in line:
            data_g.append(values)
        geology.append(data_g)
        #matplotlib.pyplot.imshow(geology)
    
    
# Loading of the datasets transport 
with open('transport.txt', newline='') as t:
    reader = csv.reader(t, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
   
    for line in (reader):
        data_t=[]
        for values in line:
            data_t.append(values)
        transport.append(data_t)
        #matplotlib.pyplot.imshow(transport)
    
 
# Loading of the datasets population   
with open('population.txt', newline='') as p:
    reader = csv.reader(p, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
   
    for line in (reader):
        data_p=[]
        for values in line:
            data_p.append(values)
        population.append(data_p)
        #matplotlib.pyplot.imshow(transport)


'''             
#Combining/merging the three datasets..
The scrollbar values resulted to multiple images
'''
for g,t,p in zip(geology,transport,population):
        best_site.append((g+t+p))
        #print(best_site)  

#Determing the highest and lowest value for purposes of standardisation
min_b= np.min(best_site)
max_b= np.max(best_site)
#print(min_b)
#print(max_b)

#Normalisation of the data to values between 0 and 255
normalised_data = np.array([(255*((i-min_b)/(max_b-min_b))) for i in best_site])
   
#List from the normalised

final=list(normalised_data)

matplotlib.pyplot.imshow(final, cmap='gray')
#matplotlib.pyplot.show()


