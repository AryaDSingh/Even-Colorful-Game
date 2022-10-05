Q - Do we have to create one single image including both the final line and the final column, with white background?

You do NOT have to (you may, but you are complicating things more than needed).

You can create two separate images associated to the board: one image for the "final line" and one image for the "final column".

To create an initial image, you may want to first use the provided function that returns a black image, and then you can change the colors of the needed pixels to paint with the square colors.

You could also create an image starting from an empty list and appending lists with RGB lists, but this is a more sophisticated algorithm

 

Q- what is the transpose of an image?

An image is a transpose of another if their rows and columns are exchanged.  

So, if we transpose an "horizontal image line" (as referred to in the project, associated to the board) we would obtain a  "vertical  image column", and if we transpose a "vertical image column" we would obtain an "horizontal image line". (the transpose of the transpose is the same as the original) . Using a transpose function applied to an image may be useful for you to  construct a "column" image for the "final column" if you first created an horizontal image line for it.

 

Cheers,
Diana

 