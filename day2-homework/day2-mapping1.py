#!/usr/bin/env python

# import sys
import sys

f = sys.stdin

# initiate count for the first 100 entries
count = 0 

# to look at each line in the file
for line in f:
    # ensures only the lines with the actual data are being looked at
    if "DROME" not in line:
        continue
    
    else:
        # ensures only the lines with the essential data are being looked at
        if "FBgn" not in line:
            continue
        else:
            # splits each item so that columns can be made 
            row = line.split()
            # ensures on;y the first 100 entries are inlcuded 
            if count <= 100:
                count = count + 1
                # print both fly ID and Uniprot ID are printed in the right order with a tab space between
                print row[-1], "\t", row[-2]
        
            
        
        
        
        
        
        