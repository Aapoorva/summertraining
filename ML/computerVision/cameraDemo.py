#!/usr/bin/env python3

import cv2

#loading camera to capture video
cam = cv2.VideoCapture(0)

i = 0
#checking camera open or not
while cam.isOpened() :
	#reading image
	status,frame = cam.read()
	cv2.imshow('camera0',frame)
	#storing image
	if i < 1000 and i%2 == 0 :
		cv2.imwrite('./captured_frames/img'+str(i)+'.jpg',frame)
	#to store camera
	if  cv2.waitKey(1) & 0xFF == ord('q') :
		cv2.destroyAllWindows()
		break
	i+=1
#to close camera
cam.release()