#!/usr/bin/env python

import sys
argu = sys.argv[2]
# opens mapping file made
f = open( sys.argv[1])

#create a dictionary to hold the info from the mapping file
fly_dict = {}

# for each line in mapping file
for line in f:
    #stripped; assigned the two columns of data to variable names
    col = line.rstrip("\r\n").split("\t")
    # remove space 
    flybase = col[0][:-1]
    ac = col[1]
    # add ID's to the dictionary
    if flybase not in fly_dict:
        fly_dict[flybase] = [ac]

# now we moved to the file stringtie ctab file
s = sys.stdin

#initiate a count to allow for only the first 100 to be printed
count = 0

# look through each line in the stringtie file
for line in s:
    # stripped and made it easier to seperate
    fields = line.rstrip("\r'n").split("\t")
    # made sure only values were looked at
    if fields[8] == "gene_id":
        continue
    # looking at the gene_ids in fly_dict and comparing those to the gene_ids in field 8 of the ctab file
    if argu == "skip":
        if fields[8] in fly_dict:
        # allowed of only the first 100 
            if count <= 100:
            # printed the line in a nice way
                fields[8] = fly_dict[fields[8]][0]
                print "\t".join(fields)
                count = count + 1
                
    if argu == "defv":
        if count <= 100:
            if fields[8] in fly_dict:
                fields[8] = fly_dict[fields[8]][0]
                print "\t".join(fields)
                count = count + 1
        else:
            fields[8] = "N/A"
            print "\t".join(fields)
            count = count + 1
            
            
            
            

