#!/usr/bin/env python
import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math


""" 
lastz reference.fasta velvet_contigs.fa --chain --format=general:zstart1,end1,name2,size2 > velvet_lastz.tsv

sort -k 1,1 -n dotplot_good_cov_velvet.tsv > sorted_dotplot_good_cov_velvet.tsv


"""

lastz_file = open(sys.argv[1])

count = 1
plt.figure()
for i in lastz_file:
    if "zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count,count+float(fields[3])],[float(fields[0]),float(fields[1])])
        count += float(fields[3])

plt.xlabel("Contig")
plt.ylabel("Position")
plt.ylim((0,100000))
plt.xlim((0,100000))
#make some sort of tick mark with low font
plt.savefig(sys.argv[2])
plt.close()