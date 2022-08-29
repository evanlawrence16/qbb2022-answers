 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn Python.

 2b. wc -l /Users/cmdb/qbb2022-answers/day1-lunch/Copy_genes.chr21.bed
 	=219
	wc -l /Users/cmdb/qbb2022-answers/day1-lunch/Copy_exons.chr21.bed
	=13653
 mean= 62.3
 
 2c. To find the median I would first segregate exons by gene. [if start_exon(n)>start_gene(n) and end_exon(n)<end_gene(n)]. This would allow me to get exons per gene. Then I would sort each gene by number of exons and find the middle number.
 
3b cut -f4 chrom.bed|sort|uniq -c
	= 
305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
 
 3c. make a list where I have every gene name and then gene end-start to get the bp length of each gene. Then sort by state and sum the length per state. Then I would sort to find the state with the max sum. 
 
 
 4b. grep AFR /Users/cmdb/qbb2022-answers/day1-lunch/samples.panel|cut -f2|sort|uniq -c
 =
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
 