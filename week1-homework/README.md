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
```spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31 -m 1024```

2.1 
```grep -c '>' contigs.fasta```   = 4

2.2 
ran this line ``` awk '/^>/ {print;next;} {print length($0);}' contigs.fasta | uniq ```
then add together length in the headers
=234467

2.3
From the headers I got in the last answer the longest is 105830 bps

2.4
I only got 4 contigs. so the N50 was 47860
  
  
  
QUESTION 3.

3.1 
I ran ```dnadiff /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta```
Identity = 99.98

3.2
I ran  ```nucmer --coords /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta```
Longest = 207007
 
3.3
Looking in the out.report file I get
insertions=1 deletions=15
  
  
QUESTION 4.

4.1
looking in the out.delta file the position = 26787-27498

4.2
Looking in out.report the insertion length = 712

4.3
I ran ```samtools faidx /Users/cmdb/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta NODE_1_length_234497_cov_20.506939:26788-27499``

and I got

>NODE_1_length_234497_cov_20.506939:26787-27498
ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTTCTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATTCATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGACCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCGAGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAGCGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACGCCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGCTTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAGCTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTCGTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGTCTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTAGAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGTGC

4.4
I ran  

```python3 /Users/cmdb/qbb2022-answers/week1-homework/asm/dna-decode.py --decode --input /Users/cmdb/qbb2022-answers/week1-homework/message.fasta```

and I got 
The decoded message :  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens...
