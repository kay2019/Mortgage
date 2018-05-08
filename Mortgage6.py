#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:34:31 2018

@author: kiyoumars
"""

from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import seaborn as sns
from sklearn.svm import SVR



if __name__=="__main__":


    
    with open("sheet3.csv") as csvfile:
        reader=csv.reader(csvfile)
        All_rates=[]
        All_loans=[]

        for row in reader:        
            interest_temp=float(row[2])
            loan_price=float(row[7])

            All_rates.append(interest_temp)
            All_loans.append(loan_price)
 
            
    d = {'Rates': All_rates, 'Loan_price':All_loans}
    df1 = pd.DataFrame(d)
    
    plt.scatter(All_rates, All_loans)


    X=np.array(All_rates)
    X=X.reshape((len(X),1))
    y=np.array(All_loans)
    y=y.reshape((len(y),1))
    
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    y_rbf = svr_rbf.fit(X, y).predict(X)


# #############################################################################
# Look at the results
    lw = 2

    plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')

    plt.xlabel("Rates")
    plt.ylabel("Price value of loan")
    plt.show()

