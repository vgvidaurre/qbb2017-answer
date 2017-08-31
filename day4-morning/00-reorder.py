#!/usr/bin/env python

"""
Usage: ./00=reorder.py <csv_file> <tsv_file>

- Remove header
- Reorder the columns: sex, sample, stage
- Subset "female in sex column
- Convert delimter from comma to tab 

"""

import sys
import pandas as pd

#df2 = pd.DataFrame()
#orint type(df2)
#print df2

df = pd.read_csv( sys.argv[1] )
# Specify desired column order ( list to specify how the columns are set up)
coi = ["sex", "sample", "stage"]
#print df[coi] #[roi]
roi = df["sex"] == "female"
#print roi
df[coi][roi].to_csv( sys.argv[2], sep="\t", header=False, index=False )



# below code is what we have already done; panda does this for us
#f = open( sys.argv[1])

#for i, line in enumerate( f ):
    #if i == 0:
        #continue
    #fields = line.rstrip("\r\n").split(",")
    #if fields[1] == "female":
        #print "\t".join([ fields[1], fields[0], fields[2] ])

#f.close()

