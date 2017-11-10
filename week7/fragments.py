#!/usr/bin/env python

import sys
import numpy as np


""" 
hifive 5c-complete express Nora_Primers.bed -C Nora_ESC_male_E14.counts -P Nora
hifive 5c-heatmap Nora.fcp Nora_frag.heat -i Nora_frag.png -d fragment
hifive 5c-heatmap Nora.fcp Nora_enri.heat -i Nora_enri.png -d enrichment -b 0
hifive 5c-heatmap Nora.fcp Nora_enri.heat -i Nora_enri.png -d enrichment -b 0 -F npz
./fragments.py ctcf_peaks.tsv Nora_Primers.bed > topctcf.txt

"""

def load_hifive():
    data = np.load( 'Nora_enri.heat.npz' )
    return data[ '0.forward' ], data[ '0.reverse' ], data[ '0.enrichment' ]

def ctcf_binding():
    ctcf = []
    for line in open( sys.argv[1] ):
        line = line.rstrip('\r\n').split( '\t' )
        if line[0] == 'chrX':
            ctcf.append( line[1] )
    return ctcf
    
def primer_dic():
    primer = {}
    for line in open( sys.argv[2] ):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == '#chr':
            pass
        else:
            primer[ line[1] + '_' + line[2] ] = line[3]
    return primer

def ctcf_index( primers, ctcf ):
    index = []
    for i, each in enumerate( primers ):
        start, stop = int( each[0] ), int( each[1] )
        for site in ctcf:
            if int( site ) >= start and int( site ) <= stop:
                index.append( i )
                break
    return index

def int_pairs( fwd, rev, enr ):
    fwd_pairs, rev_pairs = [], []
    for f in fwd:
        top_rev, top = None, 0.
        for r in rev:
            if float( enr[ f ][ r ] ) > top:
                top_rev = r
                top = float( enr[ f ][ r ] )
        fwd_pairs.append( ( f, top_rev ) )
    for r in rev:
        top_for, top = None, 0.
        for f in fwd:
            if float( enr[ f ][ r ] ) > top:
                top_for = f
                top = float( enr[ f ][ r ] )
        rev_pairs.append( ( top_for, r ) )
    return fwd_pairs, rev_pairs

def name_int( f, r, pairs, primer, direction ):
    for i in pairs:
        fw_key = str( f[ i[0] ][0] ) + '_' + str( f[ i[0] ][1] )
        rv_key = str( r[ i[1] ][0] ) + '_' + str( r[ i[1] ][1] )
        if direction == 'fwd':
            print '%s\t%s' % ( primer[ fw_key ], primer[ rv_key ] )
        else:
            print '%s\t%s' % ( primer[ rv_key ], primer[ fw_key ] )
def main():
    # load data
    ctcf = ctcf_binding()
    f, r, enr = load_hifive()
    primer = primer_dic()
    ## gives the indices of the ctcf binding sites in the hifive data
    fwd, rev = ctcf_index( f, ctcf ), ctcf_index( r, ctcf )
    ## find the top interacting ctcf pairs
    fwd_pairs, rev_pairs = int_pairs( fwd, rev, enr )
    ## map the top interactions to primer names
    print 'Top interactions with forward primers:'
    name_int(f, r, fwd_pairs, primer, 'fwd' )
    print '\nTop interactions with reverse primers:'
    name_int(f, r, rev_pairs, primer, 'rev' )
        
main()

