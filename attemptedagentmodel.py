# -*- coding: utf-8 -*-
"""
Created on Wed May 19 01:46:14 2021

@author: ADMIN
"""
import matplotlib
import csv
import numpy as np
import pandas as pd
import agentframework



geology=[]
transport=[]
population=[]
best_site=[]

with open('geology.txt', newline='') as g:
    reader = csv.reader(g, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for line in reader:
        data_g=[]
        for values in line:
            data_g.append(values)
        geology.append(data_g)
    #print(line)
    
    
with open('transport.txt', newline='') as t:
    reader = csv.reader(t, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
   
    for line in reader:
        data_t=[]
        for values in line:
            data_t.append(values)
        transport.append(data_t)
    #print(line)
    
    
with open('population.txt', newline='') as p:
    reader = csv.reader(p, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
   
    for line in reader:
        data_p=[]
        for values in line:
            data_p.append(values)
        population.append(data_p) 
        
        

#for b,t,p in zip(geology,transport,population):
    #best_site.append(b+t+p)

for g,t,p in zip(geology,transport,population):
    best_site.append(agentframework.Agent(best_site))
        
#matplotlib.pyplot.xlim(0, 340)        
#matplotlib.pyplot.ylim(0, 530)

matplotlib.pyplot.imshow(geology, cmap='gray')
#matplotlib.pyplot.show()