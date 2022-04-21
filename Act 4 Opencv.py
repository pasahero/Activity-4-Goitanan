import cv2
path = 'lena.jpg'
windowTitle = 'ang angas mo ah'
CVimage = cv2.imread(path, 1)
cv2.imshow(windowTitle, CVimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
