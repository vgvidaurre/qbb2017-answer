#!/usr/bin/env python

import sys

tax= {}

for line in open(sys.argv[1]):
    if line.strip().split("\t")[1] not in tax:
        tax[line.strip().split("\t")[1]]=1
    else:
        tax[line.strip().split("\t")[1]]+= 1
for t in tax:
    print str(tax[t]) + "\t" + "\t".join(t.split(";"))
    
