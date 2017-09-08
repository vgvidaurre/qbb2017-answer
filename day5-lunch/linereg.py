#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#import matplotlip.pyplot as plt
avg = []
df_avg = pd.read_csv(sys.argv[1], sep = '\t', header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
df_avg = df_avg.sort_values("t_name")
avg = df_avg["mean0"].values.tolist()
print df_avg
#tab = pc.read_csv(arg)
#avg = []
#for line in tab:
    #fields = line.rstrip("\r\n").split()
    #avg.append(float(fields[4]))
    
fpkms = []
df = pd.read_csv( sys.argv[2], sep= "\t")
df = df.sort_values("t_name")
fpkms = df["FPKM"].values.tolist()
print fpkms



#print len(fpkms), len
x = avg
y = fpkms

model = sm.OLS(x,y)
results = model.fit()
print (results.summary())


