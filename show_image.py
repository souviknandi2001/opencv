import cv2
img = cv2.imread('sample.jpg', -1)
cv2.imshow('image_window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
