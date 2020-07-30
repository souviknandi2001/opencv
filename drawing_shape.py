import cv2
img = cv2.imread('sample.jpg', -1)

img= cv2.circle(img,(300,300),60,(25,98,230),-1)
font= cv2.FONT_ITALIC
img = cv2.putText(img,"souvik",(250,250),font,5,(23,36,36),10,cv2.LINE_8)
cv2.imshow('image_window',img)

cv2.waitKey(0)
cv2.destroyAllWindows()