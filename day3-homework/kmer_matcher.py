#!/usr/bin/env python
"""
kmer_matcher.py <target.fa> <query.fa> <k>
"""
import sys
import fasta

# open arguments
tar_sub = open(sys.argv[1])
dro_qu = open(sys.argv[2])
k = int(sys.argv[3])

# create and empty dictionary
kmer_dict = {}

#f or every identifier and sequence in tar_sub created kmer and position and identifier into the dictionary
for ident, sequence in fasta.FASTAReader( tar_sub ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k):
        kmer = sequence[i: i + k]
        
        if kmer not in kmer_dict:
            kmer_dict[kmer] = []
            kmer_dict[kmer].append((ident, i))
        else:
            kmer_dict[kmer].append((ident, i))
# initiated count             
count = 0
 
# for every sequence in dro_qu we compared its kmer (kmer_s) to those in dictionary already and printed the kmers that matched, the position in query and target and sequence name   
for sequence in fasta.FASTAReader(dro_qu).next():
    for i in range( 0, len(sequence) - k):
        kmer_s = sequence[i: i + k]
        if kmer_s in kmer_dict:
            # ensure only 1000 lines were outputted
            if count < 1000:
                for value in kmer_dict[kmer_s]:
                    count += 1
                    print "\t".join((str(value[0]), str(value[1]), str(i), kmer_s))
                
            
            
            