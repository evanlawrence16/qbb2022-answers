#!/usr/bin/env python3

#import libraries/functions
import sys
import matplotlib.pyplot as plt




#the code starts running here
if __name__ == "__main__":
	alldepth=[]

	readdepth1=[]
	readdepth2=[]
	readdepth3=[]
	readdepth4=[]
	readdepth5=[]
	readdepth6=[]
	readdepth7=[]
	readdepth8=[]
	readdepth9=[]
	readdepth10=[]

	allqual=[]
	qualy1=[]
	qualy2=[]
	qualy3=[]
	qualy4=[]
	qualy5=[]
	qualy6=[]
	qualy7=[]
	qualy8=[]
	qualy9=[]
	qualy10=[]

	allfreq=[]
	effect=[]
	file1 = open('/Users/cmdb/qbb2022-answers/week3-homework/samfiles/indexed/annotated.vcf', 'r')
	Lines = file1.readlines()
	file1.close()
	for i in Lines:
		if i.startswith("#"):
			continue
		else:
			splat=i.split(";AF=")[1]
			splatwo=splat.split(";")[0]
			try:
				splatwo=splatwo.split(",")[0]
			except:
				pass
			allfreq.append(float(splatwo))

			splitt=i.split("|")[2]
			effect.append(splitt)

			splot=i.split("\t")
			variants=splot[9:]
			for t in variants:
				depth=t.split(":")[1]
				try:
					alldepth.append(int(depth))
				except:
					alldepth.append(0)
				quality=t.split(":")[5]
				try:
					allqual.append(int(quality))
				except:
					allqual.append(0)

	for i in range(len(alldepth)):
		if i%10==0:
			readdepth1.append(alldepth[i])
			qualy1.append(allqual[i])
		elif i%10==1:
			readdepth2.append(alldepth[i])
			qualy2.append(allqual[i])
		elif i%10==2:
			readdepth3.append(alldepth[i])
			qualy3.append(allqual[i])
		elif i%10==3:
			readdepth4.append(alldepth[i])
			qualy4.append(allqual[i])
		elif i%10==4:
			readdepth5.append(alldepth[i])
			qualy5.append(allqual[i])
		elif i%10==5:
			readdepth6.append(alldepth[i])
			qualy6.append(allqual[i])
		elif i%10==6:
			readdepth7.append(alldepth[i])
			qualy7.append(allqual[i])
		elif i%10==7:
			readdepth8.append(alldepth[i])
			qualy8.append(allqual[i])
		elif i%10==8:
			readdepth9.append(alldepth[i])
			qualy9.append(allqual[i])
		elif i%10==9:
			readdepth10.append(alldepth[i])
			qualy10.append(allqual[i])



#print(max(alldepth))

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

ax3.set_title('Predicted Effects')
ax3.hist(effect)

ax2.set_title('Allele Frequency')
ax2.set_xticks([0,.2,.4,.6,.8])
ax2.hist(allfreq)

ax0.hist(readdepth1,bins=100, alpha=0.2, label='09')
ax0.hist(readdepth2,bins=100, alpha=0.2, label='11')
ax0.hist(readdepth3,bins=100, alpha=0.2, label='23')
ax0.hist(readdepth4,bins=100, alpha=0.2, label='24')
ax0.hist(readdepth5,bins=100, alpha=0.2, label='27')
ax0.hist(readdepth6,bins=100, alpha=0.2, label='31')
ax0.hist(readdepth7,bins=100, alpha=0.2, label='35')
ax0.hist(readdepth8,bins=100, alpha=0.2, label='39')
ax0.hist(readdepth9,bins=100, alpha=0.2, label='62')
ax0.hist(readdepth10,bins=100, alpha=0.2, label='63')
ax0.set_xlim((0,20))
ax0.set_ylim((0,50000))
ax0.set_title('Read Depth')
ax0.legend(bbox_to_anchor=(1, 1))
ax0.legend(title="Variants")



ax1.hist(qualy1,bins=100, alpha=0.5, label='09')
ax1.hist(qualy2,bins=100, alpha=0.5, label='11')
ax1.hist(qualy3,bins=100, alpha=0.5, label='23')
ax1.hist(qualy4,bins=100, alpha=0.5, label='24')
ax1.hist(qualy5,bins=100, alpha=0.5, label='27')
ax1.hist(qualy6,bins=100, alpha=0.5, label='31')
ax1.hist(qualy7,bins=100, alpha=0.5, label='35')
ax1.hist(qualy8, bins=100,alpha=0.5, label='39')
ax1.hist(qualy9, bins=100,alpha=0.5, label='62')
ax1.hist(qualy10, bins=100,alpha=0.5, label='63')
ax1.set_xlim((0,1000))
ax1.set_ylim((0,50000))
ax1.set_title('Quality')
ax1.legend(bbox_to_anchor=(1, 1))
ax1.legend(title="Variants")

plt.show() 


