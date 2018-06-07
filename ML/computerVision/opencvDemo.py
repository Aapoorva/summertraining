#!/usr/bin/env python3

import cv2
img = cv2.imread('img.jpeg',1)
print("shape = ",img.shape)
print(img[0][0])

shape = img.shape

for i in range(int(shape[0]/2),shape[0]) :
	for j in range(0,shape[1]) :
		img[i][j][0] = img[i][j][0] - 50
		img[i][j][1] = img[i][j][1] - 50
		img[i][j][2] = img[i][j][2] - 50

cv2.imshow("fool",img)
cv2.waitKey(0)
cv2.destroyAllWindows()