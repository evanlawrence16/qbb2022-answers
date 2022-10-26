#!/usr/bin/env python
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.colors as mcolors

def main():
    # in1_fname should be 40kb data
    # bin_fname should be bed file with bin locations
    
    in1_fname,bin_fname = sys.argv[1:3]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 10400000
    end = 13400000
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1

    data1=np.delete(data1, np.where((data1["F1"]<start_bin) | (data1["F2"]<start_bin) | (data1["F1"]>end_bin) | (data1["F2"]>end_bin)))

    #log transform
    data1["score"]=np.log(data1["score"])-min(np.log(data1["score"]))

    #make the square matrix
    data1b=data1.copy()
    data1b['F1']=data1['F2']
    data1b['F2']=data1['F1']
    data1=np.concatenate((data1b, data1), axis=0)

    df1 = pd.DataFrame(data1)
    df1=df1.drop_duplicates()
    df1=df1.pivot(index='F1', columns='F2', values='score')

    #get scores
    mat=df1.to_numpy()
    scores2=[]

    for t in range(mat.shape[0]):
        for i in range(mat.shape[1]):
            print(numpy.mean(mat[(i - 5):i, i:(i + 5)]))
            scores2.append(numpy.mean(mat[(i - 5):i, i:(i + 5)]))
    scores = np.array(scores2).reshape(72,72)
    scores = pd.DataFrame(scores)
    scores=scores.T
    print(scores)


    #plot the plot
    norm = mcolors.CenteredNorm()
    figure, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    sns.heatmap(df1,cmap="magma",ax=ax[0],vmax=8).set(title='40KB Data')
    sns.heatmap(scores,cmap="magma",ax=ax[1],vmax=6).set(title='40KB Insulation')
    plt.margins(x=0)
    plt.subplots_adjust(left=0.15,
                bottom=0.1,
                right=1.0,
                top=1.0,
                wspace=0.4,
                hspace=0.0)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()






