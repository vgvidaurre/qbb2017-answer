#!/usr/bin/env python

import sys
import fasta
from itertools import izip
import numpy as np
import pandas as pd
import scipy.stats as sp
import matplotlib.pyplot as plt

p_thr = 0.05

df = pd.read_csv(sys.argv[1], sep = "\t", header = None, names = ["codon", "dN/dS", "diff"])

x = range(len(df))

y = df["dN/dS"]

z_val = sp.zscore(df["diff"])
p_val = 2 * sp.norm.cdf(-1 * np.abs(z_val))

syn_x = [i for i in range(len(p_val)) if p_val[i] < p_thr]
syn_y = [y[i] for i in syn_x]
nons_x = [i for i in range(len(x)) if not i in syn_x]
nons_y = [y[i] for i in nons_x]


plt.figure()
plt.scatter(nons_x,nons_y, s=2)
plt.scatter(syn_x,syn_y, s=2, c='r')

plt.title("Synonymous v. Nonsynonymous Mutations Comparison")
plt.xlabel("Codon #")
plt.ylabel("dN/dS", rotation = 90)

plt.savefig(sys.argv[2] + ".png")
plt.close()



