#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( sys.argv[1], sep= "\t")
df_p = pd.DataFrame()
df_n = pd.DataFrame()


soi_p = df["strand"] == "+"
#for line in opens; fields = line,strip; if fields
for strand in df[soi_p]:
    df_p["chromosome"] = df["chr"][soi_p]
    df_p["start_promoter"] = df["start"][soi_p] - 500
    df_p["end_promoter"] = df["start"][soi_p] + 500
    df_p["t_name"] = df["t_name"][soi_p]

soi_n = df["strand"] == "-"

for strand in df[soi_n]:
    df_n["chromosome"] = df["chr"][soi_n]
    df_n["start_promoter"] = df["end"][soi_n] - 500
    df_n["end_promoter"] = df["end"][soi_n] + 500
    df_n["t_name"] = df["t_name"][soi_n]

df_final = df_p.append(df_n)


num = df_final._get_numeric_data()
num[num < 0] = 0



df_final.to_csv(sys.argv[2], sep = "\t", index = False, header = False)




