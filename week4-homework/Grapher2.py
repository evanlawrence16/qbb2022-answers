#!/usr/bin/env python3
#import libraries/functions
import sys
import matplotlib.pyplot as plt




#the code starts running here
if __name__ == "__main__":
	effect=[]
	file1 = open('/Users/cmdb/qbb2022-answers/week4-homework/plink.frq', 'r')
	Lines = file1.readlines()
	file1.close()
	for i in range(1,len(Lines)):
		splat=Lines[i].split()[4]
		effect.append(float(splat))
		#print(splat)

plt.hist(effect)
plt.title('Allele Frequencies')
plt.show() 


