#!/usr/bin/env python

# This program takes a fasta file
# Show nucleotide distribution
import sys

seq = "ATGAACAGNTCCCAGTC"

if(len(sys.argv)>1):
    seq = ""
    with open(sys.argv[1], 'r') as fasta:
        for line in fasta:
            line = line.strip()
            if not line.startswith(">"):
                seq = seq + line


seqLength = float(len(seq))

print "Sequence Length:", seqLength

nbA = seq.count('A') 
nbT = seq.count('T')
nbC = seq.count('C')
nbG = seq.count('G')
nbOther = seqLength - (nbA + nbT + nbC + nbG)


# Calculate percentage
print "A: %.1f" % (100 * nbA / seqLength)
print "T: %.1f" % (100 * nbT / seqLength)
print "C: %.1f" % (100 * nbC / seqLength)
print "G: %.1f" % (100 * nbG / seqLength)
print "Others: %.1f" % (100 * nbOther / seqLength)

