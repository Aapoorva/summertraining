#!/usr/bin/env python3

import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened() :
	status,frame = cam.read()
	#to show only red image
	red_only = cv2.inRange(frame,(0,0,40),(40,40,255))
	
	cv2.imshow('Red Detect',red_only)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		cv2.destroyAllWindows()
		break
cam.release()