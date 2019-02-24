# Annotate Bounding Boxes

Given a path to a directory that is associated with a particular class of objects or images, loop through all images in that directory and allow the user to interactively draw rectangles around one object per image. These will be the bounding boxes of an object of a particular class within that image. The bounding boxes are dumped to a pickle file in a local cache directory once iteration is complete.

## How To Use
1. Click, drag, and release to form a rectangle on top of the image that appears in the plot (the rectangle will appear after you release)
  ..* You can do this as many times as you like until you get the box right where you want it
2. Click x to close the plot, and a new one for the next image in the directory will appear
3. Continue this process until you've iterated through every image in the directory
4. Each bounding box will be saved in a dictionary where the key is the file name and the value is the bounding box of form [xmax, xmin, ymax, ymin]
