# Feedback day2-lunch

Overall, this script looks good. It performs all of the needed checks, is well commented, and the logic is pretty sound. Just a couple of issues:

- The score field should be an int or float if it isn't a "."
- When you convert the itemRGB entries to ints, the converted value isn't saved, since `t` gets a copy of the item from `itemrgb`. Thus, when `t` gets changed, itemrgb does not. You need something like `for j in range(len(itemrgb)):` and `itemrgb[j] = int(itemrgb[j])`.
- You don't convert the blockSizes or blockStarts fields into ints after you split them
- Because they are copied into new variables, the changes you make to itemrgb, count, sizes, and starts are lost. You need to replace the original value with the new value: `fields[11] = starts` after you make your changes
- You don't have a way to prevent bad lines from being included in the bed list. This might have been a conscious choice, just wanted you to be aware

It's clear that you are decently comfortable with this level of python. You should feel good about this script. Keep it up!
