#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <samples.csv> <ctab_dir>

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
    

    
plt.figure()
plt.plot(fpkms)
plt.savefig( "timecourse.png")
plt.close()

