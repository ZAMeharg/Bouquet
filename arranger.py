'''This script has the code to do the arrangement image.
Things this program needs to properally run:
1) A list of images [X]
2) A way to find the the GCF of the size of the list to crate the best possible matrix for that image [x]
3) Removing the backgrounds from all the images using fi.remove_background [X]
4) Get the most dominant color in each image after removing black from the color list [X]
5) Sorting the overall list ot create the sorted matrix of colors
6) Resize the image but keeping the correct quality of the image (eh not supper import for small images)
7) Creating an image using that matix list
'''
import format_image as fi
import color_analyzer as ca
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os
from PIL import Image

'''
===========================================
              picture_counter              
===========================================
input: directory

output: num_pics, a


def picture_counter(directory):
	pic_list = fi.png_list(directory)
	pic_list = set(pic_list)
	num_pics = len(pic_list)
	return num_pics
'''

def color_getter(directory):
    pic_list = fi.png_list(directory)
    #print(pic_list)
    pic_list = set(pic_list)
    num =len(pic_list)
    #for image in pic_list:
    #    fi.remove_background(directory)
    #print(num)
    for image in pic_list:
        name = os.path.basename(image)
        rgb_colors = ca.get_colors(image,1,False)
        rgb_colors = str(rgb_colors[0])
        rgb_colors = rgb_colors.replace('array(', '').replace(')', '')
        #print("Dominant color for "+name+":"+ "\t" + "RGB Code: "+str(rgb_colors))
        return rgb_colors

def idk_anymore(directory):
    image_data = {}
    pic_list = fi.png_list(directory)
    pic_list = set(pic_list)
    rgb_colors = color_getter(directory)
    for name in pic_list:
        rgb_colors = ca.get_colors(name,1,False)
       # read in image and process data
        color = rgb_colors
        image_data[name] = color
        image_data = dict(sorted(image_data.items(), key=lambda x: np.sum(x[1])))
    return image_data

def create_matrix(directory):
    image_data = idk_anymore(directory)
    num_images = len(image_data)

    # Compute the number of rows and columns needed to fit all images
    rows = int(num_images**0.5)
    cols = rows + 1 if rows * (rows + 1) < num_images else rows

    # Create the matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            index = i * cols + j
            if index < num_images:
                row.append(index)
            else:
                row.append(None)
        matrix.append(row)

    return matrix


def vase(directory, project, mode):
    colors = {}
    image_data = idk_anymore(directory)
    rows = list(image_data.keys())
    for key, value in image_data.items():
        value_str = str(value[0])
        colors[value_str] = key
    new_colors = {}
    for i,k in enumerate(colors):
        new_colors[i] = colors[k]
    for key in new_colors:
        new_colors[key] = new_colors[key].split('/')[1]
    num_images = len(new_colors)
    num_rows = int(math.sqrt(num_images))
    num_cols = math.ceil(num_images / num_rows)
    matrix = create_matrix(directory)
    cols = list(set(colors))
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            found_match = False
            for val in image_data[row]:
                if np.array_equal(col, val):
                    found_match = True
                    break
            if found_match:
                matrix[i,j] = 1
    name_matrix = []
    for row in matrix:
        row_names = []
        for key in row:
            row_names.append(new_colors[key])
        name_matrix.append(row_names)


    images = {}
    for i, filename in new_colors.items():
        img = Image.open(os.path.join(directory, filename))
        images[i] = img

    fig_width = num_cols * 2
    fig_height = num_rows * 2
    subplot_size = max(1, 20 - num_images)
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(fig_width, fig_height))
    fig.subplots_adjust(hspace=0.001, wspace=0.001)
    axs = axs.flatten()
    counter = 0
    for i in range(num_rows):
        for j in range(num_cols):
            img = Image.open(os.path.join(directory, name_matrix[i][j]))
            print("Loading " + name_matrix[i][j])
            axs[i*num_cols + j].imshow(img)
            axs[i*num_cols + j].axis('off')
            counter += 1
    print("Arranged " + str(counter) + " images!")
    
    # Set the background color of the figure to black
    if mode == True:
        fig.patch.set_facecolor('white')
    else:
        fig.patch.set_facecolor('black')

    # Show the plot
    plt.savefig(project+".png")
    plt.show()
