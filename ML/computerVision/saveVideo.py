#!/usr/bin/env python3

import cv2

#loading camera
cap = cv2.VideoCapture(0)


#storing frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#decidng video format
video_format = cv2.VideoWriter_fourcc(*'XVID')

video_output=cv2.VideoWriter('adhoc.avi',video_format,50.0,(frame_width,frame_height))

while cap.isOpened() :

	status,frame = cap.read()

	cv2.imshow('camera0',frame)

	video_output.write(frame)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		cv2.destroyAllWindows()
		break

cap.release()