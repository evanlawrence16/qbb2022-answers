 # QBB2022 - Week-6 Homework Excercises
 
Part 1:
What percentage of reads are valid interactions (duplicates do not count as valid)? 
single deletion = 34.8 percent are valid and not duplications 
double deletion = 32.3 percent are valid and not duplications

What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)? 
The majority consist of dangling end pairs - this means the fragments didn't ligate with anything and both reads are from a single fragment.

Part 2:
for subsampled data run
```
python3 /Users/cmdb/qbb2022-answers/week6-homework/modifiedLoad_Data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed /Users/cmdb/qbb2022-answers/week6-homework/heatmap
```
output= figure1


for full data run
```
python3 /Users/cmdb/qbb2022-answers/week6-homework/modifiedLoad_Data.py /Users/cmdb/qbb2022-answers/week6-homework/matrix/ddCTCF_full.6400.matrix /Users/cmdb/qbb2022-answers/week6-homework/matrix/dCTCF_full.6400.matrix /Users/cmdb/qbb2022-answers/week6-homework/matrix/6400_bins.bed /Users/cmdb/qbb2022-answers/week6-homework/heatmap
```

output= figure2

Insulation Scores

