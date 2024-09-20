# Python program for blending of
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
img1 = cv2.imread('ash.png', 1)

# Read image2
img2 = cv2.imread('pika.png', 1)

# Blending the images with 0.3 and 0.7
img = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

# Show the image
cv2.imshow('image', img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()