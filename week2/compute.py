#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math
import fasta

""" 
./compute.py contigs.fasta

"""
"""
real	0m0.007s
user	0m0.001s
sys	0m0.002s

real	0m0.006s
user	0m0.002s
sys	0m0.001s

real	0m3.653s
user	0m4.124s
sys	0m1.126s

"""


nuc_file = open(sys.argv[1])

n_seq = []

for ident, sequence in fasta.FASTAReader(nuc_file):
    n_seq.append(sequence)

print "Number of contigs = " + str(len(n_seq))
    
n_length = []

for i in range(len(n_seq)):
    n_length.append(len(n_seq[i]))
    
print "Max = " + str(max(n_length))
print "Min = " + str(min(n_length))

c_length = 0

for i in n_length:
    c_length += i
    
count = 0
position = 0

for i in n_length:
    if count < c_length/2:
        count += i
        position += 1
    else:
        print "N50 = " + str(n_length[(int(position) - 1)])
        break

print "Mean = " + str(np.mean(n_length))


      
    
    