# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * --> +1
  * would recommend listing all the samples if you're going to say something like "then run this 10 times". Alternatively, you could employ a `for` loop in bash:
  ```
  for ID in 09 11 23 24 27 31 35 39 62 63; do
    bwa mem -t 4 -R "@RG\tID: A01_${ID}\tSM: A01_${ID}" -o A01_${ID}.sam  /Users/cmdb/qbb2022-answers/week3-homework/sacCer3.fa A01_${ID}.fastq
    samtools sort -@ 4 -O bam -o A01_${ID}.bam A01_${ID}.sam
    samtools index -b A01_${ID}.bam A01_${ID}.bam.bai
  done
  ```

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1

4. variant call with freebayes

  * --> +1; perfect!

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * --> +1

9. 4 panel plot (0.25 points each panel)

  * very interesting plot. I like how you colored the distributions by sample ID, but not necessary to do so. You could have just plotted a single pooled distribution
  * --> +1

10. 1000 line vcf

  * --> +1
