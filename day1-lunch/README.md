 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn Python.

 2b. wc -l /Users/cmdb/qbb2022-answers/day1-lunch/Copy_genes.chr21.bed
 	=219
	wc -l /Users/cmdb/qbb2022-answers/day1-lunch/Copy_exons.chr21.bed
	=13653
 mean= 62.3
 
 2c. To find the median I would first segregate exons by gene. [if start_exon(n)>start_gene(n) and end_exon(n)<end_gene(n)]. This would allow me to get exons per gene. Then I would sort each gene by number of exons and find the middle number.
 
