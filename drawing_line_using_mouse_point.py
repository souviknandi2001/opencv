import cv2
import numpy


def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0, 0, 245), -1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(2,23,245),1)
        cv2.imshow("image", img)


img = numpy.zeros((512,512,3) ,numpy.uint8)
cv2.imshow("image", img)
points=[]

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
