#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:34:31 2018

@author: kiyoumars
"""

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
import pandas as pd
import pymc3 as pm
from pymc3.distributions.timeseries import GaussianRandomWalk
import pandas_datareader as pdr
from pykalman import KalmanFilter
from contextlib import ExitStack
import seaborn as sns
import csv
from itertools import chain
import math
from scipy import special






if __name__=="__main__":


    
    with open("sheet3.csv") as csvfile:
        reader=csv.reader(csvfile)
        All_rates=[]
        All_loans=[]
        All_mature=[]
        for row in reader:        
            interest_temp=float(row[2])
            loan_ratio=float(row[8])
            maturity=float(row[5])
            All_rates.append(interest_temp)
            All_loans.append(loan_ratio)
            All_mature.append(maturity)
            
    d = {'Rates': All_rates, 'Loan/Maturity':All_loans}
    df1 = pd.DataFrame(data=d,index=All_mature)
    

    plen = len(df1["Rates"])

    colour_map = plt.cm.get_cmap("YlOrRd")
    colours = np.linspace(0.1, 1, plen) 
    

    scatterplot = plt.scatter(df1["Rates"],df1["Loan/Maturity"],s=30, c=colours, cmap=colour_map,
                          edgecolor="k", alpha=0.8)
    colourbar=plt.colorbar(scatterplot)
    colourbar.ax.set_yticklabels([p for p in df1[::plen//9].index])
    plt.xlabel("Rates")
    plt.ylabel("Loan/Maturity")
    plt.show()


