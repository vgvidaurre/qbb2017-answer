#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#import matplotlip.pyplot as plt


tab = open(sys.argv[1])
avg = []
for line in tab:
    fields = line.rstrip("\r\n").split()
    avg.append(float(fields[4]))
    
fpkms = []
df = pd.read_csv( sys.argv[2], sep= "\t")
fpkms = df["FPKM"].values.tolist()


#print len(fpkms), len
x = avg
y = fpkms

model = sm.OLS(x,y)
results = model.fit()
print (results.summary())


