#!/usr/bin/env python

import sys

totalspan = 0
genecnt = 0

for line in sys.stdin:
    #line = line.rstrip()
    #print line
    mylen = int(line)
    totalspan += mylen
    genecnt += 1
    
print "there are %d gene, with a total span of %d, average gene len is %f" % (genecnt, totalspan, float(totalspan/genecnt))


