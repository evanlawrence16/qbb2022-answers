Really terrific work! Nothing wrong here, but a couple of things that might make your code a liitle more efficient:

When you're constructing your F matrix, and you're checking the scoring matrix, you don't need to loop through the entire scoring matrix until you find the correct cell. It would be faster to know which index in the matrix corresponds to each character (maybe a dictionary could help here)...

You also are being slightly inefficient on checking whether d,h, or v is the max. Instead of checking if d is bigger than the other two, than if h is bigger than the other two, and then having a separate conditional for if there's a tie, just check if d is the max, else check if h is the max, else v has to be. And then that just handles the tie breakers.

10/10
