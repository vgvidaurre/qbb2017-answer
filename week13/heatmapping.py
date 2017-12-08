#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""

Usage: 

./heatmapping.py abundance_table.tab

"""

df = pd.read_csv(sys.argv[1], sep = '\t', index_col = 0)

samples = ['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']

df_2 = df[samples]

label = {'bin.1': 'Staphylococcus haemolyticus', 'bin.2': 'Leuconostoc citreum', 'bin.3': 'Staphylococcus lugdenensis',\
            'bin.4': 'Enterococcus faecalis', 'bin.5': 'Cutibacterium avidum', 'bin.6': 'Staphylococcus epidermidis',\
            'bin.7': 'Staphylococcus aureus', 'bin.8': 'Anaerococcus prevotii'}
bin_label = []

for i in df_2.index.tolist():
    bin_label.append(label[i])


plt.figure()
plt.imshow(df_2, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Genome Abundance of Gut bacteria")
plt.colorbar(label = 'Abundance')
plt.yticks( [x for x in range(len(bin_label)) ], bin_label)
plt.xticks( range(len( df_2.columns)), df_2.columns, rotation = 'vertical')
plt.tight_layout() 
plt.savefig("Gut_bacteria_heatmap.png") # Save the image
plt.close()

