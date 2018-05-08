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
    
    
    a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55= ([] for i in range(56))
    b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55= ([] for i in range(56))

    county=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55]
    value=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55]
   


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
    
    