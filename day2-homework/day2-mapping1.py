#!/usr/bin/env python

import sys

f = sys.stdin

count = 0 
for line in f:
    if "DROME" not in line:
        continue
    
    else:
        if "FBgn" not in line:
            continue
        else:
            
            row = line.split()
            if count <= 100:
                count = count + 1
                print row[-1], "\t", row[-2]
        
            
        
        
        
        
        
        