import cv2
from matplotlib import pyplot as plt
img = cv2.imread("sample.jpg",-1)
cv2.imshow("frame",img)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()