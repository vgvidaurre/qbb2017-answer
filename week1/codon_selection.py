#!/usr/bin/env python

import sys
import fasta
from itertools import izip
import numpy as np
import scipy.stats as sp


"""
Sourced from:
http://www.petercollingridge.co.uk/python-bioinformatics-tools/codon-table
"""

base = ['T', 'C', 'A', 'G']
codon = [a+b+c for a in base for b in base for c in base]
amino_a = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codon, amino_a))


def codon_split(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq), n)]

alignment_file = open(sys.argv[1])

ref_line = codon_split(alignment_file.readline(), 3)

dS = np.zeros(len(ref_line))
dN = np.zeros(len(ref_line))

for line in alignment_file:
    for index, (codon, ref_n) in enumerate(zip(codon_split(line, 3), ref_line)):
        if codon == ref_n: 
            continue
            
        if not codon in codon_table or not ref_n in codon_table:
            continue 
            
        if codon_table[codon] == codon_table[ref_n]:
            dS[index] += 1 
        else:
            dN[index] += 1 
            
diff = dN - dS



for i in range(len(ref_line)):
    if dS[i] > 0:
        print("%s \t  %f \t %f" % (ref_line[i], float(dN[i])/dS[i], diff[i]))

 
    
    