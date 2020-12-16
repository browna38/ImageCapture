#!/usr/bin/env python

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import numpy
import atexit
import os

def exit_handler():
    print('My application is ending!')
    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows() 


# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

i = 0
while os.path.exists(f"outpy{i}.avi"):
    i += 1
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(f'outpy{i}.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))


while(True):
    ret, frame = cap.read()
        
        # Write the frame into the file 'output.avi'
    out.write(frame)

    # Display the resulting frame    
    #cv2.imshow('frame',frame)


 

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows() 

atexit.register(exit_handler)