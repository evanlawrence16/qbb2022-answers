import numpy as np 
import sys
import matplotlib.pyplot as plt
import random

#get starting inputs
freqA=float(sys.argv[1])
originalfreq=float(sys.argv[1])
popsize=int(sys.argv[2])

#functions to different graphs
def line(allele_freq,starting_freq,popsize):
    plt.plot(allele_freq)
    plt.title("Allele Frequency Over Time in Popsize="+str(popsize))
    plt.ylabel("Allele Frequency, Starting Freq="+str(starting_freq))
    plt.xlabel("Generations")
    plt.ylim([0, 1])
    plt.show()

def hist(fixation,popsize):
    plt.hist(fixation)
    plt.title("Time to Fixation in Popsize="+str(popsize)+" Starting Freq=.5")
    plt.ylabel("Frequency")
    plt.xlabel("Time to Fixation")
    #plt.xlim([min(fixation),max(fixation)])
    plt.show()


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0, 11)
    ax.set_xlabel('Starting Frequency')
    ax.set_ylabel('Generations to Fixation')


def violin(fixation,labels):
    fig, ax = plt.subplots()
    ax.violinplot(fixation,positions=[1,2,3,4,5,6,7,8,9,10])
    set_axis_style(ax, labels)
    plt.title("Time to Fixation by Starting Allele Frequencies")
    plt.show()

#run the simulation and save the output
fixation=[]
freq=[]

#get and sort the list of frequencies
freqs=[]
for i in range(10):
    freqA=round(random.uniform(0, 1),3)
    freqs.append(freqA)
freqa = sorted(freqs, key = float)

#run the simulation
for FreqA in freqa:
    #for i in range(1000):
    #freq.append(str(freqA))
    #originalfreq=freqA
    freq1=[]
    for i in range(100):
        #popsize=random.randrange(10000000)                        
        allele_freq=[]
        n=0
        freqA=FreqA
        while freqA != 1 and freqA != 0:
            allele_freq.append(freqA)
            output=np.random.binomial(popsize, freqA)
            freqA=output/popsize
            #print("freqA= "+str(freqA)+", trials="+str(n))
            n=n+1
        #line(allele_freq,originalfreq,popsize)
        freq1.append(n)
    fixation.append(freq1)
violin(fixation,freqa)
#hist(fixation,popsize)

