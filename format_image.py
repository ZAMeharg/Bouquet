#! /usr/bin/env python3
#3/3 Starting the functions of Bouquet
'''
Need to make sure to add in the install section
	pip install rembg
	pip instal PIL
	pip install argparse
'''
from rembg import remove #For removing background
from PIL import Image # For removing background
import os
import sys
from pathlib import Path
import glob
import time
global pic_list, imgs
imgs = []
pic_list = []
def image_list(directory):
    imgs = []
    #Creates the path to the directory we are looking for images in
    path = Path(directory)
    #creates the list of files in the image directory
    files = os.listdir(path)
    #For loop scearching the directory only for images
    for file in files:
        if file.endswith(('.jpg', '.png', '.jpeg','.CR2')):
            img_path = str(path) + "/" + file
            imgs.append(img_path)
    return imgs 

### Changing all the .img files into .png ###
def image_converter(directory):
    imgs = image_list(directory)
    for pic in imgs:
    	if pic.endswith(('.jpeg')):
    		img = Image.open(pic)
    		rgb_im = img.convert('RGB')
    		rgb_im.save(pic.replace("jpeg","png"))
    	if pic.endswith(('.jpg')):
    		img = Image.open(pic)
    		rgb_im = img.convert('RGB')
    		rgb_im.save(pic.replace("jpg","png"))

'''Runs through the directory creating a list that contains all the .png images.
One thing to note is that this pic_list will contain a list of all the images that are .png in testing this has been duplicating some of the
.png images. To solve this we will use the set() command to create a new pic_list that will be the unique set of images we will do any all of our
next analysis on!
'''
def png_list(directory):
	pic_list = []
	imgs = image_list(directory)
	image_converter(directory)
	for pic in imgs:
		if pic.endswith(('.png')):
			pic_list.append(pic)
	#print(pic_list)
	return pic_list
'''
Remove_background is going to go through the pic_lists for each picture and remove the background using Pillow image.
This function also has a feature that tells you how long it took to remove the background for that image. 
'''
def remove_background(directory):
	n = 0
	pic_list = png_list(directory)
	pics_list = set(pic_list)
	num_pics = len(pics_list)
	for picture in pics_list:
		start = time.time()
		input = Image.open(picture)
		no_bg = remove(input)
		no_bg.save(picture.replace("jpeg","png"))
		stop = time.time()
		pic_name = os.path.basename(picture)
		run_time = stop-start
		run_time = str(run_time)
		print("Removed background on " + pic_name + "\n" + "Run time: " + run_time + " secs")
		n += 1
		if n == num_pics:
			exit()