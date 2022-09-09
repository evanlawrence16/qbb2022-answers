 # QBB2022 - Week-1 Homework Excercises
 
 QUESTION 1.
 
 1.1 
 5x = 50000.0  15x=150000.0
 
 1.2 
See Figure_1 and genomemodel.py for the code
 
 1.3 
 7255 bps have not been sequenced. This matches the Poisson distribution very well in which 6814 had not been sequenced.
 
 
 1.4 
 The plot is Figure_2
 There are 8 bps with 0 coverage.
 This matches the Poisson distribution very well in which there are 0 bps.
 
  
  
  
  
QUESTION 2.

this is what I ran for spades 
spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31 -m 1024

2.1 
grep -c '>' contigs.fasta   = 4

2.2 
ran this line ``` awk '/^>/ {print;next;} {print length($0);}' contigs.fasta | uniq ```
then add together length in the headers
=234467

2.3
From the headers I got in the last answer the longest is 105830 bps

2.4
I only got 4 contigs. so the N50 was 47860
  
  
  
QUESTION 3.
  
  
  
QUESTION 4.



 