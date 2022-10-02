#!/usr/bin/env python3
#import libraries/functions
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import dash_bio
import seaborn as sns
from qqman import qqman

#vectors=np.genfromtxt("/Users/cmdb/qbb2022-answers/week4-homework/assocCB19.txt.assoc.linear",
#	dtype = None, encoding = None,unpack=True, names = ["CHR", "SNP", "BP","A1","TEST","NMISS","BETA","STAT","P"])

df = pd.read_csv("/Users/cmdb/qbb2022-answers/week4-homework/assocGS45.txt.assoc.linear",header=0,delim_whitespace=True)
df.set_index('CHR').transpose()
print(df.loc[df['P'] == min(df.P),'SNP'])
