#! /usr/bin/env python3
'''
#################################################################################
# This is the script that will be used to run all other scripts                 #
#                                                                               #
#                                                                               #
#                                                                               #
#                                                                               #
#                                                                               #
#                                                                               #
#                                                                               #
#                                                                               #
#################################################################################

'''
import color_analyzer as ca
import format_image as fi
import argparse
import arranger as ar

#Adding in flags to running Bouquet in two differnet modes single or arrangement
parser = argparse.ArgumentParser(
                    prog='Bouquet',
                    description='Color analysis of floral blooms')
                    #epilog='Text at the bottom of help')
parser.add_argument("-s", "--single", type = str, help="Single Picture")
parser.add_argument("-a", "--arrangement",help="Uses the arrangement function of Boquent, requires the -d flag inorder to properally run", action = 'store_true')
parser.add_argument("-d", "--directory", type = str, help = "Directory where input images are stored")
parser.add_argument("-p", "--project_name", type = str, help= "Project Name")
parser.add_argument("-c", "--color_numbers", type = int, help = "Number of colors that will be outputted")
parser.add_argument("-l", "--light_mode", action = 'store_true', help= "Puts the backgound of the arrangement into light mode")
parser.add_argument("-r", "--remove_background", action = 'store_true', help = "Removed the background of the images in the given directory")
args = parser.parse_args()
#print(args.directory)

directory = args.directory
single = args.single
number_of_colors = args.color_numbers
p_name = args.project_name
arrangement = args.arrangement
project = args.project_name
mode = args.light_mode
remove_bg = args.remove_background

if __name__ == '__main__':
    if (remove_bg == True) and (bool(directory) == True):
        print("Removing background from the images in " + directory)
        fi.remove_background(directory)
    if (bool(single) == True):
        if (number_of_colors > 0):
            ca.get_colors(single, number_of_colors, True, project)
        if (number_of_colors == 0):
            print("Please change the -c flag to a number greater than 0!")
    if (bool(arrangement) == True):
        if (bool(directory) and (bool(project)) == True):
            print("We are now arranging images from " + directory)
            ar.vase(directory, project, mode)
        if (bool(directory) == False):
            print("Use the -d flag to accurately use the --arrangement flag.")
        if (bool(project) == False):
            print("Use the -p flag to name the final image create with the --arrangement flag.")



