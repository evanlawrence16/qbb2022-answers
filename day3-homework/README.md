# QBB2022 - Day 3 - Homework Exercises Submission

QUESTION 1

run sequentially in terminal
```
#converted vcf to plink readable files
plink --vcf /Users/cmdb/qbb2022-answers/day3-homework/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf --make-bed

#make the eigenvectors
plink --bfile /Users/cmdb/qbb2022-answers/day3-homework/plink/plink --pca 3

```


QUESTION 2

my code
```
#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

#gets data from my text files
vectors=np.genfromtxt("/Users/cmdb/qbb2022-answers/day3-homework/plink/plink.eigenvec",
	dtype = None, encoding = None,unpack=True, names = ["sample", "family", "vec1","vec2","vec3",])

#sets which parts of the data to graph
plt.scatter(vectors[2],vectors[3])

#labels the axes
plt.ylabel('PC2')
plt.xlabel('PC1')

#show the plot
plt.show()
```

The points seem to separate into 3 distinct clusters. Maybe this relates to the superfamily they originate from? 



QUESTION 3

here is the code I used to get the plots
```
#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


sns.set(style='ticks')

#gets data from my text files
vectors=np.genfromtxt("/Users/cmdb/qbb2022-answers/day3-homework/join/joined.txt",
	dtype = None, encoding = None)

#makes the array into a csv
df = pd.DataFrame(vectors, columns = ["sample", "pop", "super_pop", "gender", "subsample", "vec1", "vec2", "vec3"])
#formatting and exporting the csv
df = df.iloc[1: , :]
df.to_csv("/Users/cmdb/qbb2022-answers/day3-homework/join/dataframe.csv",index=False)
#loading the csv
dff=pd.read_csv("/Users/cmdb/qbb2022-answers/day3-homework/join/dataframe.csv")

#plotting the data
ax=sns.scatterplot(x='vec1', y='vec2', data=dff, hue="super_pop")
ax.set(xlabel='PC1', ylabel='PC2', title="SNP PCA by super pop")
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

plt.show()
```


