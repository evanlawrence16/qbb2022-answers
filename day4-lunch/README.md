# QBB2022 - Day 4 - Lunch Exercises Submission

1a.
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
    
1b.
Add plotting and plt.show() commands to the echo  "Plotting AC for each .vcf" code and compare the plots that appear with the plots in the cache.

1c
The artifact type gene is interesting because I wonder what it is an artifact from. The TEC type gene is interesting because I don't know what that stands for. The transcribed_processed_pseudogene is also interesting because I wonder what the significance of getting transcribed and processed is.




2d.
All of the plots look pretty similar. This suggests that in general snps have a low density in the sampled population and that our reference genome is close to the norm.


3a.
This program takes 1 input - which is the annotation file of the data you are working with. From there it creates plots of the Snps in different subsections of the genome, including: exons, psuedogenes, protein coding genes, and random snippits.

3b.
This program takes 1 input. The input file must be a .gtf annotation file. Run this program through the terminal. This file requires the python packages sys, matplotlib.pyplot and numpy.

First this file loads in the input file.
Then it parses the file and creates a list of allele counts.
Finally it plots and saves these allele counts on a log scale.

Example output:
*** Creating .bed files for features of interest
--- Creating protein_coding.chr21.bed
--- Creating processed_pseudogene.chr21.bed
--- Creating exons.chr21.bed
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
*** Plotting AC for each .vcf
--- Plotting AC for exons.chr21.bed.vcf
--- Plotting AC for processed_pseudogene.chr21.bed.vcf
--- Plotting AC for protein_coding.chr21.bed.vcf
--- Plotting AC for random_snippet.vcf