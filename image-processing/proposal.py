import cv2

image = cv2.imread('mars_horizon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image',image)
cv2.imshow('Grayscale Image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()