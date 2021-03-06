
#importing the required libraries
import cv2
import matplotlib.pyplot as plt


image = cv2.imread('../test_images/apple.jpeg')
rows, cols = image.shape[:2]

# (col/2,rows/2) is the center of rotation for the image M is the cordinates of the center

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(image, M, (cols, rows))
plt.imshow(dst)
cv2.imwrite('../output_images/rotated_image.jpg', dst)
plt.show()
