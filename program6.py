##### Bordering an image
# cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)
# SOLID Border around an image
import cv2

img = cv2.imread("pika.png")
borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=1)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
