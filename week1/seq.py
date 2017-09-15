#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

""" transeq -sequence 1000_homologs.fa -outseq 1000_h_prot.fa """

"""1000_homologs.fa"""


seq_file = open(sys.argv[1])



for line in seq_file:
    r = line.split("\t")
    print ">" + r[0] + "\n" + r[1]
    
    
    
    
    
    
