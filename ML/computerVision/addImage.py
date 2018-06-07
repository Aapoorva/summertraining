#!/usr/bin/python3

import cv2

img1 = cv2.imread('shrek.jpg')
img2 = cv2.imread('bridge.jpg')

#to add in equal portions
addedImage = cv2.add(img1,img2)

#to add in percentage
wghtdAdd = cv2.addWeighted(img1,0.9,img2,0.2,1)

# cv2.imshow('Image 1',img1)
# cv2.imshow('Image 2',img2)
# cv2.imshow('Added Image',addedImage)
cv2.imshow('Weighted Image 1',wghtdAdd)

cv2.waitKey(0)
cv2.destroyAllWindows()