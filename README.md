# Bouquet
Created for BIOL 7180-D01 Scripting for Biologist @ Auburn University. This program was created to generate a final figure of images sorted by RGB, as well as create a pallete of colors from individial images. 

## Getting Started
Before running Bouquet, we will create a virtual environment using Python3 venv
```
mkdir venvs
cd venvs
module load python
python3 -m venvs Bouquet
```
Now that we have created a folder for the Bouqet program, we will active that virtual environment.
```
sorce Bouquet/bin/activate
```
Now we can install all the required packages.
```
pip install -r requirements.txt
```
Within this requirements.txt file are installing the following packages:
- math
- cv2
- os
- glob
- time
- sys
- sklearn.cluster
- collections
- skimage.color
- matplotlib
- numpy
- Pillow
- pathlib
- rembg 

### Example
> Bouquet.py <insert path to image><Image_name> <br>
> Image_name: RGB, Hexadecimal
>
> Boquet.py Boom_Boom_White_1.jpeg <br>
> Boom Boom White: 255,255,255 #FFFFFF
