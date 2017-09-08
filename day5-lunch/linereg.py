#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#import matplotlip.pyplot as plt
avg1 = []
df_avg1 = pd.read_csv(sys.argv[1], sep = '\t', header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
df_avg1 = df_avg1.sort_values("t_name")
avg1 = df_avg1["mean0"].values.tolist()

avg2 = []
df_avg2 = pd.read_csv(sys.argv[2], sep = '\t', header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
df_avg2 = df_avg2.sort_values("t_name")
avg2 = df_avg2["mean0"].values.tolist()

avg3 = []
df_avg3 = pd.read_csv(sys.argv[3], sep = '\t', header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
df_avg3 = df_avg3.sort_values("t_name")
avg3 = df_avg3["mean0"].values.tolist()

avg4 = []
df_avg4 = pd.read_csv(sys.argv[4], sep = '\t', header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
df_avg4 = df_avg4.sort_values("t_name")
avg4 = df_avg4["mean0"].values.tolist()
#tab = pc.read_csv(arg)
#avg = []
#for line in tab:
    #fields = line.rstrip("\r\n").split()
    #avg.append(float(fields[4]))
    
fpkms = []
df = pd.read_csv( sys.argv[5], sep= "\t")
df = df.sort_values("t_name")
fpkms = df["FPKM"].values.tolist()


total_avg = zip(avg1, avg2, avg3, avg4)

#print len(fpkms), len
y = total_avg
x = fpkms

model = sm.OLS(x,y)
results = model.fit()
print (results.summary())


