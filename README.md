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

## Running Bouquet
The main line of code used to run Bouquet is:
```
python3 Bouquet
```

With flags:
> -h 	--help					Shows the help message and exits the program
> -s	--single				Used for single image analysis
> -a	--arrangemnt			Uses the arrangement function of Bouquet, requires the -d flag
> -d 	--directory				The directory where the input images are stored
> -p	--project_name			The name of the project
> -c	--color_numbers			The number of colors required that will be outputted in the single use function
> -l	--light_mode			Puts the arrangement final image with a white backgroud
> -r	--remove_background		Removes the background of all the images in given directory 


## Running Bouquet
To use Bouquet the first thing we need to do is remove the backgrounds of all the images we are wishing to use in either one of the two functions of Bouquet.
