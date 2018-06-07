#!/usr/bin/env python3
import cv2
import numpy as np

img = cv2.imread('img.jpeg')

hint = '''
Give cropped image size like 1/2 ,1/3 etc as 2, 3 ..
'''

img_shape = img.shape
print('Image size : ',img_shape)
print(hint)
size = input('size = ')

rows = int(img_shape[0]/int(size))
cols = int(img_shape[1]/int(size))

cropped_img = img[:rows,:cols,:]

cv2.imshow("original Image",img)
cv2.imshow("Cropped Image",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()