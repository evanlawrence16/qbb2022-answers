 # QBB2022 - Week-5 Homework Excercises

run this for both
```
samtools view -b -e qual >=10 D2_Sox2_R1.bam 
```

for macs2s run this
```
MACS2 callpeak -t /Users/cmdb/qbb2022-answers/week5-homework/FilteredD2_Sox2_R2.bam -c /Users/cmdb/qbb2022-answers/week5-homework/FilteredD2_Sox2_R2_input.bam -g 94987271 -B --outdir /Users/cmdb/qbb2022-answers/week5-homework/peaks/
```

to intersect peaks - run
```
bedtools intersect -wa -wb -a /Users/cmdb/qbb2022-answers/week5-homework/peaks/R1/NA_peaks.narrowPeak -b /Users/cmdb/qbb2022-answers/week5-homework/peaks/R2/NA_peaks.narrowPeak >/Users/cmdb/qbb2022-answers/week5-homework/intersected
```

for klf4-run to get intersection
```
bedtools intersect -wa -wb -a /Users/cmdb/qbb2022-answers/week5-homework/intersected -b /Users/cmdb/qbb2022-answers/week5-homework/D2_Klf4_peaks.bed >/Users/cmdb/qbb2022-answers/week5-homework/intersectedKLF
```
run to get number of intersections
```
wc -l /Users/cmdb/qbb2022-answers/week5-homework/intersectedKLF 
```
=41 
```
wc -l /Users/cmdb/qbb2022-answers/week5-homework/D2_Klf4_peaks.bed
```
=60

=68.3 percent overlap


to scale run
```
python scale_bdg.py D0_H3K27ac_treat.bdg SCALEDD0_H3K27ac.bdg 
python scale_bdg.py D2_H3K27ac_treat.bdg SCALEDD2_H3K27ac.bdg 
python scale_bdg.py D2_Klf4_treat.bdg SCALEDD2_Klf4.bdg 
python scale_bdg.py R2_treat_pileup.bdg SCALEDSOX.bdg
```

To crop run
```
 awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' SCALEDD0_H3K27ac.bdg  > CroppedSCALEDD0_H3K27ac.bdg 
 awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' SCALEDD2_H3K27ac.bdg  > CroppedSCALEDD2_H3K27ac.bdg
 awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' SCALEDD2_Klf4.bdg > CroppedSCALEDD2_Klf4.bdg 
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' SCALEDSOX.bdg > CroppedSCALEDSOX.bdg
```

To plot run bdgAGAIN.py - output = fig_1.pdf

to sort, head, and reformat
```
sort -k 5,5rn /Users/cmdb/qbb2022-answers/week5-homework/intersected|head -300|awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > 300Output.fa
```

extract sequences from reference genome
```
samtools faidx mm10.fa -r  /Users/cmdb/qbb2022-answers/week5-homework/300Output.fa > CoordinatesPeaks.fa
```

Motif Finding
```
meme-chip -maxw 7 CoordinatesPeaks.fa
```

