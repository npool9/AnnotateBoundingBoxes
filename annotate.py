import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pickle
import os
from PIL import Image
import numpy as np


class Annotate:

    def __init__(self):
        self.ax = plt.gca()
        self.rect = Rectangle((0, 0), 1,  1, linewidth=1, edgecolor='r', facecolor='none')
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)

    def on_press(self, event):
        self.x0 = event.xdata
        self.y0 = event.ydata

    def on_release(self, event):
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.ax.figure.canvas.draw()


if __name__ == "__main__":
    # FIXME: if your dataset is configured differently, change the way that looping through subdirectories is happening
    #  here
    print("Loading images into memory...")
    # Hard-code the directory of data that you'd like to annotate with bounding boxes. Execution completes when you're
    #  completely done iterating through every image in the directory
    data_path = '/Volumes/TheShip/Data/CoalPlants/PlantImages'
    path_list = []
    image_list = []
    for image in os.listdir(data_path):
        if not image.startswith('.'):
            path_list.append(data_path + '/' + image)
            image_list.append(np.array(Image.open(data_path + '/' + image)))

    print("Image loading complete.")

    bbox_dict = dict.fromkeys(path_list)
    for i in range(len(list(bbox_dict.keys()))):
        im = image_list[i]
        # Create figure and axes
        fig, ax = plt.subplots(1)

        a = Annotate()
        # Display the image
        ax.imshow(im)
        plt.show()
        # NOTE: bbox = [xmax, xmin, ymax, ymin]
        x_s = sorted([a.x0, a.x1])
        y_s = sorted([a.y0, a.y1])
        bbox = [int(x_s[1]), int(x_s[0]), int(y_s[1]), int(y_s[0])]
        print(bbox)
        # associate a bounding box with each direct path to an image
        bbox_dict[path_list[i]] = bbox
    pickle.dump(bbox_dict.values(), open("cache/bbox_list", 'wb'))