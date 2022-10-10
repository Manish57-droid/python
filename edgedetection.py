import cv2
import numpy as np

FILE_NAME = 'img/car.jpg'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Canny edge detection.
	# blackwhite = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(img, 100, 100)

	# Write image back to disk.
	# cv2.imshow("Blackwhite",blackwhite)
	# cv2.imshow("canny", FILE_NAME)
	cv2.imshow("cannys", edges)
except IOError:
	print ('Error while reading files !!!')

cv2.waitKey(0)

