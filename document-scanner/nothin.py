src.create(rows, cols, CV_8UC1)
src = imread("/home/pi/Desktop/ima.jpg", CV_8UC1)

img = cv2.adaptiveThreshold(src, dst, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 75, 10)
cv2.imshow("A", img)
