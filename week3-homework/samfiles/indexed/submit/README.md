 # QBB2022 - Week-3 Homework Excercises

first run
```
bwa index /Users/cmdb/qbb2022-answers/week3-homework/sacCer3.fa
```

then run this 10 times
```
bwa mem -R "@RG\tID: A01_09\tSM: A01_09" -o A01_09.sam /Users/cmdb/qbb2022-answers/week3-homework/sacCer3.fa A01_09.fastq
```

run this 10 times
```
samtools sort -@ 4 -O bam -o A01_09.bam A01_09.sam
```

run this 10x
```
samtools index A01_09.bam A01_09.bam.bai
```

run this
```
freebayes -p 1  -f /Users/cmdb/qbb2022-answers/week3-homework/sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam >aligned.vcf
```

run this
```
vcffilter -f "QUAL > 20" aligned.vcf >filtered.vcf
```

run this
```
vcfallelicprimitives -k -g  filtered.vcf >primitive.vcf
```

run
```
conda install snpeff=5.0 -y
snpeff download R64-1-1.99
```

run
```
snpeff ann R64-1-1.99 primitive.vcf >annotated.vcf
```

Then run Grapher.py to graph