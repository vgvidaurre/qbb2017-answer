#!/usr/bin/env python

import sys

"""
plink2 --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno BYxRM_PhenoData_Form.txt --allow-no-sex --linear --allow-extra-chr --all-pheno

"""

phen = open(sys.argv[1])

phen_form = open(sys.argv[2], "w")

for line in phen:
    if line.startswith("\t"):
        phen_form.write("FID")
        phen_form.write("\t")
        phen_form.write("IID")
        phen_form.write(line)
    else:
        fields = line.split("\t")
        sub_field = fields[0].split("_", 1)
        phen_form.write(sub_field[0])
        phen_form.write("\t")
        phen_form.write(sub_field[1])
        phen_form.write("\t")
        phen_form.write("\t".join(fields[1:]))
        
        
        
    