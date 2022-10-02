 # QBB2022 - Week-4 Homework Excercises

Run
```
plink --vcf  /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --make-bed
```

Run
```
plink --bfile plink --pca 10
```
Run Grapher.py to get Plot1.png


Run to get the allele frequencies
```
plink --bfile plink --freq --pca 10
```

Run Grapher2.py to get Plot2.png


Run 
```
plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --covar /Users/cmdb/qbb2022-answers/week4-homework/plink.eigenvec --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/CB1908_IC50.txt --allow-no-sex --out assocCB19.txt

```

and Run
```
plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --covar /Users/cmdb/qbb2022-answers/week4-homework/plink.eigenvec --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/GS451_IC50.txt --allow-no-sex --out assocGS45.txt
```

Run Grapher3.py to get the graphs CB19.PNG and GS45.PNG

Run Grapher4.py to get the most significant snp per phenotype.
CB19=rs10876043
GS45=rs7257475

Run Grapher5.py to produce Plot3.png for rs10876043.


The top loci for CB19, on chromosome 12 at position 49190411, was directly upstream from TUBA1A. This gene encodes an alpha tubulin, a subunit of microtubules. It could be that this SNP alters the regulation of this gene, which in turn leads to the observed phenotype.

The top loci for GS45, on chromosome 19 at position 20372113, is quite far from neighbouring genes. The closest gene is "zinc finger protein 826, pseudogene" which is a few kb upstream. In this case I propose that the SNP could be altering some regulatory elements for genes elsewhere and that this disruption ultimately leads to the observed phenotype.


