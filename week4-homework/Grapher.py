#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

#gets data from my text files
vectors=np.genfromtxt("/Users/cmdb/qbb2022-answers/week4-homework/plink.eigenvec",
	dtype = None, encoding = None,unpack=True, names = ["sample", "family", "vec1","vec2","vec3","vec4","vec5","vec6","vec7","vec8","vec9","vec10",])

#sets which parts of the data to graph
plt.scatter(vectors[2],vectors[3])

#labels the axes
plt.title('genetic relatedness between the cell lines ')
plt.ylabel('PC2')
plt.xlabel('PC1')

#show the plot
plt.show()



