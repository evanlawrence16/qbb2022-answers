import numpy as np
import pandas as pd
import numpy.lib.recfunctions as rfn
import math
import scipy
from scipy.cluster.hierarchy import ward, dendrogram, leaves_list
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
import pandas as pd

#import the data
input_arr = np.genfromtxt("/Users/cmdb/qbb2022-answers/week9-homework/dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = [input_arr.dtype.names]

#remove the names
inputlist=input_arr.tolist()
nonames=[]
names=[]
for i in inputlist:
    names.append(i[0])
    i=i[1:len(i)]
    nonames.append(i)

#make 2d array
d2arr = np.asarray(nonames)

#get rid of transcripts/names below a median value
filteredvalues=[]
filterednames=[]
for i in range(len(d2arr)):
    if np.median(d2arr[i])>0:
        d2arr2=d2arr[i].tolist()
        filterednames.append(names[i])
        filteredvalues.append(d2arr2)

#log transform values
transformed=[]
for i in filteredvalues:
    rows=[]
    for t in i:
        val=math.log2(t + 0.1)
        rows.append(val)
    transformed.append(rows)

filteredvals = np.asarray(transformed)
print(filteredvals)

#cluster
#leves gives me the indexes to rearrange by
Z=scipy.cluster.hierarchy.linkage(filteredvals, method='ward', metric='euclidean', optimal_ordering=False)
leves1=leaves_list(Z)

Z1=scipy.cluster.hierarchy.linkage(filteredvals.T, method='ward', metric='euclidean', optimal_ordering=False)
leves2=leaves_list(Z1)

#rearrange filteredvals to hierarchy order
output = filteredvals[:,leves2]
output=output[leves1,:]

#plot dendrogram 2
fig = plt.figure(figsize=(10, 10))
dn = dendrogram(Z)
plt.title("Dendrogram of gene expression")
plt.show()


#plot dendrogram
fig = plt.figure(figsize=(10, 10))
dn = dendrogram(Z1)
plt.title("Dendrogram of cell types")
plt.show()


#plot heatmap
plt.imshow(output.T, cmap='hot', interpolation='nearest', aspect='auto')
plt.title("Clustered heatmap of gene expression")
plt.show()



#print(transformed)
#filteredvals = np.asarray(filteredvalues)
