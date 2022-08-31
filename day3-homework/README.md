# QBB2022 - Day 3 - Homework Exercises Submission

QUESTION 1
run sequentially in terminal
```
#converted vcf to plink readable files
plink --vcf /Users/cmdb/qbb2022-answers/day3-homework/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf --make-bed

#make the eigenvectors
plink --bfile /Users/cmdb/qbb2022-answers/day3-homework/plink/plink --pca 3

```
