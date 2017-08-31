#!/usr/bin/env python

"""
Usage: ./replicate.py <samples.csv> <ctab_dir>

- Plot time course of FBtr0331261 for females

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv( sys.argv[1])

soi = df_samples["sex"] == "female"

fpkms = []

for sample in df_samples["sample"][soi]:
    #print sample
    # build complete file path 
    f_name = os.path.join( sys.argv[2], sample, "t_data.ctab" ) 
    # read current sample
    df = pd.read_csv(f_name, sep= "\t")
    
    roi = df["t_name"] == transcript
    # Save FPKM values to the Data Framedf_gene[sample] = np.log(df[roi]["FPKM"] + 1
    
    fpkms.append( df[roi]["FPKM"].values )
    
print fpkms

soi_2 = df_samples["sex"] == "male"

fpkms_2 = []
    
for sample in df_samples["sample"][soi_2]:
    #print sample
    # build complete file path 
    f_name = os.path.join( sys.argv[2], sample, "t_data.ctab" ) 
    # read current sample
    df = pd.read_csv(f_name, sep= "\t")
    
    roi_2 = df["t_name"] == transcript
    # Save FPKM values to the Data Framedf_gene[sample] = np.log(df[roi]["FPKM"] + 1
    
    fpkms_2.append( df[roi_2]["FPKM"].values )
    
print fpkms_2


df_replicates = pd.read_csv(sys.argv[3])

rep_oi = df_replicates["sex"] == "female"

fpkms_3 = []

for sample in df_replicates["sample"][rep_oi]:
    #print sample
    # build complete file path 
    f_name = os.path.join( sys.argv[2], sample, "t_data.ctab" ) 
    # read current sample
    df = pd.read_csv(f_name, sep= "\t")
    
    rep_oi = df["t_name"] == transcript
    # Save FPKM values to the Data Framedf_gene[sample] = np.log(df[roi]["FPKM"] + 1
    
    fpkms_3.append( df[rep_oi]["FPKM"].values )
    
print fpkms_3

rep2_oi = df_replicates["sex"] == "male"

fpkms_4 = []

for sample in df_replicates["sample"][rep2_oi]:
    #print sample
    # build complete file path 
    f_name = os.path.join( sys.argv[2], sample, "t_data.ctab" ) 
    # read current sample
    df = pd.read_csv(f_name, sep= "\t")
    
    rep2_oi = df["t_name"] == transcript
    # Save FPKM values to the Data Framedf_gene[sample] = np.log(df[roi]["FPKM"] + 1
    
    fpkms_4.append( df[rep2_oi]["FPKM"].values )
    
print fpkms_4



labelx = ["10", "11", "12",  "13", "14A", "14B", "14C", "14D"]
x =[0, 1, 2, 3, 4, 5, 6, 7]
w = [ fpkms_3[0], fpkms_3[1], fpkms_3[2], fpkms_3[3]]
y = [ fpkms_4[0], fpkms_4[1], fpkms_4[2], fpkms_4[3]]
    
plt.figure()
plt.ylim(0, 300)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
r, = plt.plot(fpkms, c = "red", label = 'Female')
b, = plt.plot(fpkms_2, c = "blue", label = 'Male')
g, = plt.plot([4,5,6,7], w, 'o', c = "red", label = 'Female Replicates')
z, = plt.plot([4,5,6,7], y, 'o', c = "blue", label = 'Male Replicates')
plt.legend([r, b, g, z], ['Female', 'Male', 'Female Replicates', 'Male Replicates'])
plt.xticks(x, labelx, rotation= 'horizontal')
plt.title("Sxl \n", style = 'italic', fontsize = 20)
plt.savefig( "replicate.png")
plt.close()

