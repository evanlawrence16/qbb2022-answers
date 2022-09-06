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