#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

"""

tar xf BYxRM_subset.tar.xv 
twobittoFA sacCer3.2bit sacCer3.fa
bwa index sacCer3.fa
bwa mem -R '@RG\tID:39' sacCer3.fa A01_39.fastq > A01_39.out
samtools view -bS A01_09.out | samtools sort - -o A01_09.bam
freebayes -f sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > strain_free.vcf
vcffilter -f "QUAL > 100" strain_free.vcf > strain_free_filtered.vcf
snpEff R64-1-1.86 strain_free_filtered.vcf > snpEff_out
tail -n+83 strain_free_filtered.vcf > strain_free_filt_removeheader.vcf
sort -k 6 -r -n strain_free_filt_removeheader.vcf > strain_filt_sort.vcf

"""

var = open(sys.argv[1])

allele_freq = []
for i in var:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    alf = line[7].split(";")
    alf_2 = alf[3][3:]
    if "," in alf_2:
        alf_3 = alf_2.split(",")
        for i in alf_3:
            allele_freq.append(float(i))
    else:
        allele_freq.append(float(alf_2))
        
plt.figure()
plt.hist(allele_freq, bins = 20)
plt.xlabel("Allele")
plt.ylabel("Frequency")
plt.title("Allele Frequency Spectrum")
plt.savefig(sys.argv[2])
plt.close()