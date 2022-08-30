# QBB2022 - Day 1 - Homework Exercises Submission

Excercise 1.
a. awk: illegal field $(), name "nuc" - the variable is not defined within awk so I would define it within awk.

b. Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
 c.  Yes this follows previously reported patterns of nucleotide substitutions.
 
 
 
 
 
 Excecise 2.
 
 a. Promoter regions are not annotated in this data, so no, they are not clearly and objectively defined.
 
 b.  
 #set the state you want to extract
 # I chose state 2 because promoters might flank active transcription sites
type="2"
#extract that state type
awk -v type=$type '{if ($4 == type) {print}}' /Users/cmdb/qbb2022-answers/day1-homework/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > /Users/cmdb/qbb2022-answers/day1-homework/type2.bed

#Get where this sheet and the variant sheet overlap
bedtools intersect -a /Users/cmdb/qbb2022-answers/day1-homework/random_snippet.vcf -b /Users/cmdb/qbb2022-answers/day1-homework/type2.bed >/Users/cmdb/qbb2022-answers/day1-homework/type2snippet.vcf

#set the nucleotide you are looking for SNPs of 
nuc="C"
#filter
awk -v nuc=$nuc '{if ($4 == nuc) {print}}' /Users/cmdb/qbb2022-answers/day1-homework/type2snippet.vcf > /Users/cmdb/qbb2022-answers/day1-homework/output.vcf

#cut out the alternate nucleotides, sort, and unique count them
cut -f5 /Users/cmdb/qbb2022-answers/day1-homework/output.vcf|sort|uniq -c

output=   7 A
   4 G
  24 T

so T is the most common substitution in promoter-like regions where the reference allele is C

D. T is also the most common substitution for C across all states on chromosome 21, so this leads me to believe that promoters are not under any unique selection.



 
 
 
 Excecise 3.

a. #makes a file with the chromosome and position for each snp
awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
#sorts genes in the gene file by chromosome and start position
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
# finds the genes that are closest to one another.
bedtools closest -a variants.bed -b genes.sorted.bed



b. error 1=Error: unable to open file or unable to determine types for file variants.bed
the files are not tab delimited - to fix this I will add the line "perl -p -i -e 's/ /\t/g' input file"

error 2 = Error: Sorted input specified, but the file variants.bed has the following out of order record
to fix this I would make sure both files are sorted the same way

script=
awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
perl -p -i -e 's/ /\t/g' variants.bed
sort -k1,1 -k2,2n variants.bed> variants.bed2
sort -k1,1 -k2,2n /Users/cmdb/data/bed_files/genes.bed> genes.sorted.bed
perl -p -i -e 's/ /\t/g' genes.sorted.bed
bedtools closest -a variants.bed2 -b genes.sorted.bed

c. there are  10293  variants and 731 genes so 14 variants per gene



 
