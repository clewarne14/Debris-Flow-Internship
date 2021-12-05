# Used Pillow Docs at https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html for help
# Font OdubeeSans-Regular.ttf is downloaded from Google Fonts at https://fonts.google.com/specimen/Odibee+Sans#pairings
# Function for finding file extension found at https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
# Iterating through files found at https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
# Numbers for Exif Tags found at https://www.exiv2.org/tags.html
# OpenCV docs used at https://docs.opencv.org/3.4/d9/df8/tutorial_root.html for help with OpenCV
# Help with user input in Python found at https://www.geeksforgeeks.org/taking-input-in-python/
# Check if the file is a directory found at https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/

import cv2 as cv
import os, time, glob
from PIL import Image
import sys
from pathlib import Path

# A function to recursively add text to pictures and add them as frames of the video
def Rec(folderInp):
    # os.path
    # files = glob.glob("./*")
    # files = 
    #folderInp = "/Users/clewarne/" + folderInp
    os.chdir(folderInp)
    #filepath = os.listdir(folderInp)
    filepath = glob.glob("*")
    #print(os.path)
    filepath.sort(key=os.path.getmtime)
    
    # A loop to execute on every file in the directory given, they are sorted alphabetically
    for files in filepath:
       # print(files)
       #files = files[2:]
       # print(files)

       # Some String manipulation for file paths below, the above is some string manipulation, for some reason
       # this is necessary sometimes with the hard drive, I do not understand why this is
        f = os.path.join(folderInp,files)
        names = os.path.splitext(f)
        # If the file being looked at is actually a directory, the code is essentially paused, this same
        # function is then called using a file path that is extended with the new directory appended on it
        if os.path.isdir(f):
            tempInp = folderInp
            folderInp = f
            Rec(folderInp)
            folderInp = tempInp
        # If the file is an image, (.PNG, .jpg, .jpeg, etc.), the next part is executed, if not, it is skipped
        # and the next file is accessed at the start of the for loop
        if names[1] == '.PNG' or names[1] == '.jpg' or names[1] == '.jpeg' or names[1] == '.JPG' or names[1] == '.png' or names[1] == '.JPEG':
            img = cv.imread(cv.samples.findFile(f))
            with Image.open(f).convert("RGBA") as base:
                # Gets the date and time of the picture using exif tags
                dateTime = base.getexif()[0x0132]
            # Prints the date and time that will be added to the picture, this is for me to make sure that the program is
            # running well while it is happening
            print(dateTime)
            # Creates a new image object by combining the old image and the text, this new image is not saved
            newImg = cv.putText(img,dateTime,(100,200),cv.FONT_HERSHEY_SIMPLEX,4.0,(0,0,0),10,cv.FILLED,False)
            # The image is then added as the next frame of the video that we defined in the beginning
            vidOutput.write(newImg)

# A function to add text to the pictures in the folder given. However, in this function,
# folders are skipped over like other, non-image files and no recursion occurs
def noRec():

    # folderInp = "/Users/clewarne/" + folderInp
    os.chdir(folderInp)
    # filepath = os.listdir(folderInp)
    filepath = glob.glob("*")
    # print(os.path)
    filepath.sort(key=os.path.getmtime)
    # A loop to execute on every file in the directory given, they are sorted alphabetically
    for files in filepath:
        # print(files)
        # files = files[2:]
        # print(files)

        # Some String manipulation for file paths below, the above is some string manipulation, for some reason
        # this is necessary sometimes with the hard drive, I do not understand why this is
        f = os.path.join(folderInp,files)
        names = os.path.splitext(f)
        # If the file is an image, (.PNG, .jpg, .jpeg, etc.), the next part is executed, if not, it is skipped
        # and the next file is accessed at the start of the for loop
        if names[1] == '.PNG' or names[1] == '.jpg' or names[1] == '.jpeg' or names[1] == '.JPG' or names[1] == '.png' or names[1] == '.JPEG':
            img = cv.imread(cv.samples.findFile(f))
            with Image.open(f).convert("RGBA") as base:
                # Gets the date and time of the picture using exif tags
                dateTime = base.getexif()[0x0132]
            # Prints the date and time that will be added to the picture, this is for me to make sure that the program is
            # running well while it is happening
            print(dateTime)
            # Creates a new image object by combining the old image and the text, this new image is not saved
            newImg = cv.putText(img,dateTime,(100,200),cv.FONT_HERSHEY_SIMPLEX,4.0,(0,0,0),10,cv.FILLED,False)
            # The image is then added as the next frame of the video that we defined in the beginning
            vidOutput.write(newImg)
# Gets inputs to determine locations of files that will be the input or output, along with some preferences
folderInp = input("File path for folder that contains pictures to add text to: ")
folderOut = input("Folder to add the completed time lapse to: ")
OutputStr = input("What would you like to name the time lapse? ")
folders = input("Would you like to read any subfolders in the current directory?(y/n) ")
# folderInp = '2019_Selected_Time_Lapse_Photos_copy'
# folderOut = 'OutputTest'
# OutputStr = 'PresentationDemo'
# folders = 'y'

# Some simple string manipulation to create actual file paths
fileNum = 0
fileStr = ""
if folderOut != '':
    folderOut += '/'
outputLoc = folderOut + OutputStr + '.mov'
text = ""
dateTime = ""
# Creating an empty video with no frames, this will be added to
vidOutput = cv.VideoWriter(outputLoc,cv.VideoWriter_fourcc(*'jpeg'),15,(6000,4000))
# Getting the exact time, mainly for debugging, to determine later how long the program takes to execute
ts = time.time()

# There are two functions to be executed, one if subfolders are to be looped through and one if they are not
# The one that is executed is determined by the user's answer to the question earlier
if folders == 'y':
    Rec(folderInp)
else:
    noRec()


# Check current time and calculate the amount of time this process has taken, the above functions will have
# completed entirely before these execute
tm = time.time()
print(tm - ts)

# Below this, is a piece of code that I may need in the future to check if an image is empty,
# I may use this somewhere so I am keeping it at the bottom for now

#if img is None:
 #   sys.exit("Could not read image")

