# day 4 homework feedback

Your heatmaps are good!

While you have submitted both heatmaps, I only see code creating one of the heatmaps.

The assignment does ask you to incorporate the nested for loop and storing the power within the `run_experiment()` function rather than calling that function repeatedly. What you've done works and leads to the same conclusions, but consider how you might edit the function to incorporate the new code. While your results will be the same every time your script is run, will your results be the same compared to someone who only calls the `run_experiment()` function once therefore only sets the random seed once?

(Completely optional feedback: Do you like having the values displayed such that the y-axis goes from the top down, increasing number of coin tosses as you move down the axis? and relatedly, such that the x-axis goes from the left to the right, decreasing the probability of heads as you move across the axis? This is due to the way that you reshape your list to a numpy 2D array. If you reshape your list differently or create a 2D array and store the probability of heads in the rows (first axis) and the number of tosses in the columns (second axis) in your numpy 2d storage array, will the axes be displayed differently and more intuitively?)

Good comments/observations in your README. Very insightful comment!! -- " The more weighted the coin or the more times flipped, the larger the power. This is similar to effect size and sample size in biology"
