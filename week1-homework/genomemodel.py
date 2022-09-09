from random import *
import matplotlib.pyplot as plt
import numpy as np

#make a list of 1million zeroes = our genome
genome=[0]*1000000

#make a poisson distribution with lambda 5 and size 1 million 
model=np.random.poisson(lam=5.0, size=1000000)#


#simulate sequencing the genome with 5x coverage
for i in range(50000):

	#pick a random bp between 1 and 1mil to start a 100bp read
	seq=randint(1, 1000000)
	try:
		#add 1 to the genome list from the start bp to +100
		for loc in range(seq,seq+100):
			genome[loc]=genome[loc]+1
	except:
		#unless bp+100 is out of range. Then only add to end
		for loc in range(seq,len(genome)):
			genome[loc]=genome[loc]+1

#plot the histogram
plt.hist(genome, 
         alpha=0.5, # the transaparency parameter
         label='Sequenced genome')
  
plt.hist(model,
         alpha=0.5,
         label='Poisson distribution')
  
plt.legend(loc='upper right')
plt.title('5x coverage sequenced genome vs Poisson distribution')										
plt.xlabel('Times sequenced')
plt.ylabel("Number of bps")
plt.show()

#count zeros in genome and poisson
genome0 = genome.count(0)
poisson0=list(model).count(0)
print(genome0)
print(poisson0)

