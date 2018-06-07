#!usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread('img.jpeg')

my_img = np.zeros((512,512,3))

for i in range(0,512) :
	for j in range(0,512) :
		my_img[i][j][0] = 0
		my_img[i][j][1] = 255
		my_img[i][j][2] = 0

print(img.shape)
cv2.line(my_img,(100,100),(500,512),(250,0,0),5)
#			#img 	#text 			 #position	#font 		    #font size #color #line width #line type
cv2.putText(my_img,'testing put test',(200,200),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),10,cv2.LINE_AA)

cv2.imshow("fooool",img)
cv2.imshow("my img",my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()