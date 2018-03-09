# usr/bin/python3
# coding = uft-8

import cv2  
import sys


path = sys.argv[1]
vc = cv2.VideoCapture(path)
c=1  
  
if vc.isOpened():
	rval , frame = vc.read()  
else:
	rval = False
	print('read-file-error')

# frame interval
timeF = 1

while rval:   
    rval, frame = vc.read()  
    if(c%timeF == 0):  
        cv2.imwrite('image'+str(c) + '.jpg',frame)  
    c = c + 1  
    cv2.waitKey(1)  
vc.release()  
