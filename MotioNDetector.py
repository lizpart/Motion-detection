import cv2
import numpy as np
import datetime
import imutils


rec=cv2.VideoCapture(0)
sto, mapping1=rec.read()
sto, mapping2=rec.read()

while rec.isOpened():
    sub=cv2.absdiff(mapping1, mapping2)
    convclr=cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(convclr, (3, 3), 1)
    _, thresh=cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    enlarged=cv2.dilate(thresh, None, iterations=1)
    contours, _=cv2.findContours(enlarged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if mapping1 is None:
        break

    #Reframe the frame convert it to grayscale then blur it
    mapping1 = imutils.resize(mapping1, width=900)
    convclr1 = cv2.cvtColor(mapping1, cv2.COLOR_BGR2GRAY)
    convclr2 = cv2.GaussianBlur(convclr1,(21, 21), 0)

    if mapping1 is None:
        mapping1=convclr2
        continue
    #Compute the absolute difference betweeen the first frame that we already stored.
    frameDelta = cv2.absdiff(convclr2, convclr1)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # dilate the image to fill in the holes and find contours on threshold image
    thresh = cv2.dilate(thresh, None, iterations=2)
    count = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = imutils.grab_contours(count)

    for count in contours:
        (x, y, w, h)=cv2.boundingRect(count)
        if cv2.contourArea(count)<700:
            continue
        cv2.rectangle(mapping1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(mapping1, "REPORT: {}".format('WE HAVE DETECTED ADUDA IN THIS PREMISES'), (5, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 4)
        cv2.putText(mapping1, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, mapping1.shape[0]-10),cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 22)
    cv2.imshow("FOOTAGE", mapping1)
    cv2.imshow("MARGIN", thresh)
    cv2.imshow("DIFFERENCE OF DELTA FRAMES", frameDelta)

    mapping1=mapping2
    sto, mapping2=rec.read()

    if cv2.waitKey(50)==50:
        break

cv2.destroyAllWindows()
