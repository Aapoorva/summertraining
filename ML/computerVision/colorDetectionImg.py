#!/usr/bin/env python3

import cv2

img = cv2.imread('shrek.jpg')

#to show only red image
blue_only = cv2.inRange(img,(10,100,100),(255,190,190))
green_only = cv2.inRange(img,(0,40,40),(80,255,255))

cv2.imshow('Original',img)
cv2.imshow('Blue Detect',blue_only)
cv2.imshow('Green Detect',green_only)

cv2.waitKey(0)
cv2.destroyAllWindows()