#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

"""
plink2 --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pca 2 --allow-extra-chr  --mind
usage: ./pca.py plink.eigenvec pca_plot.png

"""

x = []
y = []
for line in open(sys.argv[1]):
    par = line.rstrip("\n").split(' ')
    x.append(float(par[2]))
    y.append(float(par[3]))
    
plt.figure()
plt.scatter(x,y)
plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.title("PCA")
plt.savefig(sys.argv[2])
plt.close()
    
