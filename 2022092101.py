import cv2
img = cv2.imread("1.png")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)





cv2.imshow("1", img)
cv2.imshow("2", img1)
cv2.waitKey()
cv2.destroyAllWindows()