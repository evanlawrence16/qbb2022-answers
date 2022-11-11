import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr 

#get values
predicted=[] #predicted value
observed=[] #observed value
name=[] #red gene names
descrip=[] #red globin gene names
for i, line in enumerate(open(sys.argv[1])):
	if line.strip('"').startswith("##"):
		header=np.array(line.strip('"\r\n').split("\t"))
		k562=np.where(header =="E123")[0][0]
	elif not line.strip('"').startswith("#"):
		fields=line.strip('"\r\n').split("\t")
		predicted.append(float(fields[4]))
		observed.append(float(fields[k562]))
		name.append(fields[1])
		descrip.append(fields[2])

#do stats
cor=pearsonr(predicted,observed)

#goi
genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs=[]

for geneoi in genesoi:
    genesoilocs.append(np.where(np.array(name) == geneoi)[0][0])

for i in range(len(descrip)):
	if "hemoglobin subunit" in descrip[i]:
		genesoi.append(name[i])
		genesoilocs.append(i)

#make a graph
fig,ax=plt.subplots()
xs=np.linspace(max(min(predicted),min(observed)),min(max(predicted),max(observed)),100)
ys=0+1*xs
ax.plot(xs,ys,color="cyan")
ax.scatter(predicted,observed,color='pink',s=0.25,alpha=1)
ax.set_xlabel("Predicted K562 expression level, \n10-fold cross validated")
ax.set_ylabel("K562 expression level (log10)")
ax.text(-1.5,3.75,"r^2 = "+str(round(cor.statistic**2,2))+"\n  n="+str(len(observed)),color="purple")
for geneoi,idx in zip(genesoi,genesoilocs):
	ax.text(predicted[idx],observed[idx],geneoi,color="red", fontweight="demi")
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.show()






