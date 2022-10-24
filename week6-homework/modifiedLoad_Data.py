#!/usr/bin/env python
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.colors as mcolors

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    mat=mat.to_numpy()
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1

    #filter out entries outside of bin range
    data1=np.delete(data1, np.where((data1["F1"]<start_bin) | (data1["F2"]<start_bin) | (data1["F1"]>end_bin) | (data1["F2"]>end_bin)))
    data2=np.delete(data2, np.where((data2["F1"]<start_bin) | (data2["F2"]<start_bin) | (data2["F1"]>end_bin) | (data2["F2"]>end_bin)))
    

    #log transform
    data1["score"]=np.log(data1["score"])-min(np.log(data1["score"]))
    data2["score"]=np.log(data2["score"])-min(np.log(data2["score"]))


    #make the square matrix
    data1b=data1.copy()
    data1b['F1']=data1['F2']
    data1b['F2']=data1['F1']
    data1=np.concatenate((data1b, data1), axis=0)

    data2b=data2.copy()
    data2b['F1']=data2['F2']
    data2b['F2']=data2['F1']
    data2=np.concatenate((data2b, data2), axis=0)

    df1 = pd.DataFrame(data1)
    df1=df1.drop_duplicates()
    nmat=df1.pivot(index='F1', columns='F2', values='score')
    smooth_matrix(nmat)
    df1=nmat


    df2 = pd.DataFrame(data2)
    df2=df2.drop_duplicates()
    nmat=df2.pivot(index='F1', columns='F2', values='score')
    smooth_matrix(nmat)
    df2=nmat


    #difference between the two
    df3 = df1 - df2;
    mat2=df3.to_numpy()

    remove_dd_bg(mat2)
    df3=mat2

    #plot the plot
    norm = mcolors.CenteredNorm()
    figure, axs = plt.subplots(1, 3)
    sns.heatmap(df1,cmap="magma_r",ax=axs[0],vmax=5, cbar=False).set(title='ddCTCF')
    sns.heatmap(df2,cmap="magma_r",ax=axs[1],vmax=5).set(title='dCTCF')
    sns.heatmap(df2,cmap="seismic",ax=axs[2],vmax=5,).set(title='Difference')


    plt.show()
    #print(start_bin)
    #print(end_bin)

if __name__ == "__main__":
    main()






