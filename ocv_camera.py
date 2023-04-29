import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sobelX = cv.Sobel(gray, cv.CV_16S, 1, 0)
    sobelY = cv.Sobel(gray, cv.CV_16S, 0, 1)
    sobel = abs(sobelX) + abs(sobelY)
    sobmin = 0
    sobmax = 0
    sobmin, sobmax, min_loc, max_loc = cv.minMaxLoc(sobel) 
    sframe = cv.convertScaleAbs(sobel, alpha=255.0 / (sobmax - sobmin), beta = 0)
    #nsframe = cv.bitwise_not(sframe)
    nsframe = cv.bitwise_not(gray)
    # Display the resulting frame
    cv.imshow('org_frame', frame)
    cv.imshow('gray_frame', nsframe)#gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()