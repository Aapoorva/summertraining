#!/usr/bin/env python3
import cv2
import numpy as np

#loading camera
cam = cv2.VideoCapture(0)

i=1

# to store list of images
img_list = []

# to store diffrence
diff=[]

while cam.isOpened() :

	status,frame = cam.read()

	cv2.imshow('camera0',frame)

	# next image name
	nxt_img_name = 'captured_frames/img'+str(i)+'.jpg'
	
	# converting to gray scale
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# storing gray scale image to list
	img_list.append(gray_frame)

	# storing image
	cv2.imwrite(nxt_img_name,frame)

	# calculating difference
	if i>=2 :
		abs_diff = cv2.absdiff(img_list[i-2],img_list[i-1])
		diff.append(abs_diff)
	
	# detecting motion
	if i>=3 :
		img_diff = cv2.bitwise_and(diff[i-3], diff[i-2])

		cv2.imshow('moved image',img_diff)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		cv2.destroyAllWindows
		break

	i+=1

cam.release()