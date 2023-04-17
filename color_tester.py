
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import cv2
from skimage.color import rgb2lab, deltaE_cie76
from collections import Counter
import os 
'''

picture = single


pic=imageio.imread(picture)
plt.figure(figsize=(10,10))
plt.imshow(pic)
image = cv2.imread(picture)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image) 

print('Type of the image : ',type(pic))
print('Shape of the image : {}'.format(pic.shape))
print('Hight of the image {}'.format(pic.shape[0]))
print('Width of the image {}'.format(pic.shape[1]))
print('Dimension of the Image {}'.format(pic.ndim)) 

print('Image size {}'.format(pic.size))
print('Maximum RGB value in this image {}'.format(pic.max()))
print('Minimum RGB value in this image {}'.format(pic.min()))

print('Value of only R channel {}'.format(pic[ 150, 100, 0]))
print('Value of only G channel {}'.format(pic[ 150, 100, 1]))
print('Value of only B channel {}'.format(pic[ 150, 100, 2]))
plt.title('R channel')
plt.imshow(pic[ : , : , 0])
plt.show()

plt.title('G channel')
plt.imshow(pic[ : , : , 1])
plt.show()

plt.title('B channel')
plt.imshow(pic[ : , : , 2])
plt.show()
'''

def RGB_HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_colors(image, number_of_colors, show_chart):
    picture = image
    pic=imageio.imread(image)
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image) 
    reshaped_image = cv2.resize(image, (600, 400))
    reshaped_image = reshaped_image.reshape(reshaped_image.shape[0]*reshaped_image.shape[1], 3)
    clf = KMeans(n_clusters = number_of_colors+1)
    labels = clf.fit_predict(reshaped_image)
    counts = Counter(labels)
    most_key = max(counts, key=lambda k:counts[k])
    most_value = counts[most_key]
    zero_value = counts[0]
    counts[most_key]=zero_value
    counts[0]=most_value
    counts = dict(sorted(counts.items(), key=lambda item: item[1]))
    counts = dict(list(counts.items())[:-1])
    counts = dict(sorted(counts.items()))
    new_counts = {}
    for i in range(number_of_colors):
        if i+1 in counts:
            new_counts[i] = counts[i+1]
    center_colors = clf.cluster_centers_
    black = np.argmin(np.sum(center_colors, axis =1))
    center_colors = np.concatenate((center_colors[:black],center_colors[black+1:]), axis=0)
    #center_colors = np.delete(center_colors,0,0)
    ordered_colors = []
    for i in new_counts.keys():
        if isinstance(i, int) and i >= 0 and i < len(center_colors):
            ordered_colors.append(center_colors[i])
    #hex_colors = [RGB_HEX(ordered_colors[i]) for i in new_counts.keys()]
    hex_colors = []
    for i in new_counts.keys():
        if i < len(ordered_colors):
            hex_color = RGB_HEX(ordered_colors[i])
            hex_colors.append(hex_color)
    print(hex_colors)
    rgb_colors = []
    for i in new_counts.keys():
        if i < len(ordered_colors):
            rgb_color = ordered_colors[i]
            rgb_colors.append(rgb_color)
    #rgb_colors = [ordered_colors[i] for i in new_counts.keys()]
    if show_chart == True:
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.show()
    return rgb_colors

#get_colors(image, 8, True)