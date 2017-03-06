from __future__ import print_function, division #makes it look pretty 
from builtins import input
 
from gopigo import * #imports gopigo library
import sys
import os
import picamera #imports picamera
import time #imports the delay funtion


#allows for the controls to be displayed on screen
def print_menu():
	print
	print("  Controls")
	print
	print("  Type '1' to run stream")
	print("  Type '2' to take picture")
	print("  Type '?' to reprint menu")

#takes a picture
def takephoto():
	camera = picamera.PiCamera()
	camera.capture('image.jpg')
	camera.close() # closes the camera so that the stream can be reopend 
print_menu()
while True:
	print("\nCmd:",end="")
	inp=input()
	if inp=='1':
		os.system('./raspberry_pi_camera_streamer') #calls the streaming script and runs it
	elif inp=='2': # takes a picture
		takephoto()
	elif inp=='?':
		print_menu()
