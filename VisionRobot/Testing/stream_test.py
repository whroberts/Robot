from __future__ import print_function, division #makes it look pretty 
from builtins import input
 
from gopigo import * #imports gopigo library
import sys
import os
import picamera #imports picamera
import time #imports the delay funtion
"""
import pygame
pygame.init()

size = [500,700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

pygame.joystick.init()
"""
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
"""	
while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
	joystick_count = pygame.joystick.get_count()
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()

	if joystick.get_button(0)==True:
		takephoto()
	if joystick.get_button(3)==True:
		os.system('./raspberry_pi_camera_streamer')
"""
