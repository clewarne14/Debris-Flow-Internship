# Used Pillow Docs at https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html for help
# Font OdubeeSans-Regular.ttf is downloaded from Google Fonts at https://fonts.google.com/specimen/Odibee+Sans#pairings
# Function for finding file extension found at https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
# Iterating through files found at https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
# Numbers for Exif Tags found at https://www.exiv2.org/tags.html
# OpenCV docs used at https://docs.opencv.org/3.4/d9/df8/tutorial_root.html for help with OpenCV
# Help with user input in Python found at https://www.geeksforgeeks.org/taking-input-in-python/

import cv2 as cv
import os, time
from PIL import Image
import sys
#folderInp = input("File path for pictures to add text to: ")
folderOut = input("File path to add the completed time lapse to: ")
folderInp = '/Volumes/Untitled/DCIM/100CANON-September'
#folderOut += "/"
#lengthOfFolder = len(folderInp)
fileNum = 0
fileStr = ""
if folderOut != '':
    folderOut += '/'
outputLoc = folderOut + 'Output-September.mov'
vidOutput = cv.VideoWriter(outputLoc,cv.VideoWriter_fourcc(*'jpeg'),30,(6000,4000))
#folderOut = 'OutputTest/'
text = ""
dateTime = ""
ts = time.time()
for files in sorted(os.listdir(folderInp)):
    # print(files)
    #files = files[2:]
    # print(files)
    f = os.path.join(folderInp,files)
    names = os.path.splitext(f)
    if names[1] == '.PNG' or names[1] == '.jpg' or names[1] == '.jpeg' or names[1] == '.JPG' or names[1] == '.png' or names[1] == '.JPEG':
        img = cv.imread(cv.samples.findFile(f))
        with Image.open(f).convert("RGBA") as base:
            dateTime = base.getexif()[0x0132]
        #dateTime = text[0x0132]
        print(dateTime)
        newImg = cv.putText(img,dateTime,(100,200),cv.FONT_HERSHEY_SIMPLEX,4.0,(0,0,0),10,cv.FILLED,False)
        # if fileNum % 100 == 0:
        #     print(fileNum)

        #cv.imshow("Display Window", newImg)
        #k = cv.waitKey(0)name_exten[0][lengthOfFolder:]
        # if fileNum < 10:
        #     fileStr = "IMG_000" + str(fileNum)
        # elif fileNum < 100:
        #     fileStr = "IMG_00" + str(fileNum)
        # elif fileNum < 1000:
        #     fileStr = "IMG_0" + str(fileNum)
        # else:
        #     fileStr = "IMG_" + str(fileNum)

        #cv.imwrite(folderOut + fileStr + ".JPG",newImg)
        fileNum = fileNum + 1
        vidOutput.write(newImg)

tm = time.time()
print(tm - ts)
# capture = cv.VideoCapture("OutputTest/IMG_%04d.JPG")
# width = int(capture.get(3))
# videoSize = (int(capture.get(3)), int(capture.get(4)))
# print(capture.isOpened())
# ret, frame = capture.read()
# if ret == True:
#     cv.imshow("Frame",frame)
#     cv.waitKey(0)
#cv.VideoWriter("outputFile.mov")
#if img is None:
 #   sys.exit("Could not read image")


#newImg = cv.putText(img,"Hello",(100,200),cv.FONT_HERSHEY_SIMPLEX,4.0,(0,0,0),10,cv.FILLED,False)
#cv.imshow("Display Window", newImg)
#k = cv.waitKey(0)
#cv.imwrite("IMG_6188.PNG",newImg)

