import cv2

#event = [i for i in dir(cv2) if "EVENT" in i]
#print(event)
def click_event(event, x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        text= str(str(x)+","+str(y))
        font = cv2.FONT_ITALIC
        cv2.putText(img , text,(x,y),font,.51,(0,0,222),2)
        cv2.imshow('''souvik's display''',img)

    if event== cv2.EVENT_RBUTTONDOWN:
        blue= img[x,y,0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        text= str(str(blue)+","+str(green)+","+str(red))
        font = cv2.FONT_ITALIC
        cv2.putText(img , text,(x,y),font,.51,(0,240,222),2)
        cv2.imshow('''souvik's display''',img)



img = cv2.imread('sample.jpg', -1)
cv2.imshow('''souvik's display''',img)

cv2.setMouseCallback('''souvik's display''',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()