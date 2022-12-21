# QBB2022 repository - Week-14 Homework Exercises

1-Used the provided script ran - for each file
```
python3 Converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197
```

Ran

```
ktImportText -q Converted/*
```

Throughout the first week Lactobacilliales is by far the most dominant group. This group makes up more than half of the organisms for the entire duration, and Bacillalis is consistently the second most common group. At one point Actinobacteria also come out of nowhere to be one of the more dominant groups.




2

You could look for known highly variable regions in the genome. Additionally you could look for snps to distinguish two organisms of the same species. GC content can also help at some level of classification

```
bwa index metagenomics_data/step0_givendata/assembly.fasta
```

Run - on all my files
```
bwa mem -t 4 /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta  /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR492183_1.fastq /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR492183_2.fastq>SRR492183
```
Sort
```
samtools sort SRR492183_2 -o SRR492183_2.bam
```
Run metaBAT2
```
jgi_summarize_bam_contig_depths --outputDepth depth.txt /Users/cmdb/qbb2022-answers/week14-homework/bam/*
```

Run
```
metabat2 -i /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o Output
```


3

3A. I have 6 bins

3B.
```
grep '>' Output.* -c`
grep '>' ./metagenomics_data/step0_givendata/assembly.fasta -c

```
197/4103= .048 - they represent 4.8 percent of the assembly

3C. I have 3 bins that are large and 3 much smaller bins - from looking at the distribution of organisms in the pie chart this seems correct. However, only 4.8 percent of the assembly is in one of these bins, and from the pie chart I know that there were many single species that made up much larger than 4 percent of my sample, so I wonder why so much of the data is lost.

3D. Since each bin should correspond to a single organism I can blast contigs against a database, and the top hits should all be from the same species. If they were not then my bins may be contaminated. Completeness could be estimated through sequence assembly and then comparison to references.
