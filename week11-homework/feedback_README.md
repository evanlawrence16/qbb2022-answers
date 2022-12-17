This is great Evan! Just one minor comment:

It looks like you may be running leiden twice, and the second time adding the clusters to a column called `clusters`. This would be fine (as it doesn't really do anything), except that it looks like the second time you do it, you're adding `resolution=0.5`. I think the default resolution is 1, so your two different columns may be slightly different. The issue is if you determined cell types from the FIRST leiden clustering, and then applied those labels to the second leiden clustering, the labels may be wrong. No points off, just be careful.

(10/10)
