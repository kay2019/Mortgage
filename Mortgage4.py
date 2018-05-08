#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:19:11 2018

@author: kiyoumars
"""

import csv
from scipy.stats import chisquare
import numpy as np
from sklearn import datasets, linear_model
from scipy import stats
import statistics
import math
import matplotlib.pyplot as plt
from lightning import Lightning

from numpy import random


if __name__=="__main__":
    

    states = set()
    
    with open("sheet2.csv") as csvfile:
        reader_temp=csv.reader(csvfile)
      
        for row in reader_temp:        
            temp_state=row[0]
            if temp_state !="": states.add(temp_state)
            

    d=len(states)       
    states=list(states)     
    vec1=[]
    vec2=[]
    
    
    
    county=[[]]*56
    value=[[]]*56
   


    with open("sheet2.csv") as csvfile:
        reader_temp=csv.reader(csvfile)
      
        for row in reader_temp:  
            temp_state=row[0]
            temp_county=row[2]
            temp_value=row[5]
            
            if temp_state!="" and temp_county!="" and temp_value!="":
                for i in range(0,d):
                    if states[i] == temp_state: 
                        county[i].append(temp_county)
                        value[i].append(float(temp_value)/100)
   
    for i in range(0,d):
        if len(value[i])==1:
            vec1.append(len(county[i]))
            vec2.append(0.0)
        else:
            vec1.append(len(county[i]))
            vec2.append(statistics.stdev(value[i]))


    colors = np.random.rand(d)
    area = vec2  # 0 to 15 point radii

    
    plt.scatter(states, vec1, s=area, c=colors, alpha=0.5)
    plt.xlabel("Code of state")
    plt.ylabel("Number of counties per state")
    plt.show()
    
    
    lgn = Lightning(ipython=True, local=True)
    
    values = random.randn(len(states))

    lgn.map(states, vec2, colormap='Blues')
    
    
