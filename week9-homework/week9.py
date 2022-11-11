import numpy as np
import pandas as pd
import numpy.lib.recfunctions as rfn
import math
import scipy
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
from statsmodels.formula.api import ols 
from statsmodels.stats.multitest import multipletests
from scipy.cluster.hierarchy import ward, dendrogram, leaves_list
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
import statsmodels.api as sm 

#import the data
input_arr = np.genfromtxt("/Users/cmdb/qbb2022-answers/week9-homework/dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
col_names=col_names[1:]
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
names2=np.asarray(filterednames)

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
plt.xlabel("Gene")
plt.ylabel("Cell Type")
plt.show()



#PART 2



#do the linear regression
pval=[]
betas=[]
for row in range(filteredvals.shape[0]):
    list_of_tuples = []
    for i in range(len(col_names)):
        fpkm = filteredvals[row, i]
        name = col_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        list_of_tuples.append((fpkm, stage))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('stage', int)])
    
    model = ols("fpkm ~ stage", data = longdf).fit()
    pval.append(model.pvalues["stage"]) 
    betas.append(model.params["stage"]) 


#plot
sm.qqplot(np.array(pval), dist = scipy.stats.uniform, line='45')
plt.tight_layout()
#plt.show()


#list of diff expressed transcripts
significant_idx = multipletests(pval, alpha=0.1, method='fdr_bh')[0]
diff_stage = names2[significant_idx]
np.savetxt('transcripts_nosex.txt', diff_stage,fmt='%s')


#repeat with sex as covariate
pval=[]
betas=[]
for row in range(filteredvals.shape[0]):
    list_of_tuples = []
    for i in range(len(col_names)):
        fpkm = filteredvals[row, i]
        name = col_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        sex = name_split[0]
        list_of_tuples.append((fpkm, stage, sex))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('stage', int), ('sex', 'S6')])
    
    model = ols("fpkm ~ stage+sex", data = longdf).fit()
    pval.append(model.pvalues["stage"]) 
    betas.append(model.params["stage"]) 


#diff expressed transcripts
significant_idx = multipletests(pval, alpha=0.1, method='fdr_bh')[0]
diff_stage1 = names2[significant_idx]
np.savetxt('transcripts_sex.txt', diff_stage1,fmt='%s')


#overlap
overlap = len(list(set(diff_stage1) & set(diff_stage)))
print(f'overlap: {overlap/len(diff_stage)*100}')


#plot it
plt.clf()
pval=np.asarray(pval)
betas=np.asarray(betas)
plt.plot(betas, -np.log10(pval), '.g', label='Not significant')
plt.plot(betas[significant_idx], -np.log10(pval[significant_idx]), '.y', label='significant')
plt.title('Volcano plot')
plt.xlabel('Beta')
plt.ylabel('p value')
plt.legend()
plt.tight_layout()

plt.show()









