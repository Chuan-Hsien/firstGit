import numpy as np
import cv2 as cv
rframe = cv.imread("jam1.jpg")
frame = cv.resize(rframe, (640,480), interpolation=cv.INTER_AREA)
#gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#sobelX = cv.Sobel(gray, cv.CV_16S, 1, 0)
#sobelY = cv.Sobel(gray, cv.CV_16S, 0, 1)
#sobel = abs(sobelX) + abs(sobelY)
#sobmin = 0
#sobmax = 0
#sobmin, sobmax, min_loc, max_loc = cv.minMaxLoc(sobel) 
#sframe = cv.convertScaleAbs(sobel, alpha=255.0 / (sobmax - sobmin), beta = 0)
#nsframe = cv.bitwise_not(sframe)
h, s, v = cv.split(hsv)
#sframe = cv.bitwise_not(b)
ret,nsframe = cv.threshold(h,64,255,cv.THRESH_BINARY_INV)
# Display the resulting frame
#cv.imshow('org_frame', frame)
#cv.imshow('gray_frame', nsframe)
b, g, r = cv.split(frame)

ret,nsframe1 = cv.threshold(b,127,255,cv.THRESH_BINARY_INV)
ginv = cv.bitwise_not(nsframe1)

result = cv.bitwise_and(nsframe, ginv)

cv.imshow("Org", frame)
cv.imshow("HSV",hsv)
cv.imshow("H",h)
cv.imshow("Blue", b)
#cv.imshow("Green", g1)
#cv.imshow("Red",r1)
#cv.imshow("s",sframe)
cv.imshow("ns",nsframe)
cv.imshow("ginv",ginv)
cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()