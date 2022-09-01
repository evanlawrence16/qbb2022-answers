#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )
#print(ac)
#print(info)

#plotting type
fig, ax = plt.subplots()
ax.hist( ac, density=True )
#set the axis ranges
plt.xlim([0,5500])
plt.ylim([0.00001,0.002])
plt.yscale('log')
#plt.axis([0,5500,0,10E-2])
plt.title("Allele Frequency "+vcf)
plt.xlabel("Allele Counts")
plt.ylabel("Number of samples");
plt.tight_layout()

fig.savefig( vcf + ".png" )

fs.close()

