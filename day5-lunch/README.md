# QBB2022 - Day 5 - Lunch Exercises Submission

PROBLEM 1
```

#get stuff derived from mother and father into two files
infile=/Users/cmdb/Downloads/cmdb-quantbio-main/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv
awk -F\, '$6 == "mother"' "$infile" >> /Users/cmdb/Downloads/cmdb-quantbio-main/assignments/bootcamp/statistical_modeling/extra_data/mother_dnm.csv
awk -F\, '$6 == "father"' "$infile" >> /Users/cmdb/Downloads/cmdb-quantbio-main/assignments/bootcamp/statistical_modeling/extra_data/father_dnm.csv


#get counts by id and add column names for father
infile=/Users/cmdb/Downloads/cmdb-quantbio-main/assignments/bootcamp/statistical_modeling/extra_data/father_dnm.csv
awk -F\, '{if (NR!=1){print $5}}' * "$infile" | sort | uniq -c | sed '1d'|tr ' ' '\,'|sed 's/^,//' |sort -k2 -t','>/Users/cmdb/qbb2022-answers/day5-lunch/father1_dnm.txt
sed '1,2d' /Users/cmdb/qbb2022-answers/day5-lunch/father1_dnm.txt>/Users/cmdb/qbb2022-answers/day5-lunch/fathera_dnm.txt
printf '%s\n%s\n' "number_father,Proband_id" "$(cat /Users/cmdb/qbb2022-answers/day5-lunch/fathera_dnm.txt)" >/Users/cmdb/qbb2022-answers/day5-lunch/father1_dnm.csv

#get counts by id and add column names for mother
infile=/Users/cmdb/Downloads/cmdb-quantbio-main/assignments/bootcamp/statistical_modeling/extra_data/mother_dnm.csv
awk -F\, '{if (NR!=1){print $5}}' * "$infile" | sort | uniq -c | sed '1d'|tr ' ' '\,'|sed 's/^,//' |sort -k2 -t','>/Users/cmdb/qbb2022-answers/day5-lunch/mother1_dnm.txt
sed '1,2d' /Users/cmdb/qbb2022-answers/day5-lunch/mother1_dnm.txt>/Users/cmdb/qbb2022-answers/day5-lunch/mothera_dnm.txt
printf '%s\n%s\n' "number_mother,Proband_id" "$(cat /Users/cmdb/qbb2022-answers/day5-lunch/mothera_dnm.txt)" >/Users/cmdb/qbb2022-answers/day5-lunch/mother1_dnm.csv

#merge mother and father together
join -t "," -j2 /Users/cmdb/qbb2022-answers/day5-lunch/mother1_dnm.csv /Users/cmdb/qbb2022-answers/day5-lunch/father1_dnm.csv>/Users/cmdb/qbb2022-answers/day5-lunch/output1.csv

#sort everything and merge with parental age file
sort -k1 -t',' /Users/cmdb/qbb2022-answers/day5-lunch/aau1043_parental_age.csv>/Users/cmdb/qbb2022-answers/day5-lunch/aau1043_parental_age2.csv
sort -k1 -t',' /Users/cmdb/qbb2022-answers/day5-lunch/output1.csv>/Users/cmdb/qbb2022-answers/day5-lunch/output1a.csv

join -t "," -j1 /Users/cmdb/qbb2022-answers/day5-lunch/aau1043_parental_age2.csv /Users/cmdb/qbb2022-answers/day5-lunch/output1a.csv>/Users/cmdb/qbb2022-answers/day5-lunch/output2.csv
printf '%s\n%s\n' "Proband_id,father_age,mother_age,number_mother,number_father" "$(cat /Users/cmdb/qbb2022-answers/day5-lunch/output2.csv)" >/Users/cmdb/qbb2022-answers/day5-lunch/outputoutputs.csv

```

PROBLEM 2

3.
There is a significant relationship between mother age and number of maternally inherited de novo mutations. 

The R-squared of this relationship is 0.253


4.
There is a significant relationship between father age and number of maternally inherited de novo mutations. 

The R-squared of this relationship is 0.620

6. The number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband

7. 8221.680671


HERE IS THE CODE FOR THIS EXERCISE
```
#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf 
import seaborn as sns
import scipy.stats as stats



#reading in my file
inputa=pd.read_csv("/Users/cmdb/qbb2022-answers/day5-lunch/outputoutputs.csv")

#create and customize scatter plot
plt.scatter(inputa.mother_age,inputa.number_mother)
plt.title('Maternal Age vs Mutations')
plt.xlabel('Maternal Age')
plt.ylabel('Maternal Mutations')

#show scatter plot
plt.show()

#perfroms and prints the linear regression
est= smf.ols(formula='number_mother ~ mother_age', data=inputa).fit() 
print(est.summary())



#create and customize scatter plot
plt.scatter(inputa.father_age,inputa.number_father)
plt.title('Paternal Age vs Mutations')
plt.xlabel('Paternal Age')
plt.ylabel('Paternal Mutations')

#show scatter plot
plt.show()

#perfroms and prints the linear regression
est= smf.ols(formula='number_father ~ father_age', data=inputa).fit() 
print(est.summary())


#plot the histogram
plt.hist(inputa["number_father"], 
         alpha=0.5, # the transaparency parameter
         label='Paternal')
  
plt.hist(inputa["number_mother"],
         alpha=0.5,
         label='Maternal')
  
plt.legend(loc='upper right')
plt.title('Maternal vs Paternal Mutations per Proband')
plt.xlabel('Mutations')
plt.ylabel("Number of probands")
plt.show()


#tests signficance between the two populations using a paired t-test
print(stats.ttest_rel(inputa["number_mother"], inputa["number_father"]))


#predicts the number of mutations based on father's age using previous regression
print(est.predict({'father_age': [50.5]}))
```