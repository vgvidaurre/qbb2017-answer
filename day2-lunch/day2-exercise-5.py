#!/usr/bin/env python

import sys

fh = sys.stdin

count = 0
total = 0
for line in fh:
    if line.startswith("@"):
        continue
    else:
        fields = line.split("\t")
        count = count + 1
        total = total + float(fields[4])
print total/count
     

