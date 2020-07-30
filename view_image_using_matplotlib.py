import cv2
import numpy
from matplotlib import pyplot
img = numpy.zeros((512,512,3),numpy.uint8)
cv2.imshow("frame",img)

pyplot.imshow(img)
pyplot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()