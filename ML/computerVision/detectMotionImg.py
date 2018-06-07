#!/usr/bin/env python3

import cv2

pic1 = cv2.imread('captured_frames/img1.jpg')
pic2 = cv2.imread('captured_frames/img101.jpg')
pic3 = cv2.imread('captured_frames/img201.jpg')


pic1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2GRAY)
pic2 = cv2.cvtColor(pic2,cv2.COLOR_BGR2GRAY)
pic3 = cv2.cvtColor(pic3,cv2.COLOR_BGR2GRAY)


diff1 = cv2.absdiff(pic1,pic2)
diff2 = cv2.absdiff(pic2,pic3)

diff_and = cv2.bitwise_and(diff1,diff2)

ret,thresh1 = cv2.threshold(diff_and,127,255,cv2.THRESH_BINARY)

cv2.imshow('diff',diff_and)
cv2.imshow('threshold',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(diff_and.shape)