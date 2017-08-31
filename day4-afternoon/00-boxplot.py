#!/usr/bin/env python

"""
Usage: ./00-boxplot.py <samples.csv> <ctab_dir>

- Boxplot distribution of Sxl transscript in female

"""


import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_samples = pd.read_csv( sys.argv[1])

soi = df_samples["sex"] == "female"

df_gene = pd.DataFrame()

for sample in df_samples["sample"][soi]:
    #print sample
    # build complete file path 
    f_name = os.path.join( sys.argv[2], sample, "t_data.ctab" ) 
    # read current sample
    df = pd.read_csv(f_name, sep= "\t")
    # subset just Sxl rows
    roi = df["gene_name"] == "Sxl"
    # Save FPKM values to the Data Frame
    df_gene[sample] = np.log(df[roi]["FPKM"] + 1)
    
#print df_gene    
    

plt.figure()
plt.boxplot( df_gene.values)
plt.savefig( "boxplot.png")
plt.close()
