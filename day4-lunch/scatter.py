#!/usr/bin/env python

"""
Usage ./scatter.py ~/data/results/stringtie/SRR72893/t_data.ctab ~/data/results/stringtie/SRR72915/t_data.ctab

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import log
import numpy

dict_1 = {}
dict_2 = {}

df = pd.read_csv( sys.argv[1], sep="\t")

transcript = df["t_name"].values.tolist()
fpkm1 = df["FPKM"].values.tolist()
fpkml = []

for item in fpkm1:
    if item == 0.0:
        fpkml.append(log((float(item) + 1.0), 10))
    else:
        fpkml.append(log((float(item) + 1.0), 10))
    

keys = transcript
values = fpkml

dict_1 = dict(zip(keys, values))

df_2 = pd.read_csv( sys.argv[2], sep= "\t")

transcript_2 = df_2["t_name"].values.tolist()
fpkm_2 = df_2["FPKM"].values.tolist()
fpkml_2= []

for item in fpkm_2:
    if item == 0.0:
        fpkml_2.append(log((float(item) + 1.0), 10))
    else:
        fpkml_2.append(log((float(item) + 1.0), 10))

keys = transcript_2
values= fpkml_2

dict_2 = dict(zip(keys, values))


plt.figure()

plt.scatter(dict_1.values(), dict_2.values(), alpha = 0.5)
plt.xlim(0,4)
plt.ylim(0,4)
plt.title("Scatter Plot Comparison \n of FPKM values of SRR072893 vs FPKM values of SRR072915")
plt.xlabel("Log FPKM values of SRR072893")
plt.ylabel("Log FPKM values of SRR072915")
plt.plot(numpy.unique(dict_1.values()), numpy.poly1d(numpy.polyfit(dict_1.values(), dict_2.values(), deg = 1))(numpy.unique(dict_1.values())))
plt.savefig( sys.argv[3] + ".png")
plt.close()