#!/usr/bin/env python3
#import libraries/functions
import sys
import pandas as pd
import matplotlib.pyplot as plt

def genotocata (row):
	if row['genotype'] == "0/0" :
		return '0'
	elif row['genotype'] == "1/1" :
		return '1'
	else:
		return '.5'


phen = pd.read_csv("/Users/cmdb/qbb2022-answers/week4-homework/gwas_data/CB1908_IC50.txt",header=0,delim_whitespace=True)
phen.set_index('FID').transpose()
phen["Sample"] = phen['FID'].astype(str) +"_"+ phen["IID"].astype(str)


geno = pd.read_csv("/Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf",header=27,delim_whitespace=True)
geno2=geno.loc[geno['ID'] == "rs10876043"]
geno2 = geno2.iloc[: , 9:]
geno2=geno2.set_index('1001_1001').transpose()
geno2 = geno2.reset_index()
geno2.columns =['Sample', 'genotype']


merged = pd.merge(geno2, phen)

merged['genotype2']=merged.apply (lambda row: genotocata(row), axis=1)

df1 = merged[merged['genotype2'] == "0"]
df2 = merged[merged['genotype2'] == "1"]
df3 = merged[merged['genotype2'] == ".5"]


plt.hist(df1['CB1908_IC50'], 
         alpha=0.5,
         label='no mutation')

plt.hist(df2['CB1908_IC50'], 
         alpha=0.5,
         label='homo mutated')

plt.hist(df3['CB1908_IC50'], 
         alpha=0.5,
         label='hetero mutated')


plt.title('Genotype VS Phenotype')
plt.legend(loc='upper right')
plt.xlabel('CB1908_IC50')
plt.show()
