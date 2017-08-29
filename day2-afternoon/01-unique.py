#!/usr/bin/env python

# Print the unique gene names from a t_data.ctab file

import sys 

# gene_names_seen = []
# gene_names_seen = set()
gene_names_counts = {}

for i, line in enumerate( sys.stdin ):
    if i == 0:
        continue
    # Remove any newlines from end of line,
    # then split using tab as delimeter
    # -> List of strings representing fields 
    fields = line.rstrip("\r\n").split("\t")
    gene_name = fields[9]
    t_name = fields[5]
    fpkm = fields[11]
    if gene_name not in gene_names_counts:
        # gene_names_seen.append( gene_name)
        gene_names_counts[gene_name] = [fpkm]
    else:
        # gene_names_counts[gene_name] += 1
        gene_names_counts[gene_name].append( fpkm )
# for gene_name in gene_names_seen:
    # print gene_name
for key, value in gene_names_counts.iteritems():
    print key, value
    