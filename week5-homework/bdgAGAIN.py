#!/usr/bin/env python
from bdg_loader import load_data
import matplotlib.pyplot as plt
import numpy as np

#load the data with the provided function
D0=load_data("/Users/cmdb/qbb2022-answers/week5-homework/CroppedScaled/CroppedSCALEDD0_H3K27ac.bdg")
D2=load_data("/Users/cmdb/qbb2022-answers/week5-homework/CroppedScaled/CroppedSCALEDD2_H3K27ac.bdg")
KLF=load_data("/Users/cmdb/qbb2022-answers/week5-homework/CroppedScaled/CroppedSCALEDD2_Klf4.bdg")
SOX=load_data("/Users/cmdb/qbb2022-answers/week5-homework/CroppedScaled/CroppedSCALEDSOX.bdg")

#plot the data and label axes
fig, axs = plt.subplots(4)

axs[0].plot(SOX["X"],SOX["Y"])
axs[1].plot(KLF["X"],KLF["Y"])
axs[2].plot(D0["X"],D0["Y"])
axs[3].plot(D2["X"],D2["Y"])

plt.xlabel("BP Location")
axs[0].set(ylabel="Sox_R1")
axs[1].set(ylabel="Klf4")
axs[2].set(ylabel="D0_H3K27ac")
axs[3].set(ylabel="D2_H3K27ac")


fig.suptitle('chr17 35,639,000 - 35,644,000')
fig.tight_layout()
plt.show()