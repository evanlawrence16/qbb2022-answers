# QBB2022 - Day 4 - Homework Exercises Submission


A. each toss in the array a number of coinflips to do. Probs makes a range of values spanning from the first number -here .55 to the last number 1.05 in steps of .05. The decimals==2 means that the values are taken to 2 decimal places. This would be a bigger issue if we were stepping by a smaller number. The [::-1] at the end reverses this array so it iterates from .5 to 1. This is the probability of heads.

C. The more weighted the coin or the more times flipped, the larger the power. This is similar to effect size and sample size in biology.

D. 

a. This study is interested in testing for 'selfish alleles' in humans. Alleles that have a probability >.5 of being passed down to the next generation. 

b. These plots look very similar, except you need fewer coin flips than number of sperm, probably because you are only able to get a limited amount of info per sperm while with coin flips we get either heads or tails.
The x axis here is # of sperm, so your sample size, and the y axis is transmission probability of an allele. 
In my plot # of coin flips corresponds to # of sperm.
Both analyses use binomial tests because we have a claimed value to test in both a fair coin and an unselfish allele, both being .5.