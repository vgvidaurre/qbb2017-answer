#!/usr/bin/env python

import sys
import fasta
import itertools
from itertools import izip




d_file = open(sys.argv[1])
a_file = open(sys.argv[2])
align_file = open("alignment_nuc1.fa", "w")

for (d_ident, d_seq), (a_ident, a_seq) in itertools.izip(fasta.FASTAReader(d_file), fasta.FASTAReader(a_file)):
    position = 0
    for a in a_seq:
        if a == "-":
            align_file.write("---")
        else:
            align_file.write(d_seq[position: position + 3])
            position = position + 1
            
    align_file.write("\n")        
    print align_file
    
