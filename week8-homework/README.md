 # QBB2022 - Week-8 Homework Excercises
 
 run
 ```
 conda create -n Medaka medaka -y
 pip install whatshap==1.0
 curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/ont_data.tar.gz --output ont_data.tar.gz
tar xzf ont_data.tar.gz
 conda activate Medaka
 cp /Users/cmdb/data/genomes/hg38.fa ./
 ```
 
 Call/phase variants
 chr11
 ```
medaka_variant -i /Users/cmdb/qbb2022-answers/week8-homework/ont_data/methylation.bam -f /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa -r chr11:1900000-2800000 -o Chr11 -p PhasedChr11 -t 6
 ```
 chr14
 ```
 medaka_variant -i /Users/cmdb/qbb2022-answers/week8-homework/ont_data/methylation.bam -f /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa -r chr14:100700000-100990000 -o Chr14 -p PhasedChr14 -t 6
 ```
 chr15
 ```
 medaka_variant -i /Users/cmdb/qbb2022-answers/week8-homework/ont_data/methylation.bam -f /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa -r chr15:23600000-25900000 -o Chr15 -p PhasedChr15 -t 6
 ```
 chr20
 ```
 medaka_variant -i /Users/cmdb/qbb2022-answers/week8-homework/ont_data/methylation.bam -f /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa -r chr20:58800000-58912000 -o Chr20 -p PhasedChr20 -t 6
 ``` 
 Assign haplotypes
 run
 ```
whatshap haplotag  --reference /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa --output-haplotag-list CHR11haplotaglist  -o Chr11Haplotag /Users/cmdb/qbb2022-answers/week8-homework/Chr11/round_0_hap_mixed_phased.vcf.gz /Users/cmdb/qbb2022-answers/week8-homework/Chr11/methylation.bam

whatshap haplotag  --reference /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa --output-haplotag-list CHR14haplotaglist  -o Chr14Haplotag /Users/cmdb/qbb2022-answers/week8-homework/Chr14/round_0_hap_mixed_phased.vcf.gz /Users/cmdb/qbb2022-answers/week8-homework/Chr14/methylation.bam

whatshap haplotag  --reference /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa --output-haplotag-list CHR15haplotaglist  -o Chr15Haplotag /Users/cmdb/qbb2022-answers/week8-homework/Chr15/round_0_hap_mixed_phased.vcf.gz /Users/cmdb/qbb2022-answers/week8-homework/Chr15/methylation.bam

whatshap haplotag  --reference /Users/cmdb/qbb2022-answers/week8-homework/hg38.fa --output-haplotag-list CHR20haplotaglist  -o Chr20Haplotag /Users/cmdb/qbb2022-answers/week8-homework/Chr20/round_0_hap_mixed_phased.vcf.gz /Users/cmdb/qbb2022-answers/week8-homework/Chr20/methylation.bam
 ```
 Split them
 run
 ```
whatshap split --output-h1 Chr11haplo1 --output-h2 Chr11haplo2 /Users/cmdb/qbb2022-answers/week8-homework/Chr11/methylation.bam /Users/cmdb/qbb2022-answers/week8-homework/CHR11haplotaglist
 
whatshap split --output-h1 Chr14haplo1 --output-h2 Chr14haplo2 /Users/cmdb/qbb2022-answers/week8-homework/Chr14/methylation.bam /Users/cmdb/qbb2022-answers/week8-homework/CHR14haplotaglist
  
whatshap split --output-h1 Chr15haplo1 --output-h2 Chr15haplo2 /Users/cmdb/qbb2022-answers/week8-homework/Chr15/methylation.bam /Users/cmdb/qbb2022-answers/week8-homework/CHR15haplotaglist

whatshap split --output-h1 Chr20haplo1 --output-h2 Chr20haplo2 /Users/cmdb/qbb2022-answers/week8-homework/Chr20/methylation.bam /Users/cmdb/qbb2022-answers/week8-homework/CHR20haplotaglist

 ```
 
 
 index these files
 ```
 samtools index Chr11haplo1.bam  Chr11haplo1.bam.bai
 
 samtools index Chr11haplo2.bam  Chr11haplo2.bam.bai
 
 samtools index Chr14haplo1.bam  Chr14haplo1.bam.bai
 
 samtools index Chr14haplo2.bam  Chr14haplo2.bam.bai
 
  samtools index Chr15haplo1.bam  Chr15haplo1.bam.bai
 
 samtools index Chr15haplo2.bam  Chr15haplo2.bam.bai
 
 samtools index Chr20haplo1.bam  Chr20haplo1.bam.bai
 
 samtools index Chr20haplo2.bam  Chr20haplo2.bam.bai
 ```
 