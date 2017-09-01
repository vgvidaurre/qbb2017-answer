#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( sys.argv[1], sep= "\t")
coi = ["chr", "start_promoter", "end_promoter", "t_name"]


soi_p = df["strand"] == "+"

for strand in df["strand"][soi_p]:
    df["start_promoter"] = df["start"] - 500
    df["end_promoter"] = df["start"] + 500

soi_n = df["strand"] == "-"

for strand in df["strand"][soi_n]:
    df["start_promoter"] = df["end"] - 500
    df["end_promoter"] = df["end"] + 500
roineg = df["start_promoter"] 

num = df._get_numeric_data()
num[num < 0] = 0

df[coi].to_csv(sys.argv[2], sep = "\t", index = False, header = False)




