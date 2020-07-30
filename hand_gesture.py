import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)
prev_y = 1000

lower= np.array([110, 50, 50])
upper= np.array([130, 255, 255])

while True:
    ret, frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv,lower,upper)
    countours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for c in countours:
        area =  cv2.contourArea(c)
        if area >300:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 0, 245),2)
            if y>prev_y:
                font = cv2.FONT_ITALIC
                frame = cv2.putText(frame, "moving down", (50, 250), font, 1, (23, 36, 236), 3, cv2.LINE_8)
                #pyautogui.press("space")
            prev_y=y
            #cv2.drawContours(frame, c, -1, (0, 0, 245), 2)

    #cv2.imshow("mask",mask)
    cv2.imshow("frame",frame )
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()