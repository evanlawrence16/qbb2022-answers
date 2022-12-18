## Week 13

0 + 1 + 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1 = 8 out of 10 points possible

1. Wright Fisher simulation is a function

* the simulation itself is not a function

2. simulation uses starting allele frequency and population size as input

3. simulation uses `numpy.random.binomial` to draw allele count samples

4. simulation stops when one allele is fixed

5. simulation returns a list of allele frequencies at each generation

6. line plot generation number x-axis and allele frequency y-axis with notated starting allele frequency and pop size as well as labeled axes; 0.5 pts for notes/labels

7. time to fixation histogram for starting allele freq of 0.5 and pop size of 100 with at least 1000 independent runs

8. line plot for fixation time (y-axis) vs N (x-axis) for a starting allele frequency of 0.5 and varied population size (at least 6 different from 100 - 10mil). Label ticks

* the plots you submitted weren't what we were asking for. We were asking for the varied population sizes to correspond to ticks on the x-axis, and the corresponding fixation time to correspond to ticks on the y-axis. The fixation time, rather than the allele frequency trajectories.

9. step 5 running the simulation for a range of 10 starting allele frequencies from 0 to 1. 100 simulations each

10. step 5 plot for variability in the time to fixation for each starting allele frequency. label the ticks and notate population size (0.5 pts for notes and labels)

Possible bonus points

1. Introduce selection in the simulation function

2. plot the allele frequency trajectory, notating selection coefficient, etc.

3. plot selection coefficient vs time to fixation for fixed population size, note population size on plot
