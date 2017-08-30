#!/usr/bin/env python
"""
kmer_matcher.py <target.fa> <query.fa> <k>
"""
import sys
import fasta

tar_sub = open(sys.argv[1])
dro_qu = open(sys.argv[2])
k = int(sys.argv[3])

kmer_dict = {}

for ident, sequence in fasta.FASTAReader( tar_sub ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k):
        kmer = sequence[i: i + k]
        
        if kmer not in kmer_dict:
            kmer_dict[kmer] = []
            kmer_dict[kmer].append((ident, i))
        else:
            kmer_dict[kmer].append((ident, i))
            
count = 0
    
for sequence in fasta.FASTAReader(dro_qu).next():
    for i in range( 0, len(sequence) - k):
        kmer_s = sequence[i: i + k]
        if kmer_s in kmer_dict:
            if count < 1000:
                for value in kmer_dict[kmer_s]:
                    count += 1
                    print "\t".join((str(value[0]), str(value[1]), str(i), kmer_s))
                
            
            
            